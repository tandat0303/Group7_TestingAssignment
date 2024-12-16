# Call all modules and functions in the "driver.py" file
from driver import *
from functions.search import search

# Test the search functionality with valid keyword
@pytest.mark.parametrize("keyword", [("shirt")])
def test_search_found(driver, keyword):
    search(driver, keyword)

    # Finding all products whose title contain the keyword
    product_titles = driver.find_elements(By.TAG_NAME, "h3")

    for title in product_titles:
        assert keyword.lower() in title.text.lower()


# Test the search functionality with notfound keyword
@pytest.mark.parametrize("keyword", [("agz"),("@!#$"),("  shirt"),("shirt  "), ("sh irt")])
def test_search_notfound(driver, keyword):  
    search(driver, keyword)

    # Find the label "No result found"
    notfound_label = driver.find_element(By.TAG_NAME, "span").text

    assert "No result found" in notfound_label


# Test the search functionality with space keyword
@pytest.mark.parametrize("keyword", [(" ")])
def test_search_spaceKW(driver, keyword):
    search(driver, keyword)

    # The website show all products when the user search space keyword
    assert "search_text=+" in driver.current_url

@pytest.mark.parametrize("keyword", [("Women's Plus-Size Shirt Dress with Gold Hardware      ")])
def test_search_space(driver, keyword):
    search(driver, keyword)
    assert  "Women's Plus-Size Shirt Dress with Gold Hardware" in driver.page_source

@pytest.mark.parametrize("keyword", [("             Women's Plus-Size Shirt Dress with Gold Hardware")])
def test_search_space(driver, keyword):
    search(driver, keyword)
    assert  "Women's Plus-Size Shirt Dress with Gold Hardware" in driver.page_source

@pytest.mark.parametrize("keyword", [("Women's Plus-Size          Shirt Dress with Gold Hardware")])
def test_search_space(driver, keyword):
    search(driver, keyword)
    assert  "Women's Plus-Size Shirt Dress with Gold Hardware" in driver.page_source
    
#Test the search functionality with space keyword
@pytest.mark.parametrize("keyword", [("")])
def test_search_emptyKW(driver, keyword):
    search(driver, keyword)

    # Customer is navigated to the homepage
    assert "index.php" in driver.current_url
