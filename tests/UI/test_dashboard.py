from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage

# def test_verify_dashboard_elements(auth_page) -> None:
#     auth_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
#     expect(auth_page.get_by_role("link", name="Dashboard")).to_be_visible()
#     expect(auth_page.get_by_text("Time at Work")).to_be_visible()
#     expect(auth_page.get_by_text("My Actions")).to_be_visible()
#     expect(auth_page.get_by_text("Quick Launch")).to_be_visible()
#     expect(auth_page.get_by_text("Buzz Latest Posts")).to_be_visible()
#     expect(auth_page.get_by_text("Employees on Leave Today")).to_be_visible()
#     expect(auth_page.get_by_text("Employee Distribution by Sub")).to_be_visible()
#     expect(auth_page.get_by_text("Employee Distribution by Location")).to_be_visible()
#     expect(auth_page.get_by_role("link", name="client brand banner")).to_be_visible()
#     expect(auth_page.get_by_role("button", name="Upgrade")).to_be_visible() 
#     expect(auth_page.locator(".oxd-userdropdown-tab")).to_be_visible()
    
#     # click on user profile to verify logout option
#     auth_page.locator(".oxd-userdropdown-tab").click()
#     expect(auth_page.get_by_role("menuitem", name="Logout")).to_be_visible()

def test_verify_dashboard_widgets(auth_page, base_url):

    dashboard = DashboardPage(auth_page)

    # Start from dashboard (already authenticated)
    dashboard.load(base_url)
    assert dashboard.is_loaded()
    dashboard.verify_widgets()