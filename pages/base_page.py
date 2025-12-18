from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    def wait_until_visible(self, locator, timeout=5000):
        locator.wait_for(state="visible", timeout=timeout)
