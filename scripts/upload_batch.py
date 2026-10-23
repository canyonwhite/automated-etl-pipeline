import argparse
import os
from pathlib import Path

import boto3

from retail_pipeline.ingestion import (
    DATASETS,
    inspect_csv,
    save_manifest,
)
from retail_pipeline.storage import upload_batch


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare and upload an Olist batch to S3"
    )

    parser.add_argument(
        "--dataset",
        required=True,
        choices=DATASETS.keys(),
    )

    parser.add_argument(
        "--file",
        required=True,
        type=Path,
    )

    parser.add_argument(
        "--batch-id",
        required=True,
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

    # Step 1: Inspect the source.
    manifest = inspect_csv(
        args.file,
        DATASETS[args.dataset],
        args.batch_id,
    )

    # Step 2: Prepare the local manifest.
    manifest_path = (
        Path("data/manifests")
        / args.dataset
        / f"batch_id={args.batch_id}.json"
    )

    save_manifest(manifest, manifest_path)

    # Step 3: Establish the AWS session.
    session = boto3.Session(
        profile_name=args.profile
    )

    s3_client = session.client(
        "s3",
        region_name=os.environ.get("AWS_REGION"),
    )

    # Step 4: Upload source and stored manifest.
    result = upload_batch(
        s3_client,
        args.bucket,
        args.file,
        manifest_path,
    )

    print(f"Raw object: {result['raw_key']}")
    print(f"Raw status: {result['raw_status']}")

    print(f"Manifest object: {result['manifest_key']}")
    print(f"Manifest status: {result['manifest_status']}")


if __name__ == "__main__":
    main()