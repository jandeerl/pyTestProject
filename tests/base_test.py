import pytest
import selenium.webdriver.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    driver = webdriver.Firefox()

    yield driver

    driver.close()
