from selenium.webdriver.common.by import By
from utils.url import LOGIN_URL

class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(LOGIN_URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_error(self):
        return self.driver.find_element(*self.ERROR_MSG).text
