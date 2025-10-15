# OpenAQ API Test Automation Framework

A BDD (Behavior-Driven Development) test automation framework for OpenAQ API using Python and Behave.

> **Status:** Work in Progress - 3 more features to be added + CI/CD integration with GitHub Actions

## About This Project

This framework tests the OpenAQ API (Air Quality data) using BDD approach. It validates API endpoints, data integrity, pagination, and filtering capabilities.

## Tech Stack

- **Language:** Python 3.x
- **BDD Framework:** Behave
- **HTTP Client:** Requests
- **Reporting:** Allure
- **API:** OpenAQ v3
- **VM Setup:** Vagrant (Ubuntu)

## Project Structure

```
AQI/
├── features/              # BDD feature files (test scenarios)
├── steps/                 # Step definitions (test implementation)
├── services/              # Business logic layer
├── utilities/             # Helper functions and configurations
├── resources/             # API endpoints and constants
├── logs/                  # Test execution logs
└── requirements.txt       # Python dependencies
```

## Features Covered

1. **Country Metadata** - Validate country details and filtering
2. **Parameters Metadata** - Test parameter information endpoints
3. **Pagination Behavior** - Verify pagination across endpoints
4. **City Pollutant Measurements** - Test measurement data retrieval

## Prerequisites

- Python 3.8 or higher
- OpenAQ API Key (free from [OpenAQ](https://openaq.org))
- pip (Python package manager)
- **(Optional)** Vagrant + VMware/VirtualBox for VM-based setup

## Setup Instructions

### Option A: Using Vagrant (Recommended for Isolated Environment)

Run tests in an Ubuntu VM without affecting your local machine:

```bash
# Start the VM (automatically installs all dependencies)
vagrant up

# SSH into the VM
vagrant ssh

# Set your API key
export OPENAQ_API_KEY="your_api_key_here"
source ~/.bashrc

# Navigate to project and run tests
cd /home/vagrant/openaq
behave

# Generate Allure report
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure generate allure-results -o allure-report --clean
```

**Benefits:**
- Clean Ubuntu environment
- All dependencies pre-installed (Python, Allure, Java)
- No conflicts with your local setup
- Easy to destroy and recreate

### Option B: Local Setup (Direct Installation)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AQI
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Set your OpenAQ API key:

```bash
export OPENAQ_API_KEY="your_api_key_here"
export OPENAQ_BASE_URL="https://api.openaq.org/v3"
```

Or add to your `~/.bashrc` or `~/.zshrc` for permanent setup:

```bash
echo 'export OPENAQ_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

## Running Tests

### Run All Tests

```bash
behave
```

### Run Specific Feature

```bash
behave features/country_metadata.feature
```

### Run Tests by Tag

```bash
behave --tags=@smoke
behave --tags=@regression
behave --tags=@metadata
```

### Run with Allure Reporting

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

## Test Tags

- `@smoke` - Quick smoke tests
- `@regression` - Full regression suite
- `@metadata` - Metadata validation tests
- `@integration` - Integration tests

## Key Features

✅ **BDD Approach** - Easy to read test scenarios in plain English  
✅ **Modular Design** - Separate layers for services, utilities, and steps  
✅ **Reusable Components** - Common functions for API calls and validations  
✅ **Environment Configuration** - Easy setup using environment variables  
✅ **Allure Reporting** - Detailed test reports with charts and graphs  
✅ **Tag-based Execution** - Run specific test suites using tags

## What's Coming Next

- [ ] 3 additional feature scenarios
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Enhanced error handling and logging
- [ ] Performance testing capabilities

## Project Highlights

- Clean and maintainable code structure
- Follows BDD best practices
- Easy to extend with new test scenarios
- Production-ready framework design
- Comprehensive API coverage

## Author

**Vikas Deswal**

---

*This framework demonstrates test automation skills for QA/SDET roles in API testing, BDD frameworks, and Python automation.*
