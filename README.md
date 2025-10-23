# OpenAQ API Test Automation Framework

[![Run Smoke Tests](https://github.com/Vikas-Deswal/OpenAQ-BDD-Automation/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Vikas-Deswal/OpenAQ-BDD-Automation/actions/workflows/run-tests.yml)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A BDD (Behavior-Driven Development) test automation framework for OpenAQ API using Python and Behave.

## About This Project

A **production-ready BDD automation framework** for testing OpenAQ APIs. Tests real-world scenarios like pagination, rate limits, error handling, and data integrity using plain English test scenarios.

**Perfect for**: Learning API automation, BDD testing, and building SDET portfolios.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11 |
| BDD Framework | Behave |
| HTTP Client | Requests |
| Reporting | Allure |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Infrastructure | Vagrant (Ubuntu) |

## Project Structure

```
AQI/
├── features/              # Gherkin test scenarios
├── steps/                 # Step implementations
├── services/              # API business logic
├── utilities/             # Helpers & config
├── resources/             # Endpoints & constants
├── logs/                  # Test execution logs
└── requirements.txt       # Dependencies
```

## Test Coverage

- Country metadata & filtering
- Parameter information endpoints
- Pagination behavior (no overlaps)
- City pollutant measurements
- Rate limit validation
- Error handling (401, 404, 500)
- Performance benchmarks

## Prerequisites

- **Python** 3.8+
- **OpenAQ API Key** (free from [openaq.org](https://openaq.org))
- **pip** (Python package manager)
- **(Optional)** Vagrant + VMware/VirtualBox

## Quick Start

### Option A: Local Setup (Fastest)

```bash
# 1. Clone & setup
git clone <repository-url>
cd AQI
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
export OPENAQ_API_KEY="your_api_key_here"

# 4. Run tests
behave
```

### Option B: Using Docker (Containerized)

```bash
# Pull image from Docker Hub
docker pull vikasdeswal/openaq-bdd:latest

# Run tests
docker run -e OPENAQ_API_KEY="your_api_key_here" vikasdeswal/openaq-bdd:latest

# Run with report volume mount
docker run -e OPENAQ_API_KEY="your_api_key_here" \
  -v $(pwd)/allure-results:/app/allure-results \
  vikasdeswal/openaq-bdd:latest
```

### Option C: Using Vagrant (Isolated Environment)

```bash
# Start VM with all dependencies pre-installed
vagrant up
vagrant ssh

# Set API key and run tests
export OPENAQ_API_KEY="your_api_key_here"
cd /home/vagrant/openaq
behave
```

## Running Tests

```bash
# Run all tests
behave

# Run specific feature
behave features/country_metadata.feature

# Run by tag
behave --tags=@smoke          # Quick tests
behave --tags=@regression     # Full suite
behave --tags=@negative       # Error scenarios

# Generate Allure report
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

## Test Tags

| Tag | Purpose |
|-----|----------|
| `@smoke` | Quick validation tests |
| `@regression` | Full test suite |
| `@metadata` | Metadata validation |
| `@negative` | Error handling |
| `@integration` | End-to-end tests |

## Key Features

- BDD Approach - Plain English test scenarios
- CI/CD Ready - GitHub Actions integration
- Modular Design - Clean separation of concerns
- Reusable Components - DRY principle throughout
- Easy Configuration - Environment variables
- Allure Reports - Beautiful test dashboards
- Tag-based Execution - Run specific test suites


## Learning Outcomes

This project demonstrates:
- BDD test automation best practices
- Python API testing with Behave
- CI/CD pipeline setup with GitHub Actions
- Docker containerization & optimization
- Container registry management (Docker Hub)
- Infrastructure as Code (Vagrant)
- Professional logging & error handling
- Allure reporting integration

## Support & Questions

For issues or questions, please open a GitHub issue or check the documentation.

---

**Author:** Vikas Deswal  
**License:** MIT  
**Status:** Active & Maintained

*Built to demonstrate SDET-level automation skills in API testing, BDD frameworks, and Python.*