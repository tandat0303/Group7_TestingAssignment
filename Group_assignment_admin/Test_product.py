import pytest
from driver import * 
from functions.addproduct import *
from functions.update_product import*
from functions.delete import *


# Test case 1: Thêm sản phẩm mới
def test_add_product_valid(driver):
    new_product = [{
        "name": "Keyboard", 
        "color": "Black", 
        "quantity": 30, 
        "top_level_category": "Electronics", 
        "mid_level_category": "Computers", 
        "end_level_category": "Computers and Tablets",
        "old_price": 60, 
        "current_price": 50, 
        "size": "18 Plus", 
        "featured_photo": "logo.png", 
        "is_featured": "Yes", 
        "is_active": "Yes"
    }]
    
    result = add_product(driver, new_product)
    
    assert result == "Product is added successfully." 

def test_add_product_missing_field(sample_products):
    new_product = [{
        "name": "", 
        "color": "Black", 
        "quantity": 30, 
        "top_level_category": "Electronics", 
        "mid_level_category": "Computers", 
        "end_level_category": "Computers and Tablets",
        "old_price": 60, 
        "current_price": 50, 
        "size": "18 Plus", 
        "featured_photo": "logo.png", 
        "is_featured": "Yes", 
        "is_active": "Yes"
    }]
    
    result = add_product(driver, new_product)
    assert result == "Product name can not be empty" 

def test_add_product_invalid_price(driver):
    new_product = [{
        "name": "Test", 
        "color": "Black", 
        "quantity": -30, 
        "top_level_category": "Electronics", 
        "mid_level_category": "Computers", 
        "end_level_category": "Computers and Tablets",
        "old_price": -60, 
        "current_price": -50, 
        "size": "18 Plus", 
        "featured_photo": "logo.png", 
        "is_featured": "Yes", 
        "is_active": "Yes"
    }]
    
    result = add_product(driver, new_product)
    assert result == " Price and quantity must be greater than 0" 

# Test case 2: Sửa thông tin sản phẩm
def test_update_product_valid(driver):
    updated_info = {
        "name": "Game", 
        "old_price": 1000,  
        "current_price": 1200,  
        "size": "20 Plus",  
        "is_featured": "Yes",  
        "is_active": "Yes"
    }

    result = update_product(driver, product_name="test", updated_info=updated_info)

    assert result == "Product updated successfully." 

    product_name_on_page = driver.find_element(By.NAME, "p_name").get_attribute("value")
    old_price_on_page = driver.find_element(By.NAME, "p_old_price").get_attribute("value")
    current_price_on_page = driver.find_element(By.NAME, "p_current_price").get_attribute("value")
    
    assert product_name_on_page == "Game"
    assert old_price_on_page == "1000"
    assert current_price_on_page == "1200"


def test_update_product_duplicate_name(driver):
    updated_info = {"name": "test"}  
    
    result = update_product(driver, product_name="test", updated_info=updated_info)
    
    assert result == "Product name already exists."


def test_update_product_missing_field(driver):
    updated_info = {"current_price": " "}  
    
    result = update_product(driver, product_name="test",  updated_info=updated_info)
    
    assert result == "Price not be empty."


# Test case 3: Xóa sản phẩm
def test_delete_product_valid(driver):
    product_name = "Gaming Laptop"  
    
    result = delete_product(driver, product_name)
    
    assert result == "Product deleted successfully"
    
    try:
        driver.find_element(By.XPATH, f"//tr[td[contains(text(), '{product_name}')]]")
        assert False, "Product not deleted successfully"
    except:
        assert True
