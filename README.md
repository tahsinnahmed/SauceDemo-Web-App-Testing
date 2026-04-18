# SauceDemo Web App Automation Testing

## Overview

This project is built for software testing purpose.

It automates testing of the SauceDemo web application and includes:
- Functional UI automation testing
- Pytest execution framework
- Allure reporting
- Excel-based defect tracking using openpyxl

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Allure Reports
- openpyxl (Excel logging)

## Project Structure

```text
saucedemo-testing/
│
├── tests/                  # Test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── pom/                    # Page Object Model (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── utils/                  # Utility modules
│   ├── driver_setup.py
│   ├── excel_logger.py
│   └── url.py
│
├── test_data/              # Test data (JSON files)
│   └── login_data.json
│
├── reports/                # Allure raw results
├── requirements.txt
└── pytest.ini              # Run test automatically

```


## Screenshots

- Defect Tracking (Excel)

<img width="1109" height="359" alt="Defect Tracking (Excel)" src="https://github.com/user-attachments/assets/ede210b8-19a7-45b6-aa99-a03eba1de8a5" />

- Report Generation (Allure Report)

<img width="913" height="780" alt="Report (Allure Report)" src="https://github.com/user-attachments/assets/f0900354-cc7c-45ce-a1a4-2a066f2422dd" />

