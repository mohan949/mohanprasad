# test_example.py
from playwright.sync_api import sync_playwright

def test_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://hugo-boss-uat.fynd.io/")
        assert page.title() == "hugo-boss-uat"
        # Verify head banner
        banner = page.locator("div.bg-white.h-\[42px\].flex-center")
        banner.wait_for(state="visible")
        text = banner.inner_text().strip()
        print(text)
        assert text == "Sale - Up to 40% off: Shop Now"
        browser.close()
