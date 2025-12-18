import pytest
from pages.dashboard_page import DashboardPage
from pages.apply_leave_page import ApplyLeavePage

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_apply_leave_flow(auth_page, base_url):

    dashboard = DashboardPage(auth_page)
    apply_leave = ApplyLeavePage(auth_page)

    # Start from dashboard (already authenticated)
    dashboard.load(base_url)
    assert dashboard.is_loaded()
    dashboard.verify_widgets()

    # Navigate to Apply Leave
    dashboard.navigate_to_apply_leave()
    assert "applyLeave" in auth_page.url
    assert apply_leave.is_loaded()
    assert apply_leave.no_leave_message.is_visible(), \
        "Expected 'No Leave Types with Leave Balance' message not shown"    

    # apply_leave.apply_leave(
    #     leave_type="CAN - FMLA",
    #     from_date="2025-12-20",
    #     to_date="2025-12-21",
    #     comment="Family function"
    # )

    # assert apply_leave.is_leave_applied()
