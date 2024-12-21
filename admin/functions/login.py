import time
from selenium.webdriver.common.by import By

def login(driver, email, password):
    driver.get("http://localhost/eCommerceSite-PHP/admin/login.php")
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "form1").click()