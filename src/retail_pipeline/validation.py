from collections.abc import Iterable

REQUIRED_ORDER_COLUMNS = {
    "order_id",
    "customer_id",
    "order_status",
    "order_purchase_timestamp"
}


def validate_order_columns(columns: Iterable[str], allow_extra: bool = True) -> None:
    """ Verify that all required order columns exist."""
    missing = REQUIRED_ORDER_COLUMNS - set(columns)
    extra_col = set(columns) - REQUIRED_ORDER_COLUMNS

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )
    if not allow_extra and extra_col:
        raise ValueError(
            f"Unexpected column provided: {sorted(extra_col)}"
        )