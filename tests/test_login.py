import json
from pom.login_page import LoginPage
from utils.url import INVENTORY_URL

def load_data():
    with open("test_data/login_data.json") as f:
        return json.load(f)

def test_valid_login(driver):
    data = load_data()
    test_login = LoginPage(driver)

    test_login.open()
    test_login.login(
        data["valid"]["username"],
        data["valid"]["password"]
    )

    assert driver.current_url == INVENTORY_URL

def test_invalid_login(driver):
    data = load_data()
    test_login = LoginPage(driver)

    test_login.open()
    test_login.login(
        data["invalid"]["username"],
        data["invalid"]["password"]
    )

    assert "Epic sadface: Username and password do not match any user in this service" in test_login.get_error()