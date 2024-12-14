import time
from selenium.webdriver.common.by import By
from functions.login import login

def test_logout(driver):
    """
    Test the logout functionality by first logging in and then logging out.
    """
    # Navigate to the login page
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    # Perform login using the reusable login function
    login(driver, "ls17189a3.11@gmail.com", "123456")

    # Perform logout
    logout_button = driver.find_element(By.XPATH, "//button[text()='Logout']")
    logout_button.click()
    time.sleep(2)

    # Verify the user is redirected to the login page after logout
    assert "http://localhost/eCommerceSite-PHP/login.php" in driver.current_url
