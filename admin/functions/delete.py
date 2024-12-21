from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from functions.login import login
from functions.search import search

def delete_product(driver, email, password, product_name):
    login(driver, email, password)
    try:
        driver.find_element(By.LINK_TEXT, "Product Management").click()
        
        # Tìm kiếm sản phẩm cần cập nhật theo tên (hoặc bạn có thể thay bằng thông tin khác)
        search(driver, product_name)

        # Tìm nút xóa trong dòng sản phẩm này
        delete_button = driver.find_element(By.LINK_TEXT, "Delete")
        
        # Nhấn nút xóa
        delete_button.click()
        time.sleep(2)
        
        # Nếu có hộp thoại xác nhận xóa, chấp nhận
        confirm_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[3]/a")
        confirm_button.click()
        

        time.sleep(2)  # Đợi một chút để chắc chắn rằng sản phẩm đã bị xóa
    except Exception as e:
        print(f"Error: {str(e)}")
