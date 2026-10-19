from collections.abc import Iterable

REQUIRED_ORDER_COLUMNS = {
    "order_id",
    "customer_id",
    "order_status",
    "order_purchase_timestamp"
}

def validate_order_columns(columns: Iterable[str]) -> None:
    """ Verify that all required order columns exist."""
    missing = REQUIRED_ORDER_COLUMNS - set(columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )