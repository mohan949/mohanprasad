from playwright.sync_api import sync_playwright

def search_amazon_simple():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Go to Amazon
        page.goto("https://www.amazon.in")
        page.wait_for_load_state("domcontentloaded")
        
        # Search for laptop
        page.fill("input#twotabsearchtextbox", "laptop")
        page.click("input#nav-search-submit-button")
        page.wait_for_selector(".s-main-slot")
        
        # Get all products
        products = []
        containers = page.locator("div[data-component-type='s-search-result']").all()
        
        for container in containers:
            try:
                name = container.locator("h2 span").first.inner_text().strip()
                price_text = container.locator("span.a-price-whole").first.inner_text().strip()
                price = int(price_text.replace(",", ""))
                products.append({"name": name, "price": price})
            except:
                pass
        
        # Find highest and lowest
        if products:
            highest = max(products, key=lambda x: x['price'])
            lowest = min(products, key=lambda x: x['price'])
            
            print(f"\nHIGHEST PRICE: ₹{highest['price']:,}")
            print(f"PRODUCT: {highest['name']}")
            print(f"\nLOWEST PRICE: ₹{lowest['price']:,}")
            print(f"PRODUCT: {lowest['name']}")
        
        # Close browser
        browser.close()

# Run it
if __name__ == "__main__":
    search_amazon_simple()