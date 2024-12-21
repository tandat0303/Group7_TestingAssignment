from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from functions.login import login
    
def navigate_to_edit_profile(driver, email, password):
    """Login and navigate to the Edit Profile page."""
    login(driver, email, password)
    driver.find_element(By.LINK_TEXT, "Admin").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Edit Profile"))).click()

def update_profile(driver, email, password, full_name, update_email, phone):
    """Helper to update profile details."""
    navigate_to_edit_profile(driver, email, password)

    name = driver.find_element(By.NAME, "full_name")
    name.clear()
    name.send_keys(full_name)

    email_field = driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys(update_email)

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.clear()
    phone_field.send_keys(phone)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

def update_password(driver, email, password, new_password, re_password):
    """Helper to update the password."""
    navigate_to_edit_profile(driver, email, password)
    driver.find_element(By.LINK_TEXT, "Update Password").click()
    
    old_pass_field = driver.find_element(By.NAME, "password")
    old_pass_field.clear()
    old_pass_field.send_keys(new_password)

    new_pass_field = driver.find_element(By.NAME, "re_password")
    new_pass_field.clear()
    new_pass_field.send_keys(re_password)

    driver.find_element(By.NAME, "form3").click()
    time.sleep(2)