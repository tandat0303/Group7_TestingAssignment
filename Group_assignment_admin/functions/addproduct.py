from driver import *
from Test_login_logout import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def add_product(driver,product):
    test_user_login(driver)
    for info in product:
        top_level_category = info["top_level_category"]
        mid_level_category = info["mid_level_category"]
        end_level_category = info["end_level_category"]
        name = info["name"]
        color = info["color"]
        quantity = info["quantity"]
        old_price = info["old_price"]
        current_price = info["current_price"]
        size = info["size"]
        featured_photo = info["featured_photo"]
        is_featured = info["is_featured"]
        is_active = info["is_active"]

        driver.get("http://localhost/Phpcode/eCommerceSite-PHP/admin/product.php")
        driver.find_element(By.LINK_TEXT,"Add Product").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[1]/div/span/span[1]/span/span[1]").click()
        select_top_level_input=driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
        select_top_level_input.send_keys(top_level_category)
        select_top_level_input.send_keys(Keys.RETURN)
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[2]/div/span/span[1]/span/span[1]").click()
        select_mid_level_input=driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        select_mid_level_input.send_keys(mid_level_category)
        select_mid_level_input.send_keys(Keys.RETURN)
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[3]/div/span/span[1]/span/span[1]").click()
        select_end_level_input=driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        select_end_level_input.send_keys(end_level_category)
        select_end_level_input.send_keys(Keys.RETURN)
        time.sleep(1)

        driver.find_element(By.NAME,"p_name").send_keys(name)
        time.sleep(1)

        driver.find_element(By.NAME,"p_old_price").send_keys(old_price)
        time.sleep(1)
        driver.find_element(By.NAME,"p_current_price").send_keys(current_price)
        time.sleep(1)
        driver.find_element(By.NAME,"p_qty").send_keys(quantity)
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[8]/div/span/span[1]/span/ul").click()
        size_input=driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[8]/div/span/span[1]/span/ul/li/input")
        size_input.send_keys(size)
        size_input.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/div/div/form/div/div/div[9]/div/span/span[1]/span/ul").click()
        color_input=driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/div/div/form/div/div/div[9]/div/span/span[1]/span/ul/li/input")
        color_input.send_keys(color)
        color_input.send_keys(Keys.RETURN)
        time.sleep(1)
        # if featured_photo:
        #     featured_photo_input = driver.find_element(By.NAME, "p_featured_photo").click()
        #     featured_photo_input.send_keys(featured_photo)  

        # time.sleep(1)  
        
        featured=Select(driver.find_element(By.NAME,"p_is_featured"))
        featured.select_by_visible_text(is_featured)
        time.sleep(1)
        
        active=Select(driver.find_element(By.NAME,"p_is_active"))
        active.select_by_visible_text(is_active)
        time.sleep(1)
        
        driver.find_element(By.NAME,"form1").click()
        time.sleep(2)

        return "Product is added successfully."