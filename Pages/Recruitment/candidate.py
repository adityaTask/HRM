from base.selenium_driver import SeleniumDriver
from base.locators import Locators
from base.common import Common


class Candidate(SeleniumDriver):
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators
        self.common = Common(driver)
        self.select_recruitment_by_id = 'menu_recruitment_viewRecruitmentModule'
        self.add_first_name_by_id = 'addCandidate_firstName'
        self.add_last_name_by_id = 'addCandidate_lastName'
        self.add_email_by_id = 'addCandidate_email'
        self.select_vacancy_by_id = 'addCandidate_vacancy'
        self.delete_dialog_by_id = 'dialogDeleteBtn'

    def navigate_to_recruitment(self):
        self.element_click(self.select_recruitment_by_id)

    def add_candidate(self, first_name, last_name, email, vacancy='Associate IT Manager'):
        self.element_click(self.locators.add_button_by_id)
        self.send_keys(first_name, self.add_first_name_by_id)
        self.send_keys(last_name, self.add_last_name_by_id)
        self.send_keys(email, self.add_email_by_id)
        self.select_from_dropdown(vacancy, self.select_vacancy_by_id)
        self.element_click(self.locators.save_button_by_id)
        self.element_click(self.locators.back_button_by_id)

    def find_delete_candidate(self, name):
        self.common.find_and_check_row_in_table(column_name='Candidate', value=name)
        self.element_click(self.locators.delete_button_by_id)
        self.element_click(self.locators.dialog_del_button_by_id)


