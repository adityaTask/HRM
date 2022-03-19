from base.common import Common
from base.selenium_driver import SeleniumDriver
from base.locators import Locators

class Employee(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = Locators
        self.common = Common(driver)
        self.pim_by_id = 'menu_pim_viewPimModule'
        self.employee_list_by_id = 'menu_pim_viewEmployeeList'
        self.first_name_by_id = 'firstName'
        self.last_name_by_id = 'lastName'
        self.employee_id_by_id = 'employeeId'
        self.attribute_of_emp_id = 'value'

    def navigate_to_employee(self):
        self.element_click(self.pim_by_id)
        self.element_click(self.employee_list_by_id)

    def add_employee(self,first_name,last_name):
        self.element_click(self.locators.add_button_by_id)
        self.send_keys(first_name,self.first_name_by_id)
        self.send_keys(last_name,self.last_name_by_id)
        emp_id = self.get_attribute(self.attribute_of_emp_id,self.employee_id_by_id)
        self.element_click(self.locators.save_button_by_id)
        self.element_click(self.employee_list_by_id)
        return emp_id

    def find_delete_employee(self,emp_id):
        self.common.find_and_check_row_in_table(column_name='Id',value=emp_id)
        self.element_click(self.locators.delete_button_by_id)
        self.element_click(self.locators.dialog_del_button_by_id)

