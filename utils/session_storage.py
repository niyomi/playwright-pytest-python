from playwright.sync_api import sync_playwright
 

def save_login_session(context):
    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")

    page.wait_for_url("**/dashboard**")

    context.storage_state(path="auth.json")
    page.close()