import time

from base.selenium_driver import SeleniumDriver


class UserManagement(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navigate_to_admin_by_id = 'menu_admin_viewAdminModule'
        self.navigate_to_admin_by_linktext = 'Admin'
        self.navigate_to_user_management_by_id = 'menu_admin_UserManagement'
        self.navigate_to_users_by_id = "menu_admin_viewSystemUsers"
        self.add_user_by_id = 'btnAdd'
        self.select_user_role_by_id = "systemUser_userType"
        self.employee_name_by_id = "systemUser_employeeName_empName"
        self.username_by_id = "systemUser_userName"
        self.select_user_status_by_id = "systemUser_status"
        self.password_by_id = "systemUser_password"
        self.confirm_password_by_id = "systemUser_confirmPassword"
        self.save_by_id = "btnSave"
        self.users_list_by_xpath = "//tbody//tr"
        self.next_page_by_xpath = "//a[text()='Next']"
        self.username_by_xpath = "//tbody//tr[{0}]//td[2]//a"
        self.check_user_by_xpath = "//tbody//tr[{0}]//td[1]//input"
        self.delete_by_id = "btnDelete"
        self.delete_dialog_by_id = "dialogDeleteBtn"

    def navigate_to_users(self):
        self.element_click(self.navigate_to_admin_by_id)
        self.mouse_hovering(self.navigate_to_user_management_by_id)
        self.element_click(self.navigate_to_users_by_id)

    def add_users(self, role, emp_name, username, status, password):
        self.element_click(self.add_user_by_id)
        self.select_from_dropdown(role, self.select_user_role_by_id)
        self.send_keys(emp_name, self.employee_name_by_id)
        self.send_keys(username, self.username_by_id)
        self.select_from_dropdown(status, self.select_user_status_by_id)
        self.send_keys(password, self.password_by_id)
        self.send_keys(password, self.confirm_password_by_id)
        time.sleep(2)
        self.element_click(self.save_by_id)

    def find_user(self, username):
        while True:
            users_list = self.find_elements_list(self.users_list_by_xpath, "xpath")
            index = 1
            for i in range(1, len(users_list) + 1):
                user_name_from_list = self.get_text(self.username_by_xpath.format(index), "xpath")
                if username == user_name_from_list:
                    return index
                index += 1
            self.element_click(self.next_page_by_xpath, "xpath")

    def delete_user(self, username):
        index = self.find_user(username)
        self.element_click(self.check_user_by_xpath.format(index), "xpath")
        self.element_click(self.delete_by_id)
        self.element_click(self.delete_dialog_by_id)
