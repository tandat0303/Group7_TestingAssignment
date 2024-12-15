from selenium.webdriver.common.by import By
from driver import * 
from functions.addtocart import *
from functions.search import *
from functions.login import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test case: Add multiple products to the cart with valid information
def test_add_multiple_products_to_cart(driver):
    products_info = [
        {"name": "Men's Soft Classic Sneaker", "color": "Coffee", "quantity": 2},
        {"name": "Truck Boys Pajamas Toddler Sleepwear Clothes", "color": "Blue", "quantity": 3},
        {"name": "Digital Infrared Thermometer for Adults and Kids", "color": "White", "quantity": 4}
    ]
    
    add_to_cart(driver, products_info)  # Call function to add products to the cart
    
    # Navigate to the cart and wait for the table to load
    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "table")))

    table = driver.find_element(By.CLASS_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        
        if len(columns) > 1:
            product_name_in_cart = columns[2].text  # Get product name from the third column
            qty_input = columns[6].find_element(By.NAME, "quantity[]")
            product_qty_in_cart = qty_input.get_attribute("value").strip()  # Get the quantity value
            
            # Find the matching product and check if the name and quantity match
            matching_product = next((product for product in products_info if product["name"] == product_name_in_cart), None)
            assert matching_product, f"{product_name_in_cart} is not in the cart"
            
            expected_qty = str(matching_product["quantity"])
            assert expected_qty == product_qty_in_cart, f"Quantity mismatch for {product_name_in_cart}, expected {expected_qty}, got {product_qty_in_cart}"


# Test case 2: Thêm sản phẩm vào giỏ hàng khi sản phẩm không tồn tại
def test_add_non_existent_product_to_cart(driver):
    non_existent_product_info = [
        {"name": "NonExistentProduct", "color": "Red", "quantity": 1}
    ]
    
    # Tìm kiếm sản phẩm không tồn tại
    search(driver, non_existent_product_info[0]["name"])
    
    # Kiểm tra xem có thông báo "No result found" xuất hiện không
    assert "No result found" in driver.page_source, "Expected 'No result found' message, but it was not found."

# Test case 3: Thêm sản phẩm vào giỏ hàng với số lượng không hợp lệ
def test_add_product_with_invalid_quantity_to_cart(driver):
    invalid_quantity_product_info = [
        {"name": "Men's Soft Classic Sneaker", "color": "Coffee", "quantity": "-1"},
        {"name": "Truck Boys Pajamas Toddler Sleepwear Clothes", "color": "Blue", "quantity": "0"}
    ]
    
    add_to_cart(driver, invalid_quantity_product_info)
    
    # Navigate to the cart and wait for the table to load
    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    assert "Cart is Empty!!" in driver.page_source

# Test case 4: Thêm sản phẩm vào giỏ hàng với màu sắc không hợp lệ
def test_add_product_with_invalid_color_to_cart(driver):
    invalid_color_product_info = [
        {"name": "Men's Soft Classic Sneaker", "color": "InvalidColor", "quantity": 2}
    ]
    
    add_to_cart(driver, invalid_color_product_info)
    
    # Kiểm tra thông báo lỗi về màu sắc không hợp lệ
    assert "Invalid color" in driver.page_source  # Điều chỉnh thông báo lỗi cho phù hợp

def test_remove_item_from_cart(driver):
    # Thêm sản phẩm vào giỏ hàng
    product_info = [
        {"name": "Men's Soft Classic Sneaker", "color": "Coffee", "quantity": 1}
    ]
    add_to_cart(driver, product_info)
    
    # Mở giỏ hàng
    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    
    # Lấy tất cả các dòng trong giỏ hàng
    table = driver.find_element(By.CLASS_NAME, "table")
    
    # Chờ một chút để đảm bảo DOM đã cập nhật sau khi xóa
    time.sleep(2)
    
    # Lấy lại các dòng sau khi DOM đã cập nhật
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    # Kiểm tra các sản phẩm trong giỏ hàng
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        
        if len(columns) > 1:
            # Lấy tên sản phẩm trong giỏ hàng
            product_name_in_cart = columns[2].text
            
            # Nếu tên sản phẩm trùng khớp với tên đã thêm, tiến hành xóa
            if product_name_in_cart == "Men's Soft Classic Sneaker":
                remove_button = driver.find_element(By.CLASS_NAME, "trash") 
                remove_button.click()
                time.sleep(2)  # Chờ để hành động xóa hoàn tất
                
                # Xử lý hộp thoại xác nhận (alert)
                try:
                    # Chờ alert xuất hiện và đồng ý xóa
                    WebDriverWait(driver, 5).until(EC.alert_is_present())  # Đợi tối đa 5 giây để alert xuất hiện
                    alert = driver.switch_to.alert  # Chuyển tới alert
                    alert.accept()  # Chấp nhận (OK) alert
                    time.sleep(2)  # Chờ sau khi chấp nhận
                except:
                    print("No confirmation alert found.")
                
                # Thoát vòng lặp khi sản phẩm đã bị xóa
                break  # Dừng vòng lặp sau khi xóa thành công
    
    # Mở lại giỏ hàng và kiểm tra nếu sản phẩm đã bị xóa
    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()  # Mở lại giỏ hàng
    
    # Lấy lại các dòng sau khi DOM đã cập nhật
    rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'cart')]//tr")
    
    # Kiểm tra xem sản phẩm đã bị xóa chưa
    assert "Men's Soft Classic Sneaker" not in driver.page_source, "Product was not removed from the cart"

