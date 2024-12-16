from driver import *
from Test_login_logout import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def update_product(driver, product_name, updated_info):
    test_user_login(driver)

    # Truy cập trang danh sách sản phẩm
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/admin/product.php")
    
    # Tìm kiếm sản phẩm cần cập nhật theo tên (hoặc bạn có thể thay bằng thông tin khác)
    search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/label/input")
    search_box.send_keys(product_name)

    time.sleep(2)

    # Click vào link Edit của sản phẩm tìm thấy
    try:
        product_edit_link = driver.find_element(By.LINK_TEXT,"Edit")  
        product_edit_link.click()
    except Exception as e:
        print(f"Không tìm thấy sản phẩm: {e}")
        return "Product not found."

    # Lấy thông tin từ updated_info và cập nhật sản phẩm
    top_level_category = updated_info.get("top_level_category")
    mid_level_category = updated_info.get("mid_level_category")
    end_level_category = updated_info.get("end_level_category")
    name = updated_info.get("name")
    color = updated_info.get("color")
    quantity = updated_info.get("quantity")
    old_price = updated_info.get("old_price")
    current_price = updated_info.get("current_price")
    size = updated_info.get("size")
    featured_photo = updated_info.get("featured_photo")
    is_featured = updated_info.get("is_featured")
    is_active = updated_info.get("is_active")

    # Cập nhật các trường
    if top_level_category:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[1]/div/span/span[1]/span/span[1]").click()
        select_top_level_input = driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        select_top_level_input.send_keys(top_level_category)
        select_top_level_input.send_keys(Keys.RETURN)
        time.sleep(1)

    if mid_level_category:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[2]/div/span/span[1]/span/span[1]").click()
        select_mid_level_input = driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        select_mid_level_input.send_keys(mid_level_category)
        select_mid_level_input.send_keys(Keys.RETURN)
        time.sleep(1)

    if end_level_category:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[3]/div/span/span[1]/span/span[1]").click()
        select_end_level_input = driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        select_end_level_input.send_keys(end_level_category)
        select_end_level_input.send_keys(Keys.RETURN)
        time.sleep(1)

    if name:
        driver.find_element(By.NAME, "p_name").clear()
        driver.find_element(By.NAME, "p_name").send_keys(name)
        time.sleep(1)

    if old_price:
        driver.find_element(By.NAME, "p_old_price").clear()
        driver.find_element(By.NAME, "p_old_price").send_keys(old_price)
        time.sleep(1)

    if current_price:
        driver.find_element(By.NAME, "p_current_price").clear()
        driver.find_element(By.NAME, "p_current_price").send_keys(current_price)
        time.sleep(1)

    if quantity:
        driver.find_element(By.NAME, "p_qty").clear()
        driver.find_element(By.NAME, "p_qty").send_keys(quantity)
        time.sleep(1)

    if size:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[8]/div/span/span[1]/span/ul").click()
        size_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[8]/div/span/span[1]/span/ul/li/input")
        size_input.clear()
        size_input.send_keys(size)
        size_input.send_keys(Keys.RETURN)
        time.sleep(1)

    if color:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[9]/div/span/span[1]/span/ul").click()
        color_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/form/div/div/div[9]/div/span/span[1]/span/ul/li/input")
        color_input.clear()
        color_input.send_keys(color)
        color_input.send_keys(Keys.RETURN)
        time.sleep(1)

    if is_featured:
        featured = Select(driver.find_element(By.NAME, "p_is_featured"))
        featured.select_by_visible_text(is_featured)
        time.sleep(1)

    if is_active:
        active = Select(driver.find_element(By.NAME, "p_is_active"))
        active.select_by_visible_text(is_active)
        time.sleep(1)

    # Submit form để cập nhật sản phẩm
    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)
    
    return "Product updated successfully."
