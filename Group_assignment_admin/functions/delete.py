from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Test_login_logout import *

def delete_product(driver, product_name):
    test_user_login(driver)
    try:
        # Truy cập trang danh sách sản phẩm
        driver.get("http://localhost/Phpcode/eCommerceSite-PHP/admin/product.php")
        
        # Tìm kiếm sản phẩm cần cập nhật theo tên (hoặc bạn có thể thay bằng thông tin khác)
        search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/label/input")
        search_box.send_keys(product_name)
        time.sleep(2)

        # Tìm nút xóa trong dòng sản phẩm này
        delete_button = driver.find_element(By.LINK_TEXT, "Delete")
        
        # Nhấn nút xóa
        delete_button.click()
        time.sleep(2)
        
        # Nếu có hộp thoại xác nhận xóa, chấp nhận
        confirm_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[3]/a")
        confirm_button.click()
        

        time.sleep(2)  # Đợi một chút để chắc chắn rằng sản phẩm đã bị xóa
        return "Product deleted successfully"
    except Exception as e:
        return f"Error: {str(e)}"
