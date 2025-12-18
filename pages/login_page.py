# from  playwright.sync_api import Page
# class loginPage:
#     def __init__(self,page:Page):
#         self.page = page
#         self.userName = page.get_by_role("textbox", name="Username")
#         self.password = page.get_by_role("textbox", name="Password")
#         self.loginButton = page.get_by_role("button", name="Login")
      
#     def loadPage(self):
#         self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  
      
#     def login(self, username:str, password:str):
#         self.userName.fill(username)
#         self.password.fill(password)
#         self.loginButton.click()
        
        
# from playwright.sync_api import Page, expect
# from locators.login_locators import LoginLocators

# class LoginPage:
#     def __init__(self, page: Page):
#         self.page = page

#         self.username_input = page.locator(LoginLocators.USERNAME)
#         self.password_input = page.locator(LoginLocators.PASSWORD)
#         self.login_button = page.locator(LoginLocators.LOGIN_BUTTON)
#         self.error_alert = page.locator(LoginLocators.ERROR_ALERT)
#         self.dashboard_link = page.locator(LoginLocators.DASHBOARD_LINK)

#     def load(self, base_url: str):
#         self.page.goto(f"{base_url}/web/index.php/auth/login")
#         expect(self.username_input).to_be_visible()

#     def login(self, username: str, password: str):
#         self.username_input.fill(username)
#         self.password_input.fill(password)
#         self.login_button.click()

#     def expect_login_success(self):
#         expect(self.dashboard_link).to_be_visible()

#     def expect_login_failure(self):
#         expect(self.error_alert).to_contain_text("Invalid credentials")



from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username = page.locator(LoginLocators.USERNAME)
        self.password = page.locator(LoginLocators.PASSWORD)
        self.login_button = page.locator(LoginLocators.LOGIN_BUTTON)
        self.error_message = page.locator(LoginLocators.ERROR_MESSAGE)

    def load(self, base_url):
        self.page.goto(f"{base_url}/web/index.php/auth/login")
        self.wait_for_page_load()

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        self.wait_for_page_load()

    def is_login_failed(self):
        """Wait for invalid login error"""
        try:
            self.error_message.wait_for(state="visible", timeout=8000)
            return True
        except Exception:
            return False
