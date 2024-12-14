from selenium.webdriver.common.by import By
import time

def login(driver, email, password):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    email = driver.find_element(By.NAME, "cust_email").send_keys(email)
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(password)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()