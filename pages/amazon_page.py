from playwright.sync_api import Page

class AmazonPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.amazon.in")
        # Wait for the page to load
        self.page.wait_for_load_state("domcontentloaded")

    def search(self, product_name):
        # Wait for search box to be ready
        self.page.wait_for_selector("input#twotabsearchtextbox", state="visible")
        self.page.fill("input#twotabsearchtextbox", product_name)
        self.page.click("input#nav-search-submit-button")
        # Wait for results to load
        self.page.wait_for_selector(".s-main-slot", state="visible")

    def get_all_prices(self):
        # Get a list of prices from the search results
        price_els = self.page.query_selector_all("span.a-price-whole")
        prices = []
        for price_el in price_els:
            try:
                price_text = price_el.inner_text().strip()
                # Remove commas
                price_text = price_text.replace(",", "")
                price = int(price_text)
                prices.append(price)
            except Exception:
                continue
        return prices

    def get_highest_and_lowest_price(self):
        prices = self.get_all_prices()
        if not prices:
            return None, None
        return max(prices), min(prices)