from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def register(driver, user_info):
    driver.get('http://localhost/eCommerceSite-PHP/registration.php')

    for info in user_info:
        name = info["name"]
        cname = info["cname"]
        email = info["email"]
        phone = info["phone"]
        address = info["address"]
        country = info["country"]
        city = info["city"]
        state = info["state"]
        zip = info["zip"]
        password = info["password"]
        re_password = info["re_password"]
        
        driver.find_element(By.NAME, "cust_name").send_keys(name)
        time.sleep(1.5)

        driver.find_element(By.NAME, "cust_cname").send_keys(cname)
        time.sleep(1.5)

        driver.find_element(By.NAME, "cust_email").send_keys(email)
        time.sleep(1.5)

        driver.find_element(By.NAME, "cust_phone").send_keys(phone)
        time.sleep(1.5)

        driver.find_element(By.NAME, "cust_address").send_keys(address)
        time.sleep(1.5)

        # Using the "Select" module of Selenium to be able to use the select item in HTML
        select_element = Select(driver.find_element(By.NAME, "cust_country"))

        # Use the "select_by_visible_text()" method to set the value for the select item
        select_element.select_by_visible_text(country)
        time.sleep(2)

        driver.find_element(By.NAME, "cust_city").send_keys(city)
        time.sleep(1.5)

        driver.find_element(By.NAME, "cust_state").send_keys(state)
        time.sleep(1.5)

        driver.find_element(By.NAME, "cust_zip").send_keys(zip)
        time.sleep(1.5)

        driver.find_element(By.NAME, "cust_password").send_keys(password)
        time.sleep(1.5)

        driver.find_element(By.NAME, "cust_re_password").send_keys(re_password)
        time.sleep(1.5)

        driver.find_element(By.NAME, "form1").click()
        time.sleep(1.5)