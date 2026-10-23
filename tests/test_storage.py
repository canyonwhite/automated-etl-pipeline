import pytest
from botocore.exceptions import ClientError

from retail_pipeline.ingestion import (
    DatasetSpec,
    inspect_csv,
    save_manifest,
)
from retail_pipeline.storage import upload_batch


class FakeS3:
    def __init__(self):
        self.objects = {}

    def put_object(self, **kwargs):
        identifier = (
            kwargs["Bucket"],
            kwargs["Key"],
        )

        if identifier in self.objects:
            raise ClientError(
                {
                    "Error": {
                        "Code": "PreconditionFailed",
                        "Message": "Object already exists",
                    }
                },
                "PutObject",
            )

        body = kwargs["Body"]

        self.objects[identifier] = {
            "Body": body,
            "ContentLength": len(body),
            "Metadata": kwargs["Metadata"],
        }

    def head_object(self, Bucket, Key):
        obj = self.objects[(Bucket, Key)]

        return {
            "ContentLength": obj["ContentLength"],
            "Metadata": obj["Metadata"],
        }

@pytest.fixture
def prepared_batch(tmp_path):
    source = tmp_path / "orders.csv"

    source.write_text(
        "order_id,customer_id\n"
        "O1,C1\n"
        "O2,C2\n",
        encoding="utf-8",
    )

    spec = DatasetSpec(
        name="orders",
        required_columns=(
            "order_id",
            "customer_id",
        ),
        allow_extra_columns=False,
    )

    manifest = inspect_csv(
        source,
        spec,
        "0002",
    )

    manifest_path = tmp_path / "manifest.json"

    save_manifest(
        manifest,
        manifest_path,
    )

    return source, manifest_path

def test_upload_new_batch(prepared_batch):
    source, manifest = prepared_batch
    s3 = FakeS3()

    result = upload_batch(
        s3,
        "test-bucket",
        source,
        manifest,
    )

    assert result["raw_status"] == "uploaded"
    assert result["manifest_status"] == "uploaded"
    assert len(s3.objects) == 2

def test_upload_same_batch_twice(prepared_batch):
    source, manifest = prepared_batch
    s3 = FakeS3()

    upload_batch(
        s3,
        "test-bucket",
        source,
        manifest,
    )

    result = upload_batch(
        s3,
        "test-bucket",
        source,
        manifest,
    )

    assert result["raw_status"] == "already_exists"
    assert result["manifest_status"] == "already_exists"
    assert len(s3.objects) == 2

def test_reject_changed_source(prepared_batch):
    source, manifest = prepared_batch
    s3 = FakeS3()

    source.write_text(
        "order_id,customer_id\n"
        "O1,CHANGED\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="no longer matches",
    ):
        upload_batch(
            s3,
            "test-bucket",
            source,
            manifest,
        )

    assert len(s3.objects) == 0