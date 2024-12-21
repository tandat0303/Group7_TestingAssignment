import time
from selenium.webdriver.common.by import By

def search(driver, product_name):
    search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/label/input")
    search_box.send_keys(product_name)
    time.sleep(2)