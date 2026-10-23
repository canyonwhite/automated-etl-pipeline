import pytest

from retail_pipeline.ingestion import (
    DatasetSpec,
    inspect_csv,
    save_manifest,
)


@pytest.fixture
def sample_csv(tmp_path):
    path = tmp_path / "orders.csv"

    path.write_text(
        "order_id,customer_id\n"
        "O1,C1\n"
        "O2,C2\n",
        encoding="utf-8",
    )

    return path


def test_valid_csv(sample_csv):
    spec = DatasetSpec(
        name="orders",
        required_columns=("order_id", "customer_id"),
        allow_extra_columns=False,
    )

    manifest = inspect_csv(sample_csv, spec, "0001")

    assert manifest["row_count"] == 2
    assert manifest["dataset"] == "orders"
    assert len(manifest["sha256"]) == 64


def test_missing_column(sample_csv):
    spec = DatasetSpec(
        name="orders",
        required_columns=(
            "order_id",
            "customer_id",
            "order_status",
        ),
        allow_extra_columns=False,
    )

    with pytest.raises(ValueError, match="Missing"):
        inspect_csv(sample_csv, spec, "0001")


def test_invalid_field_count(tmp_path):
    path = tmp_path / "invalid.csv"

    path.write_text(
        "order_id,customer_id\n"
        "O1,C1,EXTRA\n",
        encoding="utf-8",
    )

    spec = DatasetSpec(
        name="orders",
        required_columns=("order_id", "customer_id"),
        allow_extra_columns=False,
    )

    with pytest.raises(ValueError, match="field count"):
        inspect_csv(path, spec, "0001")


def test_repeated_batch(sample_csv, tmp_path):
    spec = DatasetSpec(
        name="orders",
        required_columns=("order_id", "customer_id"),
        allow_extra_columns=False,
    )

    manifest = inspect_csv(sample_csv, spec, "0001")
    destination = tmp_path / "manifest.json"

    assert save_manifest(manifest, destination) is True
    assert save_manifest(manifest, destination) is False

    sample_csv.write_text(
        "order_id,customer_id\nO1,CHANGED\n",
        encoding="utf-8",
    )

    changed = inspect_csv(sample_csv, spec, "0001")

    with pytest.raises(ValueError, match="different metadata"):
        save_manifest(changed, destination)


def test_missing_rows(sample_csv):
    sample_csv.write_text(
        "order_id,customer_id\n",
        encoding="utf-8",
    )

    spec = DatasetSpec(
        name="orders",
        required_columns=("order_id", "customer_id"),
        allow_extra_columns=False,
    )

    with pytest.raises(ValueError, match="No rows"):
        inspect_csv(sample_csv, spec, "0001")


def test_single_row(sample_csv):
    sample_csv.write_text(
        "order_id,customer_id\nO1,C1\n",
        encoding="utf-8",
    )

    spec = DatasetSpec(
        name="orders",
        required_columns=("order_id", "customer_id"),
        allow_extra_columns=False,
    )

    manifest = inspect_csv(sample_csv, spec, "0001")

    assert manifest["row_count"] == 1