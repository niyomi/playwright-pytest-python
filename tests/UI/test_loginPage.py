from pages.login_page import loginPage
from playwright.sync_api import Page

def test_example(page: Page) -> None:
    login_page = loginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user","secret_sauce")