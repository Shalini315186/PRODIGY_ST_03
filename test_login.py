import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Logged In Successfully" in driver.page_source

def test_invalid_username(driver):
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Your username is invalid!" in driver.page_source

def test_invalid_password(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("WrongPass")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Your password is invalid!" in driver.page_source

def test_empty_fields(driver):
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Your username is invalid!" in driver.page_source

def test_only_username(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Your password is invalid!" in driver.page_source

def test_only_password(driver):
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Your username is invalid!" in driver.page_source
