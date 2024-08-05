from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def openPage(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)
