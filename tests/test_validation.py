import pytest

from retail_pipeline.validation import validate_order_columns


def test_valid_order_columns():
    columns = [
        "order_id",
        "customer_id",
        "order_status",
        "order_purchase_timestamp"
    ]

    validate_order_columns(columns)

def test_missing_order_column():
    columns = [
        "order_id",
        "order_status",
        "order_purchase_timestamp",
    ]

    with pytest.raises(ValueError, match="customer_id"):
        validate_order_columns(columns)

def test_unexpected_column():
    columns = [
        "order_id",
        "customer_id",
        "order_status",
        "order_purchase_timestamp",
        "unexpected_column"
    ]
    
    with pytest.raises(ValueError, match="Unexpected column provided"):
        validate_order_columns(columns, False)