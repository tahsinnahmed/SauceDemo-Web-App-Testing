from selenium.webdriver.common.by import By

class CartPage:
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def proceed_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()