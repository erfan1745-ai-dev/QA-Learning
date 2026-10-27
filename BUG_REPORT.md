# Bug Report — BUG-001

## Title
The form accepts customer names longer than 50 characters

## Environment
- OS: Windows
- Browser: Google Chrome
- Application: QA Demo Store
- Test Tool: Selenium WebDriver

## Preconditions
The QA Demo Store page is open.

## Steps to Reproduce
1. Open the QA Demo Store page.
2. Enter a customer name containing 51 characters.
3. Click the Submit button.
4. Observe the displayed message.

## Expected Result
The form should reject names longer than 50 characters
and display a validation message.

## Actual Result
The form accepts the 51-character name and displays
a greeting message.

## Severity
Low — for this training scenario.

## Priority
Medium — assuming the requirement is confirmed.

## Status
Closed — Fix verified

## Notes
This is a simulated bug report for a local demo application.
The 50-character limit is an assumed training requirement.

## Verification

- Fix implemented: Yes
- Verification test: test_submit_name_over_50_characters_displays_validation_message
- Regression result: 5 Selenium tests passed
- Status: Closed — Fix verified