# Call all modules and functions in the "driver.py" file
from driver import *
from functions.login import login

# Test the login functionality with valid email and password
@pytest.mark.parametrize("email, password", [("ls17189a3.11@gmail.com", 123456)])
def test_valid_login(driver, email, password):
    login(driver, email, password)
    assert "http://localhost/eCommerceSite-PHP/dashboard.php" in driver.current_url


# Test the login functionality with invalid email
@pytest.mark.parametrize("email, password", [("ls1718gmail.com", 123456)])
def test_invalid_email(driver, email, password):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    mail = driver.find_element(By.NAME, "cust_email")
    mail.send_keys(email)
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(password)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    # Get the UI error message
    error_message = mail.get_attribute("validationMessage")

    assert "include an '@' in the email address" in error_message


# Test the login functionality with wrong email
@pytest.mark.parametrize("email, password", [("ls17189@gmail.com", 123456)])
def test_wrong_email(driver, email, password):
    login(driver, email, password)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Email Address does not match." in error

# Test the login functionality with wrong password
@pytest.mark.parametrize("email, password", [("ls17189a3.11@gmail.com", 1234)])
def test_wrong_password(driver, email, password):
    login(driver, email, password)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Passwords do not match." in error


# Test the login functionality without filling the fields
@pytest.mark.parametrize("email, password", [("", "")])
def test_empty_fields(driver, email, password):
    login(driver, email, password)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Email and/or Password can not be empty." in error

