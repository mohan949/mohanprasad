from playwright.sync_api import sync_playwright
import time

def search_amazon_simple():
    # Launch browser
    with sync_playwright() as p:
        # Start browser (set headless=False to see the browser)
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        
        # Create a new page
        page = browser.new_page()
        
        # Navigate to Amazon India
        print("Going to Amazon.in...")
        page.goto("https://www.amazon.in")
        
        # Wait for the page to load
        page.wait_for_load_state("domcontentloaded")
        
        # Find and fill the search box
        print("Searching for 'laptop'...")
        search_box = page.locator("input#twotabsearchtextbox")
        search_box.fill("laptop")
        
        # Click the search button
        search_button = page.locator("input#nav-search-submit-button")
        search_button.click()
        
        # Wait for results to load
        page.wait_for_selector(".s-main-slot")
        print("Search results loaded!")
        
        # Get all product containers
        product_containers = page.locator("div[data-component-type='s-search-result']").all()
        products = []
        
        print(f"\nFound {len(product_containers)} products. Extracting details...")
        
        for i, container in enumerate(product_containers):
            try:
                # Get product name
                name_element = container.locator("h2 span").first
                product_name = name_element.inner_text().strip()
                
                # Get price
                price_element = container.locator("span.a-price-whole").first
                price_text = price_element.inner_text().strip()
                price_text = price_text.replace(",", "")
                price = int(price_text)
                
                products.append({
                    "name": product_name,
                    "price": price
                })
                
                print(f"Product {i+1}: {product_name[:50]}... - ₹{price:,}")
                
            except:
                continue
        
        print(f"\nSuccessfully extracted {len(products)} products with prices")
        
        # Find highest and lowest priced products
        if products:
            highest = max(products, key=lambda x: x['price'])
            lowest = min(products, key=lambda x: x['price'])
            
            print(f"\n{'='*60}")
            print("HIGHEST PRICED PRODUCT:")
            print(f"Name: {highest['name']}")
            print(f"Price: ₹{highest['price']:,}")
            
            print(f"\n{'='*60}")
            print("LOWEST PRICED PRODUCT:")
            print(f"Name: {lowest['name']}")
            print(f"Price: ₹{lowest['price']:,}")
            print(f"{'='*60}")
        else:
            print("No products with prices found!")
        
        # Take a screenshot
        page.screenshot(path="amazon_search_results.png")
        print("\nScreenshot saved as 'amazon_search_results.png'")
        
        # Close browser
        browser.close()

# Run the function
if __name__ == "__main__":
    search_amazon_simple()