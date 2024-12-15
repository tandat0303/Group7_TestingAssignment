from functions.login import *
from driver import * 
from functions.update_pass import *

def test_update_password_success(driver):
    # Đăng nhập vào tài khoản
    login(driver, "testuser1@example.com", "Password123")

    # Cập nhật mật khẩu mới
    update_password(driver, "NewPassword123", "NewPassword123")
    
    # Kiểm tra xem có thông báo thành công không (ví dụ: "Password updated successfully")
    assert "Password is updated successfully." in driver.page_source


def test_update_password_mismatch(driver):
    # Đăng nhập vào tài khoản
    login(driver, "testuser1@example.com", "NewPassword123")

    # Cập nhật mật khẩu mới với mật khẩu và xác nhận mật khẩu không khớp
    update_password(driver, "NewPassword123", "DifferentPassword123")
    
    # Kiểm tra thông báo lỗi về việc mật khẩu không khớp
    assert "Passwords do not match." in driver.page_source

def test_update_password_short(driver):
    # Đăng nhập vào tài khoản
    login(driver, "testuser1@example.com", "NewPassword123")

    # Cập nhật mật khẩu mới với độ dài quá ngắn
    update_password(driver, "short", "short")
    
    # Kiểm tra thông báo lỗi về mật khẩu không hợp lệ (ví dụ: "Password is too short")
    assert "Password is too short." in driver.page_source

def test_update_password_empty_fields(driver):
    # Đăng nhập vào tài khoản

    login(driver, "testuser1@example.com", "short")

    # Cập nhật mật khẩu mà không điền gì vào trường mật khẩu
    update_password(driver, "", "")
    
    # Kiểm tra thông báo lỗi về việc mật khẩu không được để trống
    assert "Password can't be empty." in driver.page_source

def test_update_password_same_as_old(driver):
    # Đăng nhập vào tài khoản
    login(driver, "testuser1@example.com", "short")

    # Cập nhật mật khẩu mới giống mật khẩu cũ
    update_password(driver, "short", "short")
    
    # Kiểm tra thông báo lỗi về việc mật khẩu mới giống mật khẩu cũ
    assert "New password cannot be the same as old password." in driver.page_source

