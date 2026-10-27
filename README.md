# QA Learning Project

A practical software testing project built with Python, pytest, Selenium WebDriver, Requests, and SQLite.

## Project Objectives

- Practice functional, positive, and negative testing.
- Automate browser tests using Selenium WebDriver.
- Validate REST API responses.
- Verify database records using SQL.
- Practice test case design and boundary value analysis.
- Document test plans, test results, and software defects.
- Practice regression testing and version control with Git.

## Technology Stack

- Python 3.12.9
- pytest
- Selenium WebDriver
- Requests
- SQLite
- Google Chrome
- Git

## Project Structure

| File | Description |
|---|---|
| `test_qa_demo.py` | Automated browser tests using Selenium |
| `qa_demo.html` | Local demo web page for browser testing |
| `test_api.py` | API testing scenarios using Requests |
| `test_database.py` | Database validation tests using SQLite |
| `delivery_calculator.py` | Order total and delivery fee calculation logic |
| `test_delivery_calculator.py` | Delivery calculation and boundary tests |
| `test_order_total1.py` | Parameterized order total tests |
| `order_total.py` | Earlier learning example |
| `test_cases_order_total.md` | Order total test case documentation |
| `TEST_PLAN.md` | Test plan for the demo application |
| `BUG_REPORT.md` | Example bug report and verification notes |
| `.gitignore` | Files and folders excluded from version control |

## Test Coverage

### 1. Unit and Functional Testing

- Order total calculation
- Delivery fee calculation
- Valid and invalid input handling
- Negative values
- Boundary value analysis around the free delivery threshold

### 2. UI Automation Testing

- Valid customer name submission
- Empty name validation
- Whitespace-only input
- Leading and trailing spaces
- Customer names exceeding 50 characters

### 3. API Testing

- Successful GET requests
- HTTP 404 response validation
- POST request response validation
- Response status code, content type, and JSON data validation

### 4. Database Testing

- Verifying stored order data
- Checking expected order amounts and statuses
- Confirming that nonexistent orders return no data

### 5. Regression Testing

The complete test suite can be executed after code changes to check whether previously tested behaviors continue to work as expected.

## Setup

### Prerequisites

- Python 3.12 or a compatible Python version
- Google Chrome
- Git
- A compatible ChromeDriver for browser automation

### Create a Virtual Environment

Open a terminal in the project directory and run:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install selenium pytest requests
```

## Browser Test Configuration

The Selenium tests use Google Chrome and a local HTML page.

A compatible `chromedriver.exe` must be available in the project root directory.

The browser driver is excluded from version control. Each environment must provide its own compatible driver.

## Running Tests

### Run the Complete Test Suite

```powershell
python -m pytest -v
```

### Run Browser Tests

```powershell
python -m pytest -v test_qa_demo.py
```

### Run API Tests

```powershell
python -m pytest -v test_api.py
```

### Run Database Tests

```powershell
python -m pytest -v test_database.py
```

### Run Delivery Calculator Tests

```powershell
python -m pytest -v test_delivery_calculator.py
```

## Test Documentation

The project includes a test plan and a sample bug report to demonstrate basic QA documentation practices.

The sample bug report covers a simulated input validation issue, its reproduction through automated testing, and verification after a fix.

## Limitations

- The demo web application is a local educational example.
- The API tests use a public testing service and require internet access.
- The database tests use an in-memory SQLite database.
- The browser tests require Google Chrome and a compatible ChromeDriver.
- The project does not represent or test the production systems of Snappfood.
- The current test suite is an introductory portfolio project, not a comprehensive production QA framework.

## Learning Outcomes

This project demonstrates practical exercises in:

- Python-based test automation
- Test case design
- Boundary value analysis
- Functional and negative testing
- Selenium WebDriver
- API testing
- SQL and database validation
- Bug reporting
- Regression testing
- Git version control