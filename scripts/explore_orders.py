from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

file_path = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "olist_orders_dataset.csv"
)

df = pd.read_csv(file_path)

print("FIRST FIVE ROWS")
print(df.head())

print("\nDATAFRAME INFORMATION")
df.info()

print("\nSHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nMISSING PERCENTAGE")
print(
    (df.isnull().mean() * 100).round(2)
)

print("\n")
print(
    pd.crosstab(
        df["order_status"],
        df["order_delivered_customer_date"].isna()
    )
)

print("\nEXACT DUPLICATE ROWS")
print(df.duplicated().sum())

print("\nDUPLICATE ORDER IDs")
print(df.duplicated(subset=["order_id"]).sum())

print("\nORDER STATUS DISTRIBUTION")
print(
    df["order_status"].value_counts(
        dropna=False
    )
)