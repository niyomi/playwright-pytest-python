
from playwright.sync_api import Page, expect
def test_apply_leave_insufficient_balance(page: Page) -> None:    
    page.get_by_role("button", name="Apply Leave").click()
    page.get_by_role("textbox", name="Type for hints...").click()
    page.get_by_role("textbox", name="Type for hints...").fill("add")
    page.get_by_role("textbox", name="Type for hints...").press("Enter")
    page.get_by_role("textbox", name="Type for hints...").fill("james")
    page.get_by_role("option", name="James Monroe ${lastName}").click()
    page.get_by_text("-- Select --").click()
    page.get_by_role("option", name="CAN - Personal").click()
    page.get_by_role("textbox", name="yyyy-dd-mm").first.click()
    page.get_by_text("4", exact=True).click()
    expect(page.get_by_text("Balance not sufficient")).to_be_visible()