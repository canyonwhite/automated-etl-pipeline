# S3 Ingestion Design

## 1. Overview
Purpose of automated S3 ingestion.

## 2. Architecture
How Python, Boto3, S3, and manifests interact.

## 3. AWS Authentication
Credential provider configuration and IAM permissions.

## 4. Object Storage Structure
Raw data prefixes and manifest locations.

## 5. Upload Workflow
File validation, checksum verification, and upload steps.

## 6. Idempotency
Conditional writes and existing-object verification.

## 7. Failure Recovery
Behavior when only some objects were uploaded.

## 8. Testing
Unit tests and manual integration testing.

## 9. Security Considerations
Least privilege, encryption, and credential protection.

## 10. Known Limitations
File size restrictions, non-atomic multi-object uploads,
and lack of persistent warehouse ingestion status.