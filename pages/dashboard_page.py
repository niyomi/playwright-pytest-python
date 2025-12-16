from  playwright.sync_api import Page
class dashboardPage:
    def __init__(self,page:Page):
        self.page = page
        self.dashboardLink = page.get_by_role("link", name="Dashboard")
        self.timeAtWorkCard = page.get_by_text("Time at Work")
        self.myActionsCard = page.get_by_text("My Actions")
        self.quickLaunchCard = page.get_by_text("Quick Launch")
        self.buzzLatestPosts = page.get_by_text("Buzz Latest Posts")
        self.employeesOnLeaveToday = page.get_by_text("Employees on Leave Today")
        # self.employeeDistributionBySubUnitChart = page.locator("div").filter(has_text="Employee Distribution by Sub")
        # self.employeeDistributionByLocationChart = page.locator("div").filter(has_text="Employee Distribution by Location")
        self.clientBrandBanner = page.get_by_role("link", name="client brand banner")
        self.upgradeButton = page.get_by_role("button", name="Upgrade")
        self.userProfileName = page.locator("span").filter(has_text="123TestName user")
