from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"

DATASETS = {
    "orders": {
        "file": "olist_orders_dataset.csv",
        "key": ["order_id"],
        "relationships": [("customer_id", "customers", "customer_id")],
    },
    "order_items": {
        "file": "olist_order_items_dataset.csv",
        "key": ["order_id", "order_item_id"],
        "relationships": [
            ("order_id", "orders", "order_id"),
            ("product_id", "products", "product_id"),
            ("seller_id", "sellers", "seller_id"),
        ],
    },
    "payments": {
        "file": "olist_order_payments_dataset.csv",
        "key": ["order_id", "payment_sequential"],
        "relationships": [("order_id", "orders", "order_id")],
    },
    "customers": {
        "file": "olist_customers_dataset.csv",
        "key": ["customer_id"],
        "fkey": [],
        "parents": [],
    },
    "products": {
        "file": "olist_products_dataset.csv",
        "key": ["product_id"],
        "fkey": [],
        "parents": [],
    },
    "sellers": {
        "file": "olist_sellers_dataset.csv",
        "key": ["seller_id"],
        "fkey": [],
        "parents": [],
    },
}


def profile_dataset(
    name: str,
    config: dict,
) -> None:
    file_path = DATA_DIR / config["file"]

    # Preserve ZIP-code prefixes as strings.
    dtype_options = {}
    if name == "customers":
        dtype_options = {
            "customer_zip_code_prefix": "string"
        }
    elif name == "sellers":
        dtype_options = {
            "seller_zip_code_prefix": "string"
        }

    df = pd.read_csv(
        file_path,
        dtype=dtype_options,
        low_memory=False,
    )

    key_columns = config["key"]

    print(f"\n{'=' * 50}")
    print(f"DATASET: {name.upper()}")
    print(f"{'=' * 50}")

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nCOLUMN DATA TYPES")
    print(df.dtypes)

    print("\nNULL COUNTS")
    print(df.isnull().sum())

    print("\nNULL PERCENTAGES")
    print(
        (df.isnull().mean() * 100).round(2)
    )

    print("\nDUPLICATE ROWS")
    print(df.duplicated().sum())

    print("\nDUPLICATE KEYS")
    print(
        df.duplicated(subset=key_columns).sum()
    )

    print("\nNULL KEYS")
    print(df[key_columns].isna().any(axis=1).sum())

def profile_relationships() -> None:
    print(f"\n{'=' * 50}")
    print("RELATIONSHIPS BETWEEN DATASETS")
    print(f"{'=' * 50}")

    datasets = {
        name: pd.read_csv(DATA_DIR / config["file"], low_memory=False)
        for name, config in DATASETS.items()
    }

    for name, config in DATASETS.items():
        df = datasets[name]
        for child_column, parent_name, parent_column in config.get("relationships", []):
            parent_df = datasets[parent_name]
            parent_keys = parent_df[parent_column].dropna()
            orphan_mask = (
                df[child_column].notna()
                & ~df[child_column].isin(parent_keys)
            )
            orphan_keys = df.loc[orphan_mask, child_column].drop_duplicates()

            print(f"\n{name.upper()}.{child_column} -> {parent_name.upper()}.{parent_column}")
            print(f"Rows with missing foreign keys: {int(orphan_mask.sum())}")
            print(f"Distinct missing foreign keys: {len(orphan_keys)}")



def main():
    for name, config in DATASETS.items():
        profile_dataset(name, config)
    profile_relationships()

if __name__ == "__main__":
    main()