from driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Helper functions
def perform_login(driver, email, password):
    """Perform login with given email and password."""
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "form1").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Administrator")))

def navigate_to_edit_profile(driver):
    """Login and navigate to the Edit Profile page."""
    perform_login(driver, "admin@mail.com", "Password@123")
    driver.find_element(By.LINK_TEXT, "Administrator").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Edit Profile"))).click()

def update_profile(driver, full_name, email, phone):
    """Helper to update profile details."""
    name = driver.find_element(By.NAME, "full_name")
    name.clear()
    name.send_keys(full_name)

    email_field = driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys(email)

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.clear()
    phone_field.send_keys(phone)

    driver.find_element(By.NAME, "form1").click()

def update_password(driver, old_password, new_password):
    """Helper to update the password."""
    old_pass_field = driver.find_element(By.NAME, "password")
    old_pass_field.clear()
    old_pass_field.send_keys(old_password)

    new_pass_field = driver.find_element(By.NAME, "re_password")
    new_pass_field.clear()
    new_pass_field.send_keys(new_password)

    driver.find_element(By.NAME, "form3").click()

# Test cases
def test_update_information(driver):
    """Test successful profile update."""
    navigate_to_edit_profile(driver)
    update_profile(driver, "Admin", "admin@mail.com", "0397387337")
    assert "Profile updated successfully" in driver.page_source

def test_invalid_email_format(driver):
    """Test profile update with invalid email."""
    navigate_to_edit_profile(driver)
    update_profile(driver, "Admin", "admin@mail", "0397387337")
    assert "Email address must be valid." in driver.page_source

def test_empty_fields(driver):
    """Test profile update with empty fields."""
    navigate_to_edit_profile(driver)
    update_profile(driver, "", "", "")
    assert "Name can not be empty." in driver.page_source
    assert "Email Address can not be empty" in driver.page_source

def test_invalid_phone(driver):
    """Test profile update with invalid phone number."""
    navigate_to_edit_profile(driver)
    update_profile(driver, "Admin", "admin@mail.com", "invalid_phone")
    assert "Phone number must be valid." in driver.page_source

def test_duplicate_email(driver):
    """Test profile update with a duplicate email."""
    navigate_to_edit_profile(driver)
    update_profile(driver, "Admin", "existing_user@mail.com", "0397387337")
    assert "Email already exists." in driver.page_source

def test_update_password_success(driver):
    """Test successful password update."""
    navigate_to_edit_profile(driver)
    update_password(driver, "Password@123", "NewPassword@123")
    assert "Password updated successfully" in driver.page_source

def test_update_password_mismatch(driver):
    """Test password update with mismatched confirmation."""
    navigate_to_edit_profile(driver)
    update_password(driver, "Password@123", "WrongPassword")
    assert "Password confirmation does not match." in driver.page_source

def test_update_password_wrong_old(driver):
    """Test password update with wrong old password."""
    navigate_to_edit_profile(driver)
    update_password(driver, "WrongPassword@123", "NewPassword@123")
    assert "Old password is incorrect." in driver.page_source

def test_update_password_weak(driver):
    """Test password update with weak password."""
    navigate_to_edit_profile(driver)
    update_password(driver, "Password@123", "123")
    assert "Password is too weak." in driver.page_source