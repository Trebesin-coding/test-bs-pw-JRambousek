from playwright.sync_api import sync_playwright
import os

login = "Jarmil"
password = "Admin123"

def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://souhrada.github.io/playwright-exam/")
    
        page.fill("input#login", login)
        page.fill("input#pass", password)
        page.click(".login-btn")
        page.locator(".psst hidden").text_content()

        page.wait_for_timeout(20000)
        browser.close()
    

if __name__ == "__main__":
    main()
