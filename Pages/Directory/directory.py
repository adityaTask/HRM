from base.selenium_driver import SeleniumDriver


class Directory(SeleniumDriver):
    def __init__(self,driver):
        self.driver = driver
        self.navigate_to_directory_by_id = 'menu_directory_viewDirectory'
        self.search_employee_directory_by_id = 'searchDirectory_emp_name_empName'
        self.search_button_by_id = 'searchBtn'
        self.search_result_emp_name_by_xpath = '//*[@id="resultTable"]//b'


    def navigate_to_directory(self):
        self.element_click(self.navigate_to_directory_by_id)

    def search_directory(self,emp_name):
        self.send_keys(emp_name,self.search_employee_directory_by_id)
        self.element_click(self.search_button_by_id)

    def verify_user_search(self):
        return self.get_text(self.search_result_emp_name_by_xpath,"xpath")