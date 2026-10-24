import argparse
import json
from pathlib import Path

import boto3

from retail_pipeline.warehouse import (
    create_snowflake_connection,
    load_orders_batch,
)


def main():
    parser = argparse.ArgumentParser(
        description="Load an Olist orders batch into Snowflake"
    )

    parser.add_argument(
        "--manifest",
        required=True,
        type=Path,
    )

    parser.add_argument(
        "--bucket",
        required=True,
    )

    parser.add_argument(
        "--profile",
        default=None,
    )

    args = parser.parse_args()

    manifest = json.loads(
        args.manifest.read_text(encoding="utf-8")
    )

    session = boto3.Session(
        profile_name=args.profile
    )

    s3_client = session.client("s3")

    connection = create_snowflake_connection()

    try:
        result = load_orders_batch(
            connection,
            s3_client,
            args.bucket,
            manifest,
        )

        print(f"Status: {result['status']}")
        print(f"Source rows: {result['source_rows']}")
        print(f"Inserted rows: {result['inserted_rows']}")

    finally:
        connection.close()


if __name__ == "__main__":
    main()