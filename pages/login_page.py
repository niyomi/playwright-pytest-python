from  playwright.sync_api import Page
class loginPage:
    def __init__(self,page:Page):
        self.page = page
        self.userName = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.loginButton = page.locator("[data-test=\"login-button\"]")
   
   #atomic methods, functions per single action
    
    def enter_userName(self,username:str):
        self.userName.fill("standard_user")
        
    def enter_password(self, password:str):
        self.password.fill("secret_sauce")       
        
    def click_login(self):
        self.loginButton.click()
        
   #single method, functions per functionality
    def login(self, username:str, password:str):
        self.userName.fill("standard_user")
        self.password.fill("secret_sauce")
        self.loginButton.click()