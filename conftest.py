import pytest
import allure
from utils.driver_setup import get_driver
from utils.excel_logger import log_bug
from pom.login_page import LoginPage
import json

def load_data():
    with open("test_data/login_data.json") as f:
        return json.load(f)

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    data = load_data()

    login = LoginPage(driver)
    login.open()
    login.login(
        data["valid"]["username"],
        data["valid"]["password"]
    )

    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")

        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except:
                pass

        log_bug(item.name, str(result.longrepr))