from selenium.webdriver.common.by import By

class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")
    FINISH = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(*self.FIRST_NAME).send_keys("Ash")
        self.driver.find_element(*self.LAST_NAME).send_keys("William")
        self.driver.find_element(*self.ZIP).send_keys("1234")
        self.driver.find_element(*self.CONTINUE).click()
        self.driver.find_element(*self.FINISH).click()

    def success_message(self):
        return self.driver.find_element(*self.SUCCESS_MSG).text
