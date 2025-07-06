# PRODIGY_ST_03 – Automated Login Test for a Web Application
Automated login test suite for saucedemo.com using Pytest and Selenium as part of Task-03 for Prodigy Infotech's Software Testing Internship. Includes both positive and negative test cases for validating login functionality across common user scenarios.



🎯 **Internship Task**: Task-03 – Prodigy Infotech  
🔬 **Track**: Software Testing  
🌐 **Tested Site**: [https://www.saucedemo.com](https://www.saucedemo.com)

---

## 📌 Project Overview

This repository includes an automated test suite designed to validate the login functionality of the **SauceDemo** e-commerce web application using `Selenium` and `Pytest`. The goal of this task is to simulate real-world login scenarios, catch potential edge cases, and ensure that the application behaves as expected under both valid and invalid user inputs.

This task is a part of the **Software Testing Internship** offered by **Prodigy Infotech**.

---

## 🧪 Technologies Used

- **Programming Language**: Python 🐍
- **Automation Framework**: Pytest
- **Browser Automation**: Selenium WebDriver
- **Test Environment**: Google Chrome
- **Tool Used for Testing**: [SauceDemo](https://www.saucedemo.com)

---

## ✅ Test Scenarios Covered

### Positive Test Case
- Login with **valid credentials**:
  - `Username`: `standard_user`
  - `Password`: `secret_sauce`

### Negative Test Cases
- Invalid username with correct password
- Valid username with incorrect password
- Both username and password fields left empty
- Username entered, password empty
- Password entered, username empty

Each test checks for the appropriate error message or page redirection to ensure the login system is handling inputs securely and predictably.

---

## 📁 Files Included

- `saucedemo_login_test.py` – Pytest-based Selenium test suite with fixtures and assertions
- `README.md` – Documentation and setup instructions

---

## 🚀 How to Run the Tests

### 🔧 Prerequisites
- Python 3.x installed
- Google Chrome installed
- ChromeDriver compatible with your browser version
- Install Python packages:
```bash
pip install selenium pytest

