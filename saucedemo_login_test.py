import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory" in driver.current_url

def test_invalid_username(driver):
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_msg = driver.find_element(By.XPATH, "//h3").text
    assert "Username and password do not match" in error_msg

def test_invalid_password(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_msg = driver.find_element(By.XPATH, "//h3").text
    assert "Username and password do not match" in error_msg

def test_empty_fields(driver):
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_msg = driver.find_element(By.XPATH, "//h3").text
    assert "Username is required" in error_msg

def test_only_username(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_msg = driver.find_element(By.XPATH, "//h3").text
    assert "Password is required" in error_msg

def test_only_password(driver):
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_msg = driver.find_element(By.XPATH, "//h3").text
    assert "Username is required" in error_msg
