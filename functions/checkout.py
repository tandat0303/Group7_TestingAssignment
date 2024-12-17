from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Automated_Testing.Test_addtocart import test_add_products
from functions.login import login
import time

def checkout(driver, email, password, products, payment_method):
    login(driver, email, password)
    
    driver.find_element(By.XPATH, "//button[text()='Update Billing and Shipping Info']").click()
    time.sleep(2)

    if not is_billing_address_filled(driver):
        update_billing_address(driver)
        
    if not is_shipping_address_filled(driver):
        update_shipping_address(driver)
    
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(2)

    test_add_products(driver, products)    

    # Click "Proceed to Checkout"
    driver.find_element(By.XPATH, "//a[@href='checkout.php']").click()
    time.sleep(2)

    select_payment_method = Select(driver.find_element(By.NAME, "payment_method"))
    select_payment_method.select_by_visible_text(payment_method)
    time.sleep(2)

# This is a function to fill all fields of Billing Address to Checkout
def update_billing_address(driver):
    driver.find_element(By.NAME, "cust_b_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_cname").send_keys("SGU")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_phone").send_keys("0383161867")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_b_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_address").send_keys("An Duong Vuong")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)
    
    driver.find_element(By.NAME, "cust_b_state").send_keys("Mien Nam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_zip").send_keys(112233)
    time.sleep(1.5)


# This is a function to fill all fields of Shipping Address to Checkout
def update_shipping_address(driver):
    driver.find_element(By.NAME, "cust_s_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_cname").send_keys("SGU")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_phone").send_keys("0383161867")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_s_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_address").send_keys("112 Huynh Ba Chanh")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)
    
    driver.find_element(By.NAME, "cust_s_state").send_keys("Mien Nam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_zip").send_keys(112233)
    time.sleep(1.5)


# This is a function to check if all fields of Billing Address are filled and updated
def is_billing_address_filled(driver):
    required_fields = ["cust_b_name", "cust_b_cname", "cust_b_phone", "cust_b_address", "cust_b_city", "cust_b_state", "cust_b_zip"]
    for field_name in required_fields:
        field_value = driver.find_element(By.NAME, field_name).get_attribute("value")
        if not field_value:
            return False
    return True


# This is a function to check if all fields of Shipping Address are filled and updated
def is_shipping_address_filled(driver):
    required_fields = ["cust_s_name", "cust_s_cname", "cust_s_phone", "cust_s_address", "cust_s_city", "cust_s_state", "cust_s_zip"]
    for field_name in required_fields:
        field_value = driver.find_element(By.NAME, field_name).get_attribute("value")
        if not field_value:
            return False
    return True