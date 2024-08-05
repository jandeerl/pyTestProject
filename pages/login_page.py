import selenium
import selenium.webdriver.common
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.main_page import MainPage


class LoginPage(BasePage):

    loginPageUrl = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, username):
        username_input: WebElement = super().find_element(
            *LoginPageLocators.USERNAME_INPUT)
        username_input.send_keys(username)
        return self

    def input_password(self, password):
        password_input: WebElement = super().find_element(
            *LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        return self

    def click_login_button(self):
        login_button: WebElement = super().find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        return self

    def login_user(self, username, password):
        self.input_username(username).input_password(
            password).click_login_button()
        return MainPage(self.driver)

    def check_username_input(self):
        username_input = super().find_element(
            *LoginPageLocators.USERNAME_INPUT).get_attribute("value")
        return username_input
