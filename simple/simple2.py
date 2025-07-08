from playwright.sync_api import sync_playwright

def search_amazon_simple():
    # Start Playwright
    with sync_playwright() as p:
        # Launch browser (headless=False so you can see it)
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # Go to Amazon India
        print("Opening Amazon.in...")
        page.goto("https://www.amazon.in")

        # Wait until the page loads
        page.wait_for_load_state("domcontentloaded")

        # Type "laptop" in the search box
        print("Typing 'laptop' in the search box...")
        page.fill("input#twotabsearchtextbox", "laptop")

        # Click the search button
        print("Clicking search...")
        page.click("input#nav-search-submit-button")

        # Wait for results to load
        page.wait_for_selector(".s-main-slot")
        print("Results loaded!")

        # Find prices (first 10)
        prices = []
        print("Extracting prices...")
        price_elements = page.query_selector_all("span.a-price-whole")
        for i, price_el in enumerate(price_elements[:10]):
            price_text = price_el.inner_text().replace(",", "").strip()
            if price_text.isdigit():
                prices.append(int(price_text))
                print(f"Product {i+1}: ₹{price_text}")

        # Show highest and lowest prices
        if prices:
            print(f"Highest price: ₹{max(prices)}")
            print(f"Lowest price: ₹{min(prices)}")
        else:
            print("No prices found!")

        # Take a screenshot
        page.screenshot(path="amazon_search_results.png")
        print("Screenshot saved as 'amazon_search_results.png'")

        # Close browser
        browser.close()

if __name__ == "__main__":
    search_amazon_simple()
