from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():
    driver_path = Path(__file__).with_name("chromedriver.exe")
    return webdriver.Chrome(
        service=Service(executable_path=str(driver_path))
    )


def test_submit_name_displays_greeting():
    driver = create_driver()

    try:
        page_path = Path(__file__).with_name("qa_demo.html").resolve().as_uri()
        driver.get(page_path)

        driver.find_element(By.ID, "customer-name").send_keys("Erfan")
        driver.find_element(By.ID, "submit-btn").click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"),
                "Hello, Erfan!"
            )
        )

        assert driver.find_element(By.ID, "message").text == "Hello, Erfan!"

    finally:
        driver.quit()


def test_submit_empty_name_displays_validation_message():
    driver = create_driver()

    try:
        page_path = Path(__file__).with_name("qa_demo.html").resolve().as_uri()
        driver.get(page_path)

        driver.find_element(By.ID, "submit-btn").click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"),
                "Please enter your name."
            )
        )

        assert (
            driver.find_element(By.ID, "message").text
            == "Please enter your name."
        )

    finally:
        driver.quit()

def test_submit_spaces_only_displays_validation_message():
    driver = create_driver()

    try:
        page_path = Path(__file__).with_name("qa_demo.html").resolve().as_uri()
        driver.get(page_path)

        driver.find_element(By.ID, "customer-name").send_keys("   ")
        driver.find_element(By.ID, "submit-btn").click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"),
                "Please enter your name."
            )
        )

        assert (
            driver.find_element(By.ID, "message").text
            == "Please enter your name."
        )

    finally:
        driver.quit()

def test_submit_name_with_extra_spaces():
    driver = create_driver()

    try:
        page_path = Path(__file__).with_name("qa_demo.html").resolve().as_uri()
        driver.get(page_path)

        driver.find_element(By.ID, "customer-name").send_keys("  Erfan  ")
        driver.find_element(By.ID, "submit-btn").click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"),
                "Hello, Erfan!"
            )
        )

        assert driver.find_element(By.ID, "message").text == "Hello, Erfan!"

    finally:
        driver.quit()

#تست های انجام شده 
#ورود نام معتبر
# ارسال فرم خالی
#وارد کردن فقط فاصله
#وارد کردن نام با فاصله‌های اضافی


def test_submit_name_over_50_characters_displays_validation_message():
    driver = create_driver()

    try:
        page_path = Path(__file__).with_name("qa_demo.html").resolve().as_uri()
        driver.get(page_path)

        long_name = "A" * 51
        driver.find_element(By.ID, "customer-name").send_keys(long_name)
        driver.find_element(By.ID, "submit-btn").click()

        expected_message = "Name must be 50 characters or fewer."

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"),
                expected_message
            )
        )

        assert driver.find_element(By.ID, "message").text == expected_message

    finally:
        driver.quit()