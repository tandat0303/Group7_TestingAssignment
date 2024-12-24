from driver import *
from functions.login import login

# Helper Functions
def verify_text_in_page(driver, text):
    """Assert that the specified text is in the page source."""
    assert text in driver.page_source

# Test Cases
@pytest.mark.parametrize("email, password", [("admin@mail.com", "Password@123")])
def test_admin_login(driver, email, password):
    login(driver, email, password)
    verify_text_in_page(driver, "Dashboard")


@pytest.mark.parametrize("email, password", [("admin@mail.com", "Password#123")])
def test_admin_invalid_login_pass(driver, email, password):
    login(driver, email, password)
    verify_text_in_page(driver, "Password does not match")


@pytest.mark.parametrize("email, password", [("invalid@mail.com", "Password@123")])
def test_admin_invalid_login_email(driver, email, password):
    login(driver, email, password)
    verify_text_in_page(driver, "Email Address does not match")


@pytest.mark.parametrize("email, password", [("", "")])
def test_admin_empty_login(driver, email, password):
    login(driver, email, password)
    verify_text_in_page(driver, "Email and/or Password can not be empty")
    

@pytest.mark.parametrize("email, password", [("admin@mail.com", "Password@123")])
def test_admin_logout(driver, email, password):
    test_admin_login(driver, email, password)
    driver.find_element(By.LINK_TEXT, "Administrator").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(2)
    verify_text_in_page(driver, "Log in to start your session")
