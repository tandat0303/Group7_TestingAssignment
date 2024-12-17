from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from functions.search import search
import time

def add_to_cart(driver, product_info):
    for info in product_info:
        name = info["name"]
        color = info["color"]
        quantity = info["quantity"]

        search(driver, name)

        driver.find_element(By.LINK_TEXT, name).click()

        # Using the "Select" module of Selenium to be able to use the select item in HTML
        select_color = Select(driver.find_element(By.NAME, "color_id"))

        # Use the "select_by_visible_text()" method to set the value for the select item
        select_color.select_by_visible_text(color)
        time.sleep(2)

        qty_input = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty[name='p_qty']")
        qty_input.clear()
        qty_input.send_keys(quantity)
        time.sleep(2)
        
        driver.find_element(By.NAME, "form_add_to_cart").click()
        time.sleep(2)