from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    mainPageUrl = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        super().__init__(driver)

    def check_if_logo_visible(self):
        main_logo: WebElement = super().find_element(*MainPageLocators.MAIN_LOGO)
        return main_logo.is_displayed
