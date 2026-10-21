# Retail Data Platform — Cloud Architecture

## Overview
Describe the purpose of the cloud environment.

## AWS Configuration
- AWS Region: us-east-2
- S3 Bucket: retail-data-platform-cbw
- Raw Data Prefix: 
- IAM Role: retail-snowflake-s3-read-role
- Permissions Summary: 

## Snowflake Configuration
- Snowflake Cloud/Region: AWS_US_EAST_2
- Database: RETAIL_DB
- Schemas: RAW, BRONZE, SILVER, GOLD
- Warehouse: RETAIL_DEV_WH
- Storage Integration: RETAIL_S3_INT
- External Stage: RETAIL_DB.RAW.OLIST_ORDERS_STAGE

## Data Ingestion
Describe how Olist orders move from S3 into Snowflake.

## Security Decisions
Explain our use of IAM roles, least privilege,
and Snowflake storage integrations.

## Cost Controls
Document AWS billing safeguards and Snowflake
warehouse and resource-monitor settings.

## Validation Results
- Source row count: 99441
- Loaded row count: 99441
- Unique order count: 99441
- Null order IDs: 0
- COPY INTO result: LOADED
- Second COPY INTO result: *Copy executed with 0 files processed.*

## Known Limitations
Document limitations of the initial loading
and idempotency approach.