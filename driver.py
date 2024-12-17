import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    chrome_options = Options()
    service = Service('C:/xampp/htdocs/eCommerceSite-PHP/drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
