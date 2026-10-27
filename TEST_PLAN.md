# QA Demo Store - Test Plan

## 1. Objective
Validate the behavior of the QA Demo Store form.

## 2. Scope of Testing
- Submitting a valid customer name
- Submitting an empty name
- Submitting spaces only
- Submitting a name with leading and trailing spaces

## 3. Test Types
- Functional Testing
- Positive Testing
- Negative Testing
- UI Automation Testing
- Regression Testing

## 4. Test Environment
- Operating System: Windows
- Programming Language: Python 3.12.9
- Test Framework: pytest
- Browser Automation: Selenium WebDriver
- Browser: Google Chrome

## 5. Test Approach
- Execute manual test scenarios where needed.
- Automate repeatable browser scenarios using Selenium.
- Compare actual results with expected results.
- Run the test suite after changes to check for regressions.

## 6. Entry Criteria
- The demo page is available.
- Python and required test libraries are installed.
- ChromeDriver is available.

## 7. Exit Criteria
- All planned test cases have been executed.
- Test results have been recorded.
- Any failed tests have been investigated.

## 8. Known Limitations
- The application is a local demo page.
- The test suite does not represent the full Snappfood production system.