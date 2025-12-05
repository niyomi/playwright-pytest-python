import pytest
from pages.login_page import loginPage
from playwright.sync_api import Page, expect

def get_json_data() -> list:
    import json
    with open('./test_data/login_creds.json', "r") as jsonfile:
        data = json.load(jsonfile)
    return [(item['username'], item['password']) for item in data]

@pytest.mark.parametrize("username,password", get_json_data())
def test_login(page: Page,username,password) -> None:
    login_page = loginPage(page)
    login_page.loadPage()
    login_page.login(username,password)
    if "InvalidUser" in username or "WrongUser" in username:
       expect(page.get_by_role("alert")).to_contain_text("Invalid credentials")~
    else:
        expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
    