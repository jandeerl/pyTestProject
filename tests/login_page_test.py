import pytest
import selenium
import selenium.webdriver.common

from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.base_test import driver


def test_login_correct_password(driver):
    login_page = LoginPage(driver)
    login_page.openPage(login_page.loginPageUrl)
    login_page.login_user(
        "standard_user", "secret_sauce").check_if_logo_visible()
