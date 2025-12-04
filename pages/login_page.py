from  playwright.sync_api import Page
class loginPage:
    def __init__(self,page:Page):
        self.page = page
        self.userName = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.loginButton = page.get_by_role("button", name="Login")
      
    def login(self, username:str, password:str):
        self.userName.fill(username)
        self.password.fill(password)
        self.loginButton.click()