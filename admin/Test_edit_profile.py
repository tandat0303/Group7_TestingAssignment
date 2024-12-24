from driver import *
from functions.update_profile import update_profile, update_password

# Test cases
@pytest.mark.parametrize("email, password, full_name, phone",
                         [("admin@mail.com", "Password@123", "Admin", "0397387337")])
def test_update_information(driver, email, password, full_name, phone):
    """Test successful profile update."""
    update_profile(driver,email, password, full_name, email, phone)
    assert "Profile updated successfully" in driver.page_source


@pytest.mark.parametrize("email, password, full_name, invalid_email, phone",
                         [("admin@mail.com", "Password@123", "Admin", "admin@mail", "0397387337")])
def test_invalid_email_format(driver, email, password, full_name, invalid_email, phone):
    update_profile(driver, email, password, full_name, invalid_email, phone)
    assert "Email address must be valid." in driver.page_source


@pytest.mark.parametrize("email, password, full_name, update_email, phone",
                         [("admin@mail.com", "Password@123", "", "", "")])
def test_empty_fields(driver, email, password, full_name, update_email, phone):
    """Test profile update with empty fields."""
    update_profile(driver, email, password, full_name, update_email, phone)
    assert "Name can not be empty." in driver.page_source
    assert "Email Address can not be empty" in driver.page_source


@pytest.mark.parametrize("email, password, full_name, phone",
                         [("admin@mail.com", "Password@123", "Admin", "invalid_phone")])
def test_invalid_phone(driver, email, password, full_name, phone):
    """Test profile update with invalid phone number."""
    update_profile(driver, email, password, full_name, email, phone)
    assert "Phone number must be valid." in driver.page_source


@pytest.mark.parametrize("email, password, new_password, re_password",
                         [("admin@mail.com", "Password@123", "Password@123", "Password@123")])
def test_update_password_success(driver, email, password, new_password, re_password):
    """Test successful password update."""
    update_password(driver, email, password, new_password, re_password)
    assert "Password updated successfully" in driver.page_source


@pytest.mark.parametrize("email, password, new_password, re_password",
                         [("admin@mail.com", "Password@123", "NewPass", "WrongPassword")])
def test_update_password_mismatch(driver, email, password, new_password, re_password):
    """Test password update with mismatched confirmation."""
    update_password(driver, email, password, new_password, re_password)
    assert "Password confirmation does not match." in driver.page_source
