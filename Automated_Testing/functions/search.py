from selenium.webdriver.common.by import By
import time

def search(driver, keyword):
    driver.get("http://localhost/eCommerceSite-PHP/index.php")

    driver.find_element(By.NAME, "search_text").send_keys(keyword)
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    time.sleep(2)