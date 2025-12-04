from pages.login_page import loginPage
from playwright.sync_api import Page
import pytest

@pytest.mark.parametrize("username,password", [
    ("Admin", "admin123"),
    ("admin123", "admin123")
])
def test_example(page: Page,username,password) -> None:
    login_page = loginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login(username,password)