# Call all modules and functions in the "driver.py" file
from driver import *
from functions.login import login
from functions.update_pass import update_password
from selenium.common.exceptions import UnexpectedAlertPresentException

# Test the forget password functionality
def test_forget_password(driver):
    driver.get("http://localhost/eCommerceSite-PHP/login.php")

    driver.find_element(By.LINK_TEXT, "Forget Password?").click()
    time.sleep(2)

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    # Click "Submit"
    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

    # If there was an alert after submitting, accept it
    try:
        alert = driver.switch_to.alert
        alert_message = alert.text
        alert.accept()  # Accept alert
        time.sleep(2)
    except UnexpectedAlertPresentException:
        print("There is no alert to be handle")

    assert "A confirmation link is sent to your email address. You will get the password reset information in there." in alert_message


# Test the forget password functionality with invalid email
def test_invalid_email(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    email = driver.find_element(By.NAME, "cust_email")
    email.send_keys("ls17189gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

    # Get the UI error message
    error_message = email.get_attribute("validationMessage")

    assert "include an '@' in the email address" in error_message


# Test the user updating information functionality
@pytest.mark.parametrize(
    "email, password",[("ls17189a3.11@gmail.com",123456)]
)
def test_update_info(driver, email, password):
    login(driver, email, password)

    driver.find_element(By.XPATH, "//button[text()='Update Profile']").click()
    time.sleep(2)

    name = driver.find_element(By.NAME, "cust_name")
    name.clear() # Clear value of input field
    name.send_keys("Dat")
    time.sleep(1.5)

    cname = driver.find_element(By.NAME, "cust_cname")
    cname.clear()
    cname.send_keys("SGU")
    time.sleep(1.5)

    phone = driver.find_element(By.NAME, "cust_phone")
    phone.clear()
    phone.send_keys("12345")
    time.sleep(1.5)

    address = driver.find_element(By.NAME, "cust_address")
    address.clear()
    address.send_keys("Hills")
    time.sleep(1.5)

    # Using the "Select" module of Selenium to be able to use the select item in HTML
    select_element = Select(driver.find_element(By.NAME, "cust_country"))

    # Use the "select_by_visible_text()" method to set the value for the select item
    select_element.select_by_visible_text("United States")
    time.sleep(2)

    city = driver.find_element(By.NAME, "cust_city")
    city.clear()
    city.send_keys("New York")
    time.sleep(1.5)

    state = driver.find_element(By.NAME, "cust_state")
    state.clear()
    state.send_keys("Florida")
    time.sleep(1.5)

    zip = driver.find_element(By.NAME, "cust_zip")
    zip.clear()
    zip.send_keys(11223344)
    time.sleep(1.5)

    # Click "Update"
    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

    success = driver.find_element(By.CLASS_NAME, "success").text

    assert "updated successfully" in success


# Test updating the "Name" field data, the new value contains a special character
def test_special_character(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Update Profile']").click()
    time.sleep(2)

    # Add some special character (such as @,!,: ...) in field "Name"
    name = driver.find_element(By.NAME, "cust_name")
    name.clear()
    name.send_keys("Dat@!")
    time.sleep(1.5)

    # Click "Update"
    driver.find_element(By.NAME, "form1").click()
    time.sleep(1.5)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Fullname is not contain special character(s)." in error


# Test update password functionality
@pytest.mark.parametrize(
    "email, password, new_pass, re_pass",[("ls17189a3.11@gmail.com",123456, 123456, 123456)]
)
def test_update_password(driver, email, password, new_pass, re_pass):
    login(driver, email, password)

    update_password(driver, new_pass, re_pass)

    success = driver.find_element(By.CLASS_NAME, "success").text
    assert "Password is updated" in success


# Test the retype password if it matches the password in the reset password form
@pytest.mark.parametrize(
    "email, password, new_pass, re_pass",[("ls17189a3.11@gmail.com",123456, 123456, 1234)]
)
def test_passwords_match(driver, email, password, new_pass, re_pass):
    login(driver, email, password)

    update_password(driver, new_pass, re_pass)

    if new_pass == re_pass:
        success = driver.find_element(By.CLASS_NAME, "success").text
        assert "Password is updated" in success
    else:
        error = driver.find_element(By.CLASS_NAME, "error").text
        assert "Passwords do not match." in error


# Test the Contact functionality
def test_contact_us(driver):
    driver.get('http://localhost/eCommerceSite-PHP/index.php')

    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(2)

    driver.find_element(By.NAME, "visitor_name").send_keys("Dat")
    time.sleep(2)

    driver.find_element(By.NAME, "visitor_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "visitor_phone").send_keys("0123456789")
    time.sleep(2)

    driver.find_element(By.NAME, "visitor_message").send_keys("Please send me all vouchers your shop has")
    time.sleep(2)

    # Click "Send Message"
    driver.find_element(By.NAME, "form_contact").click()
    time.sleep(2)

    # If there was an alert after sending message, accept it
    try:
        alert = driver.switch_to.alert
        alert_message = alert.text
        alert.accept()  # Accept alert
        time.sleep(2)
    except UnexpectedAlertPresentException:
        print("There is no alert to be handle")

    assert "Thank you for sending email. We will contact you shortly." in alert_message