import argparse
from pathlib import Path

from retail_pipeline.ingestion import (
    DATASETS,
    inspect_csv,
    save_manifest,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate and prepare an Olist ingestion batch"
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

    args = parser.parse_args()

    manifest = inspect_csv(
        file_path=args.file,
        spec=DATASETS[args.dataset],
        batch_id=args.batch_id,
    )

    destination = (
        Path("data/manifests")
        / args.dataset
        / f"batch_id={args.batch_id}.json"
    )

    created = save_manifest(
        manifest,
        destination,
    )

    if created:
        print(f"Created manifest: {destination}")
    else:
        print(f"Batch already prepared: {destination}")

    print(f"Records: {manifest['row_count']}")
    print(f"Checksum: {manifest['sha256']}")


if __name__ == "__main__":
    main()