from base.selenium_driver import SeleniumDriver
from base.common import Common
from base.locators import Locators

class Nationalities(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.common = Common(driver)
        self.locators = Locators
        self.admin_by_id = 'menu_admin_viewAdminModule'
        self.nationalities_by_id = 'menu_admin_nationality'
        self.nationality_name_by_id = 'nationality_name'

    def navigate_to_nationalities(self):
        self.element_click(self.admin_by_id)
        self.element_click(self.nationalities_by_id)

    def add_nationality(self,nationality):
        self.element_click(self.locators.add_button_by_id)
        self.send_keys(nationality,self.nationality_name_by_id)
        self.element_click(self.locators.save_button_by_id)

    def find_delete_nationality(self,nationality):
        self.common.find_and_check_row_in_table(column_name='Nationality',value=nationality)
        self.element_click(self.locators.delete_button_by_id)
        self.element_click(self.locators.dialog_del_button_by_id)

