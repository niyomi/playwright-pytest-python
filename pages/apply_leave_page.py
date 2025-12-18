from pages.base_page import BasePage
from locators.apply_leave_locators import ApplyLeaveLocators

class ApplyLeavePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        # Page identity
        self.page_header = page.locator(ApplyLeaveLocators.PAGE_HEADER)
        self.no_leave_message = page.locator(ApplyLeaveLocators.NO_LEAVE_MESSAGE)
        
        # Toast
        self.success_toast = page.locator(ApplyLeaveLocators.SUCCESS_TOAST)

    def is_loaded(self):
        """Validate page identity only"""
        try:
            self.page.wait_for_url("**/applyLeave**", timeout=8000)
            self.wait_until_visible(self.page_header, timeout=8000)
            return True
        except Exception:
            return False

    def has_leave_balance(self):
        """Business condition check"""
        return not self.no_leave_message.is_visible()
    
    def apply_leave(self, leave_type, from_date, to_date, comment):
        self.leave_type.click()
        self.page.get_by_text(leave_type).click()

        self.from_date.fill(from_date)
        self.to_date.fill(to_date)
        self.comment.fill(comment)
        self.submit.click()

    def is_leave_applied(self):
        return self.success_toast.is_visible()