def test_cart_after_account_update(driver):
    login(driver, "testuser1@example.com", "Password123")
    # Thêm sản phẩm vào giỏ hàng
    product_info = [
        {"name": "Men's Soft Classic Sneaker", "color": "Coffee", "quantity": 1}
    ]
    add_to_cart(driver, product_info)
    
    # Mở giỏ hàng
    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    
    # Đăng xuất
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/dashboard.php")
    driver.find_element(By.LINK_TEXT,"Logout").click()
    
    # Đăng nhập lại
    login(driver, "testuser1@example.com", "Password123")
    
    # Kiểm tra sản phẩm trong giỏ hàng sau khi đăng nhập lại
    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    assert "Men's Soft Classic Sneaker" in driver.page_source

def test_add_product_with_quantity_greater_than_stock(driver):
    
    # Thêm sản phẩm vào giỏ hàng với số lượng lớn hơn số lượng có sẵn trong kho (257)
    product_info = [
        {"name": "Men's Soft Classic Sneaker", "color": "Coffee", "quantity": "10000"}  
    ]
    
    add_to_cart(driver, product_info)
    
    # Chờ thông báo alert xuất hiện
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    
    # Lấy thông báo alert
    alert = driver.switch_to.alert
    alert_text = alert.text
    
    # In nội dung alert ra để kiểm tra
    print("Alert text: ", alert_text)
    
    # Kiểm tra thông báo lỗi
    assert "Sorry! There are only 257 item(s) in stock" in alert_text
    
    # Đóng alert
    alert.accept()

# def test_update_item_quantity_in_cart(driver):
#     # Thêm sản phẩm vào giỏ hàng
#     product_info = [
#         {"name": "Men's Soft Classic Sneaker", "color": "Coffee", "quantity": 1}
#     ]
#     add_to_cart(driver, product_info)
    
#     # Mở giỏ hàng
#     driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()

#     table = driver.find_element(By.CLASS_NAME, "table")
#     rows = table.find_elements(By.TAG_NAME, "tr")
#     product_name ="Men's Soft Classic Sneaker"
#     for row in rows:
#         columns = row.find_elements(By.TAG_NAME, "td")
        
#     if len(columns) > 1:

#         product_name_in_cart = columns[2].text  

#         if product_name == product_name_in_cart:

#             quantity_input = driver.find_element(By.CLASS_NAME, "input-text") 
#             quantity_input.clear()
#             quantity_input.send_keys("2")  
                

#             driver.find_element(By.NAME, "form1").click()
#             time.sleep(2)


#         updated_quantity = driver.find_element(By.CLASS_NAME, "input-text").get_attribute("value")
#         updated_price = driver.find_element(By.CLASS_NAME, "text-right").text 

#         assert updated_quantity == "2"  
#         assert "Total Price: $..." in updated_price  