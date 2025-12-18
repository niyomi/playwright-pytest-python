class ApplyLeaveLocators:
    # Page identity
    PAGE_HEADER = "h6:has-text('Apply Leave')"
    NO_LEAVE_MESSAGE = "p:has-text('No Leave Types with Leave Balance')"

    # Form elements (may or may not exist depending on leave balance)
    LEAVE_TYPE = ".oxd-select-text"
    FROM_DATE = "input[placeholder='From Date']"
    TO_DATE = "input[placeholder='To Date']"
    COMMENT = "textarea"
    SUBMIT = "button:has-text('Apply')"

    # Toast
    SUCCESS_TOAST = ".oxd-toast--success"
