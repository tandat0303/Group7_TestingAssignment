import pytest
from selenium import webdriver
from driver import *  
from functions.regis import register


# Define test data
valid_user = {
    "name": "testuser",
    "cname": "ABC Company",
    "email": "testuser1@example.com",
    "phone": "0397387337",
    "address": "123 Main St",
    "country": "Vietnam",
    "city": "Ho Chi Minh",
    "state": "Mien Nam",
    "zip": "112233",
    "password": "Password123",
    "re_password": "Password123"
}

invalid_email_user = {
    "name": "testuser",
    "cname": "ABC Company",
    "email": "invalidemail",
    "phone": "0397387337",
    "address": "123 Main St",
    "country": "Vietnam",
    "city": "Ho Chi Minh",
    "state": "Mien Nam",
    "zip": "112233",
    "password": "Password123",
    "re_password": "Password123"
}

mismatched_password_user = {
    "name": "testuser",
    "cname": "ABC Company",
    "email": "testuser1@example.com",
    "phone": "0397387337",
    "address": "123 Main St",
    "country": "Vietnam",
    "city": "Ho Chi Minh",
    "state": "Mien Nam",
    "zip": "112233",
    "password": "Password123",
    "re_password": "DifferentPass123"
}

missing_required_fields_user = {
    "name": "",
    "cname": "",
    "email": "",
    "phone": "",
    "address": "",
    "country": "Vietnam",
    "city": "",
    "state": "",
    "zip": "",
    "password": "",
    "re_password": ""
}

max_length_username_user = {
    "name": "a" * 51,  
    "cname": "ABC Company",
    "email": "testuser2@example.com",
    "phone": "0397387337",
    "address": "123 Main St",
    "country": "Vietnam",
    "city": "Ho Chi Minh",
    "state": "Mien Nam",
    "zip": "112233",
    "password": "Password123",
    "re_password": "Password123"
}

special_characters_user = {
    "name": "test@user!$",
    "cname": "ABC Company",
    "email": "testuser3@example.com",
    "phone": "039738@$#@#7337",
    "address": "123 Main St",
    "country": "Vietnam",
    "city": "Ho Chi Minh",
    "state": "Mien Nam",
    "zip": "112233",
    "password": "Password123",
    "re_password": "Password123"
}



# Test cases
def test_register_valid_user(driver):
    register(driver, [valid_user])
    # Check for successful registration message or redirection
    assert "Your registration is completed. Please check your email address to follow the process to confirm your registration." in driver.page_source

def test_register_empty(driver):
    # Attempt to register with empty fields
    register(driver, [missing_required_fields_user])
    
    # Check for error message related to missing required fields
    assert "Customer Name can not be empty." in driver.page_source
    assert "Email Address can not be empty" in driver.page_source
    assert "Phone Number can not be empty." in driver.page_source
    assert "Address can not be empty." in driver.page_source
    assert "City can not be empty."in driver.page_source
    assert "State can not be empty."in driver.page_source
    assert "City can not be empty."in driver.page_source
    assert "Zip Code can not be empty." in driver.page_source
    assert "Password can not be empty." in driver.page_source

def test_register_invalid_email(driver):
    register(driver, [invalid_email_user])
    # Check for error message related to email validation
    assert "Email address must be valid." in driver.page_source

def test_registration_max_username(driver):
    register(driver, [max_length_username_user])

    assert "Your registration is completed. Please check your email address to follow the process to confirm your registration." in driver.page_source

def test_registration_special(driver):
    # Attempt to register with special characters in the username
    register(driver, [special_characters_user])
    
    assert "Special characters are not allowed" in driver.page_source  

def test_retypePW_match(driver):

    register(driver, [mismatched_password_user])
    
    assert "Passwords do not match." in driver.page_source  
