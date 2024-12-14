from selenium.webdriver.common.by import By
import time

def update_password(driver, password, re_password):
    driver.find_element(By.XPATH, "//button[text()='Update Password']").click()
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(password)
    time.sleep(2)

    driver.find_element(By.NAME, "cust_re_password").send_keys(re_password)
    time.sleep(2)

    # Click "Update"
    driver.find_element(By.NAME, "form1").click()