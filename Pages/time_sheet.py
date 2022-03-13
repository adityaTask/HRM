import time
from Pages.login import LoginPage
from base.web_driver import WebDriver
from configs.config_parser import ConfigParser

from base.selenium_driver import SeleniumDriver

class TimeSheet(SeleniumDriver):
    def __init__(self,driver):
        self.driver = driver
        self.select_time_by_id = 'menu_time_viewTimeModule'
        self.search_employee_by_id = 'employee'
        self.select_shortlisted_user_by_class = 'ac_even ac_over'
        self.select_view_by_id = 'btnView'
        self.add_time_sheet_by_id = 'btnAddTimesheet'
        self.select_date_picker_by_class = 'ui-datepicker-trigger'
        self.select_todays_date_by_class = 'ui-state-default ui-state-highlight ui-state-active'
        self.select_time_sheet_edit_button_by_id = 'btnEdit'
        self.add_project_by_id = 'initialRows_0_projectName'
        self.select_activity_by_class = 'projectActivity'
        self.save_time_sheet_by_id = 'submitSave'
        self.get_time_sheet_status_by_xpath = '//*[@id="timesheet_status"]/h2'

        self.click_ok_button_by_id = 'addTimesheetBtn'
        self.duplicate_time_sheet_message_by_id = 'msgDiv'
        self.submit_button_by_id = 'btnSubmit'
        self.action_status_by_id = 'actionlogStatus'

    def navigate_to_time_sheets(self):
        self.element_click(self.select_time_by_id)

    def search_employee_view(self,emp_name):
        self.send_keys(emp_name,self.search_employee_by_id)
        self.element_click(self.select_shortlisted_user_by_class,"class")
        self.element_click(self.select_view_by_id)

    def add_time_sheet(self):
        self.element_click(self.add_time_sheet_by_id)
        self.element_click(self.select_date_picker_by_class,"class")
        self.element_click(self.select_todays_date_by_class,"class")
        time.sleep(1)
        self.element_click(self.select_time_sheet_edit_button_by_id)

    def add_time_sheet_info(self,project_name,activity):
        self.send_keys(project_name,self.add_project_by_id)
        time.sleep(0.5)
        self.element_click(self.select_shortlisted_user_by_class,"class")
        self.select_from_dropdown(activity,self.select_activity_by_class,"class")
        time.sleep(1)
        self.element_click(self.save_time_sheet_by_id)

    def get_time_sheet_status(self):
        time.sleep(2)
        return self.get_text(self.get_time_sheet_status_by_xpath,"xpath")



if __name__ == '__main__':
    def test_time_sheet_submit():
        config = ConfigParser()
        wd = WebDriver(url=config.get_url())
        driver = wd.create_driver_instance()
        lp = LoginPage(driver)
        lp.login(username=config.get_username(), password=config.get_password())
        ts = TimeSheet(driver)
        ts.navigate_to_time_sheets()
        ts.search_employee_view(emp_name='orange test')
        ts.add_time_sheet()
        ts.add_time_sheet_info(project_name='Fresh Books Software Ltd - Fresh Books Software Ltd - Phase I',activity='Bug Fixes')
    test_time_sheet_submit()



