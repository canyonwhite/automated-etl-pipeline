import pytest

from retail_pipeline.warehouse import (
    ORDER_COLUMNS,
    verify_s3_batch,
)


class FakeS3:
    def __init__(self, size, checksum):
        self.size = size
        self.checksum = checksum

    def head_object(self, Bucket, Key):
        return {
            "ContentLength": self.size,
            "Metadata": {
                "sha256": self.checksum,
            },
        }


@pytest.fixture
def manifest():
    return {
        "dataset": "orders",
        "batch_id": "0002",
        "columns": list(ORDER_COLUMNS),
        "row_count": 2,
        "file_size_bytes": 100,
        "sha256": "a" * 64,
    }


def test_valid_s3_batch(manifest):
    s3 = FakeS3(
        size=100,
        checksum="a" * 64,
    )

    key = verify_s3_batch(
        s3,
        "test-bucket",
        manifest,
    )

    assert key == (
        "raw/olist/orders/batch_id=0002/orders.csv"
    )


def test_reject_checksum_mismatch(manifest):
    s3 = FakeS3(
        size=100,
        checksum="b" * 64,
    )

    with pytest.raises(ValueError, match="does not match"):
        verify_s3_batch(
            s3,
            "test-bucket",
            manifest,
        )


def test_reject_invalid_batch_id(manifest):
    manifest["batch_id"] = "../bad-batch"

    s3 = FakeS3(
        size=100,
        checksum="a" * 64,
    )

    with pytest.raises(ValueError, match="Invalid batch ID"):
        verify_s3_batch(
            s3,
            "test-bucket",
            manifest,
        )