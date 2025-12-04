import pytest
from pages.login_page import loginPage
from playwright.sync_api import Page, expect

def get_csv_data() -> list:
    import csv
    data = []
    with open('./test_data/login_data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

@pytest.mark.parametrize("username,password", get_csv_data())
def test_login(page: Page,username,password) -> None:
    login_page = loginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login(username,password)
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()