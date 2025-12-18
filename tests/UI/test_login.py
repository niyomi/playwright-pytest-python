# import pytest
# from pages.login_page import loginPage
# from playwright.sync_api import Page, expect

# def get_json_data() -> list:
#     import json
#     with open('./test_data/login_creds.json', "r") as jsonfile:
#         data = json.load(jsonfile)
#     return [(item['username'], item['password']) for item in data]

# @pytest.mark.parametrize("username,password", get_json_data())
# def test_login(page: Page,username,password) -> None:
#     login_page = loginPage(page)
#     login_page.loadPage()
#     login_page.login(username,password)
#     if "InvalidUser" in username or "WrongUser" in username:
#        expect(page.get_by_role("alert")).to_contain_text("Invalid credentials")
#     else:
#         expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
   
import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_login_data
from pages.dashboard_page import DashboardPage

test_data = load_login_data()

@pytest.mark.parametrize(
    "username,password,expected",
    [(d["username"], d["password"], d["expected"]) for d in test_data]
)
def test_login(page, base_url, username, password, expected):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.load(base_url)
    login_page.login(username, password)

    if expected == "success":
        assert dashboard_page.is_loaded()
    else:
        assert login_page.is_login_failed()