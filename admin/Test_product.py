import pytest
from driver import * 
from functions.addproduct import *
from functions.update_product import*
from functions.delete import *

# Test case 1: Thêm sản phẩm mới
@pytest.mark.parametrize("email, password, product",
                         [("admin@mail.com",
                           "Password@123",
                           [{
                                "name": "Keyboard", 
                                "color": "Black", 
                                "quantity": 30, 
                                "top_level_category": "Electronics", 
                                "mid_level_category": "Computers", 
                                "end_level_category": "Computers and Tablets",
                                "old_price": 60, 
                                "current_price": 50, 
                                "size": "18 Plus", 
                                "featured_photo": r"D:\Năm 4\Kiểm thử phần mềm\Final Projects\Flowchart\AddtoCart.jpg", 
                                "is_featured": "Yes", 
                                "is_active": "Yes"}])])
def test_add_product_valid(driver, email, password, product): 
    add_product(driver, email, password, product)
    
    assert "Product is added successfully." in driver.page_source

@pytest.mark.parametrize("email, password, product",
                         [("admin@mail.com",
                           "Password@123",
                           [{
                                "name": "", 
                                "color": "Black", 
                                "quantity": 30, 
                                "top_level_category": "Electronics", 
                                "mid_level_category": "Computers", 
                                "end_level_category": "Computers and Tablets",
                                "old_price": 60, 
                                "current_price": 50, 
                                "size": "18 Plus", 
                                "featured_photo": r"D:\Năm 4\Kiểm thử phần mềm\Final Projects\Flowchart\AddtoCart.jpg", 
                                "is_featured": "Yes", 
                                "is_active": "Yes"}])])
def test_add_product_missing_field(driver, email, password, product):
    add_product(driver, email, password, product)
    assert "Product name can not be empty" in driver.page_source

@pytest.mark.parametrize("email, password, product",
                         [("admin@mail.com",
                           "Password@123",
                           [{
                                "name": "Test", 
                                "color": "Black", 
                                "quantity": -30, 
                                "top_level_category": "Electronics", 
                                "mid_level_category": "Computers", 
                                "end_level_category": "Computers and Tablets",
                                "old_price": -60, 
                                "current_price": -50, 
                                "size": "18 Plus", 
                                "featured_photo": r"D:\Năm 4\Kiểm thử phần mềm\Final Projects\Flowchart\AddtoCart.jpg", 
                                "is_featured": "Yes", 
                                "is_active": "Yes"}])])
def test_add_product_invalid_price(driver, email, password, product):
    add_product(driver, email, password, product)
    assert " Price and quantity must be greater than 0" in driver.page_source

# Test case 2: Sửa thông tin sản phẩm
@pytest.mark.parametrize("email, password, product_name, updated_info",
                         [("admin@mail.com",
                           "Password@123",
                           "test",
                           {
                               "name": "Game", 
                                "old_price": 1000,  
                                "current_price": 1200,  
                                "size": "20 Plus",  
                                "is_featured": "Yes",  
                                "is_active": "Yes"
                           })])
def test_update_product_valid(driver, email, password, product_name, updated_info):
    update_product(driver, email, password, product_name, updated_info)

    assert "Product updated successfully." in driver.page_source

    product_name_on_page = driver.find_element(By.NAME, "p_name").get_attribute("value")
    old_price_on_page = driver.find_element(By.NAME, "p_old_price").get_attribute("value")
    current_price_on_page = driver.find_element(By.NAME, "p_current_price").get_attribute("value")
    
    assert product_name_on_page == "Game"
    assert old_price_on_page == "1000"
    assert current_price_on_page == "1200"


@pytest.mark.parametrize("email, password, product_name, updated_info",
                         [("admin@mail.com",
                           "Password@123",
                           "Game",
                           {
                               "current_price": " "
                           })])
def test_update_product_missing_field(driver, email, password, product_name, updated_info):
    update_product(driver, email, password, product_name, updated_info)
    
    assert "Price not be empty." in driver.page_source


# Test case 3: Xóa sản phẩm
@pytest.mark.parametrize("email, password, product_name",
                         [("admin@mail.com", "Password@123", "Game")])
def test_delete_product_valid(driver, email, password, product_name):   
    delete_product(driver, email, password, product_name)
    
    search(driver, product_name)

    assert "No matching records found" in driver.page_source
    
    try:
        driver.find_element(By.XPATH, f"//tr[td[contains(text(), '{product_name}')]]")
        assert False, "Product not deleted successfully"
    except:
        assert True
