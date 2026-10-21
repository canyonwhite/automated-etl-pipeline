
# Development Environment Setup

## 1. Overview

### 1.1 Purpose
- Explain the purpose of the development environment.
- Describe how it supports the Automated ELT Pipeline.
- Define the scope of this documentation.

### 1.2 Technology Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| Python | Data ingestion and validation | 3.12.15 |
| AWS S3 | Cloud-based data storage | N/A |
| AWS IAM | Access management | N/A |
| Snowflake | Data warehouse | N/A |
| SQLMesh | SQL transformations and model management | 0.236.3 |
| Git / GitHub | Version control | 2.54.0 |
| pytest | Automated Python testing | 9.1.1 |

---

## 2. Prerequisites

### 2.1 Required Software
- Python installation
- Git installation
- Code editor / IDE
- Required Python packages
- SQLMesh CLI

### 2.2 Required Cloud Resources
- AWS account with appropriate IAM permissions
- S3 bucket for source data
- Snowflake account and development environment
- Snowflake storage integration

### 2.3 Required Access and Permissions
- AWS IAM permissions
- Snowflake roles and privileges
- GitHub repository access

---

## 3. Local Environment Configuration

### 3.1 Repository Setup
- Clone the GitHub repository.
- Navigate to the project root.
- Describe the repository structure.

### 3.2 Python Virtual Environment
- Create a virtual environment.
- Activate the environment.
- Install project dependencies.
- Verify successful installation.

### 3.3 Environment Variables
- Describe required environment variables.
- Explain how configuration is loaded.
- Document the use of `.env` files.
- Explain which files must be excluded from Git.

### 3.4 Project Dependencies
- Describe the dependency management approach.
- Explain how dependencies are updated.
- Document how to reproduce the environment.

---

## 4. AWS Development Configuration

### 4.1 S3 Bucket Configuration
- Describe the purpose of the S3 bucket.
- Document the expected folder structure.
- Explain how source data is organized.

### 4.2 IAM Configuration
- Document the IAM roles and policies required.
- Explain how least-privilege access is enforced.
- Describe the trust relationship used by Snowflake.

### 4.3 AWS Access Verification
- Explain how to verify AWS access.
- Describe how to confirm S3 permissions.
- Document expected successful results.

---

## 5. Snowflake Development Configuration

### 5.1 Snowflake Environment
- Describe the development database.
- Document schemas and warehouse configuration.
- Identify the Snowflake role used for development.

### 5.2 Authentication
- Explain the configured authentication method.
- Document RSA key-pair authentication, if applicable.
- Describe secure key storage.

### 5.3 Snowflake Storage Integration
- Describe the AWS S3 storage integration.
- Explain the IAM role trust configuration.
- Document integration verification steps.

### 5.4 External Stages
- Explain how Snowflake references S3 data.
- Document external stage configuration.
- Verify access to source files.

---

## 6. SQLMesh Configuration

### 6.1 SQLMesh Installation
- Explain how SQLMesh is installed.
- Document required adapters and dependencies.
- Verify the installed version.

### 6.2 Project Initialization
- Describe the SQLMesh project structure.
- Explain the purpose of configuration files.
- Identify the directory where CLI commands run.

### 6.3 Snowflake Connection
- Document SQLMesh gateway configuration.
- Explain how authentication is configured.
- Describe connection verification.

### 6.4 External Models
- Explain how external source tables are represented.
- Describe external model generation.
- Document how models are validated.

---

## 7. Development Workflow

### 7.1 Standard Workflow
- Activate the Python virtual environment.
- Verify cloud connectivity.
- Make changes to pipeline code or SQL models.
- Run applicable validation commands.
- Commit and push changes to GitHub.

### 7.2 Testing
- Explain how to run Python unit tests.
- Document SQLMesh validation commands.
- Explain how failed tests should be investigated.

### 7.3 Version Control
- Describe the branching strategy.
- Explain commit message conventions.
- Document files excluded by `.gitignore`.

---

## 8. Security and Credential Management

### 8.1 Sensitive Files
- Identify sensitive configuration files.
- Explain how credentials are kept out of Git.
- Document `.gitignore` requirements.

### 8.2 Access Control
- Describe AWS and Snowflake permission boundaries.
- Explain how development privileges are restricted.

### 8.3 Credential Rotation
- Describe the process for replacing credentials.
- Explain how compromised credentials are handled.

---

## 9. Troubleshooting

### 9.1 AWS Permission Errors
- Access denied errors
- IAM trust policy issues
- Snowflake AssumeRole failures

### 9.2 Snowflake Authentication Errors
- Invalid Snowflake username
- SAML identity provider errors
- RSA key-pair configuration issues

### 9.3 SQLMesh Errors
- No models found
- Incorrect working directory
- Snowflake connection failures
- External model generation errors

### 9.4 Python Environment Errors
- Missing dependencies
- Incorrect interpreter
- Virtual environment issues

---

## 10. Environment Verification Checklist

- [ ] Repository cloned successfully
- [ ] Python virtual environment created
- [ ] All required dependencies installed
- [ ] AWS S3 access verified
- [ ] Snowflake authentication verified
- [ ] Snowflake storage integration working
- [ ] External stages accessible
- [ ] SQLMesh project initialized
- [ ] SQLMesh successfully connects to Snowflake
- [ ] External models generated or configured
- [ ] Python tests passing
- [ ] Sensitive files excluded from Git

---

## 11. References

- Python documentation
- AWS IAM documentation
- AWS S3 documentation
- Snowflake documentation
- SQLMesh documentation
- Project architecture documentation
