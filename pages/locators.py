from selenium.webdriver.common.by import By


class MainPageLocators(object):
    MENU_BUTTON = (By.ID, "menu")
    MAIN_LOGO = (By.CLASS_NAME, "app_logo")


class LoginPageLocators(object):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    TITLE_TEXT = (By.CLASS_NAME, "login_logo")
