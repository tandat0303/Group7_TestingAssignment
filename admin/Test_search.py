from driver import *
from functions.search import search
from functions.login import login

# Test the search functionality with valid keyword
@pytest.mark.parametrize("email, password, keyword",
                         [("admin@mail.com", "Password@123", "shirt")])
def test_search_found(driver, email, password, keyword):
    login(driver, email, password)

    driver.find_element(By.LINK_TEXT, "Product Management").click()

    search(driver, keyword)

    table = driver.find_element(By.CLASS_NAME, "table")

    # Go through all the rows in the cart table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Go through each column in each row
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

    products = []

    if len(columns) > 1:
        product_name_in_cart = columns[2].text

        products.append(product_name_in_cart)

    for product in products:
        assert keyword.lower() in product.lower()


# Test the search functionality with notfound keyword
@pytest.mark.parametrize("email, password, keyword",
                         [("admin@mail.com", "Password@123", "agz"),
                          ("admin@mail.com", "Password@123", "@!#$")])
def test_search_notfound(driver, email, password, keyword):  
    login(driver, email, password)

    driver.find_element(By.LINK_TEXT, "Product Management").click()

    search(driver, keyword)

    assert "No matching records found" in driver.page_source


# Test the search functionality with space keyword
@pytest.mark.parametrize("email, password, keyword",
                         [("admin@mail.com", "Password@123", " "),
                          ("admin@mail.com", "Password@123", "  shirt"),
                          ("admin@mail.com", "Password@123", "shirt  "),
                          ("admin@mail.com", "Password@123", "sh irt")])
def test_search_spaceKW(driver, email, password, keyword):
    login(driver, email, password)

    driver.find_element(By.LINK_TEXT, "Product Management").click()

    search(driver, keyword)

    table = driver.find_element(By.CLASS_NAME, "table")

    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

    if len(columns) > 1:
        assert True