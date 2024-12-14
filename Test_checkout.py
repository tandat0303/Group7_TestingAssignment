# Call all modules and functions in the "driver.py" file
from driver import *
from functions.checkout import checkout

# Test the checkout process, using "Bank Deposit" payment method
@pytest.mark.parametrize(
    "email, password, products, payment_method",
    [
        (
            "ls17189a3.11@gmail.com", 
            123456, 
            [
                {"name": "Men's Soft Classic Sneaker",
                 "color": "Coffee",
                 "quantity": 2},
                {"name": "Truck Boys Pajamas Toddler Sleepwear Clothes",
                 "color": "Blue",
                 "quantity": 3},
                {"name": "Digital Infrared Thermometer for Adults and Kids",
                 "color": "White",
                 "quantity": 4}
            ],
            "Bank Deposit"
        )
    ]
)
def test_bankDeposit_payment(driver, email, password, products, payment_method):
    checkout(driver, email, password, products, payment_method)
    
    driver.find_element(By.NAME, "transaction_info").send_keys("Please deliver it quickly and carefully!")
    time.sleep(2)

    # Click "Pay now"
    driver.find_element(By.NAME, "form3").click()
    time.sleep(2)

    success_message = driver.find_element(By.CSS_SELECTOR, "h3").text

    assert "Congratulation! Payment is successful." in success_message
    

# Test the checkout process, using "Paypal" payment method
@pytest.mark.parametrize(
    "email, password, products, payment_method",
    [
        (
            "ls17189a3.11@gmail.com", 
            123456, 
            [
                {"name": "Men's Soft Classic Sneaker",
                 "color": "Coffee",
                 "quantity": 2},
                {"name": "Truck Boys Pajamas Toddler Sleepwear Clothes",
                 "color": "Blue",
                 "quantity": 3},
                {"name": "Digital Infrared Thermometer for Adults and Kids",
                 "color": "White",
                 "quantity": 4}
            ],
            "PayPal"
        )
    ]
)
def test_Paypal_payment(driver, email, password, products, payment_method):
    checkout(driver, email, password, products, payment_method)

    # Click "Pay now"
    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

    assert "https://www.paypal.com/webapps/shoppingcart/error?flowlogging_id=f7930417dd231&code=GENERIC_ERROR&mfid=1730703263286_f7930417dd231" in driver.current_url
