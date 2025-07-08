from playwright.sync_api import sync_playwright

def form_automation_example():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        # Navigate to a demo form site
        print("Going to demo form...")
        page.goto("https://www.saucedemo.com/")
        
        # Fill username
        print("Filling login form...")
        page.fill("#user-name", "standard_user")
        
        # Fill password
        page.fill("#password", "secret_sauce")
        
        # Click login button
        page.click("#login-button")
        
        # Check if we're logged in by looking for inventory
        try:
            page.wait_for_selector(".inventory_list", timeout=5000)
            print("Login successful!")
            
            # Count products
            products = page.locator(".inventory_item").count()
            print(f"Found {products} products on the page")
            
            # Click on first product
            page.click(".inventory_item:first-child .inventory_item_name")
            
            # Get product details
            product_name = page.locator(".inventory_details_name").inner_text()
            product_price = page.locator(".inventory_details_price").inner_text()
            print(f"\nProduct: {product_name}")
            print(f"Price: {product_price}")
            
        except:
            print("Login failed!")
        
        # Close browser
        browser.close()

# Run the function
if __name__ == "__main__":
    form_automation_example()