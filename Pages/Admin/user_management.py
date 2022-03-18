import time
from base.common import Common
from base.selenium_driver import SeleniumDriver
from base.locators import Locators


class UserManagement(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.common = Common(driver)
        self.locators = Locators
        self.navigate_to_admin_by_id = 'menu_admin_viewAdminModule'
        self.navigate_to_admin_by_linktext = 'Admin'
        self.navigate_to_user_management_by_id = 'menu_admin_UserManagement'
        self.navigate_to_users_by_id = "menu_admin_viewSystemUsers"
        self.select_user_role_by_id = "systemUser_userType"
        self.employee_name_by_id = "systemUser_employeeName_empName"
        self.username_by_id = "systemUser_userName"
        self.select_user_status_by_id = "systemUser_status"
        self.password_by_id = "systemUser_password"
        self.confirm_password_by_id = "systemUser_confirmPassword"
        self.delete_by_id = "btnDelete"
        self.delete_dialog_by_id = "dialogDeleteBtn"

    def navigate_to_users(self):
        self.element_click(self.navigate_to_admin_by_id)
        self.mouse_hovering(self.navigate_to_user_management_by_id)
        self.element_click(self.navigate_to_users_by_id)

    def add_users(self, role, emp_name, username, status, password):
        self.element_click(self.locators.add_button_by_id)
        self.select_from_dropdown(role, self.select_user_role_by_id)
        self.send_keys(emp_name, self.employee_name_by_id)
        self.send_keys(username, self.username_by_id)
        self.select_from_dropdown(status, self.select_user_status_by_id)
        self.send_keys(password, self.password_by_id)
        self.send_keys(password, self.confirm_password_by_id)
        time.sleep(2)
        self.element_click(self.locators.save_button_by_id)

    def find_delete_user(self, username):
        self.common.find_and_check_row_in_table(column_name='Username', value=username)
        self.element_click(self.locators.delete_button_by_id)
        self.element_click(self.locators.dialog_del_button_by_id)
