from driver import *


# Helper Functions
def navigate_to_login(driver):
    """Navigate to the login page."""
    driver.get('http://localhost/Phpcode/eCommerceSite-PHP/admin')
    time.sleep(2)

def perform_login(driver, email, password):
    """Perform login with given email and password."""
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

def verify_text_in_page(driver, text):
    """Assert that the specified text is in the page source."""
    assert text in driver.page_source

# Test Cases

def test_user_login(driver):
    navigate_to_login(driver)
    perform_login(driver, "admin@mail.com", "Password@123")
    verify_text_in_page(driver, "Dashboard")

def test_user_invalid_login_pass(driver):
    navigate_to_login(driver)
    perform_login(driver, "admin@mail.com", "Password#123")
    verify_text_in_page(driver, "Password does not match")

def test_user_invalid_login_email(driver):
    navigate_to_login(driver)
    perform_login(driver, "invalid@mail.com", "Password@123")
    verify_text_in_page(driver, "Email Address does not match")

def test_user_empty_login(driver):
    navigate_to_login(driver)
    perform_login(driver, "", "")
    verify_text_in_page(driver, "Email and/or Password can not be empty")

def test_user_logout(driver):
    test_user_login(driver) 
    driver.find_element(By.LINK_TEXT, "Administrator").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(2)
    verify_text_in_page(driver, "Log in to start your session")
