import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.amazon_page import AmazonPage

scenarios("../features/amazon_search.feature")

@pytest.fixture
def amazon_page(page):
    return AmazonPage(page)

@given("I am on the Amazon India homepage")
def go_to_amazon_home(amazon_page):
    amazon_page.goto()

@when(parsers.parse('I search for "{product_name}"'))
def search_for_product(amazon_page, product_name):
    amazon_page.search(product_name)

@then("I list the product with the highest price")
def list_highest_price(amazon_page):
    highest, _ = amazon_page.get_highest_and_lowest_price()
    if highest is not None:
        print(f"Highest price: ₹{highest:,}")
    else:
        print("No prices found")

@then("I list the product with the lowest price")
def list_lowest_price(amazon_page):
    _, lowest = amazon_page.get_highest_and_lowest_price()
    if lowest is not None:
        print(f"Lowest price: ₹{lowest:,}")
    else:
        print("No prices found")