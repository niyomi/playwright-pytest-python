# from  playwright.sync_api import Page
# class dashboardPage:
#     def __init__(self,page:Page):
#         self.page = page
#         self.dashboardLink = page.get_by_role("link", name="Dashboard")
#         self.timeAtWorkCard = page.get_by_text("Time at Work")
#         self.myActionsCard = page.get_by_text("My Actions")
#         self.quickLaunchCard = page.get_by_text("Quick Launch")
#         self.buzzLatestPosts = page.get_by_text("Buzz Latest Posts")
#         self.employeesOnLeaveToday = page.get_by_text("Employees on Leave Today")
#         # self.employeeDistributionBySubUnitChart = page.locator("div").filter(has_text="Employee Distribution by Sub")
#         # self.employeeDistributionByLocationChart = page.locator("div").filter(has_text="Employee Distribution by Location")
#         self.clientBrandBanner = page.get_by_role("link", name="client brand banner")
#         self.upgradeButton = page.get_by_role("button", name="Upgrade")
#         self.userProfileName = page.locator("span").filter(has_text="123TestName user")


from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators

class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.header = page.locator(DashboardLocators.DASHBOARD_HEADER)
        self.user_menu = page.locator(DashboardLocators.USER_MENU)
        self.time_at_work = page.locator(DashboardLocators.TIME_AT_WORK)
        self.my_actions = page.locator(DashboardLocators.MY_ACTIONS)
        self.apply_leave_menu = page.locator(DashboardLocators.APPLY_LEAVE_MENU)
        
    def load(self, base_url):
        self.page.goto(f"{base_url}/web/index.php/dashboard/index")
        self.wait_for_page_load()


    def is_loaded(self):
        """Robust dashboard load check (login + session reuse safe)"""
        try:
            # URL check (soft)
            self.page.wait_for_url("**/dashboard/**", timeout=10000)

            # Hard UI waits (key fix)
            self.header.wait_for(state="visible", timeout=10000)
            self.user_menu.wait_for(state="visible", timeout=10000)

            return True
        except Exception:
            return False

    def verify_widgets(self):
        assert self.time_at_work.is_visible()
        assert self.my_actions.is_visible()
        
    def navigate_to_apply_leave(self):
        self.apply_leave_menu.click()    
        self.page.wait_for_url("**/applyLeave**")
        self.page.wait_for_load_state("networkidle")
