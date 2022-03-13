import time
from Pages.login import LoginPage
from base.web_driver import WebDriver
from configs.config_parser import ConfigParser

from base.selenium_driver import SeleniumDriver


class Recruitment(SeleniumDriver):
    def __init__(self, driver):
        self.driver = driver
        self.select_recruitment_by_id = 'menu_recruitment_viewRecruitmentModule'
        self.add_recruitment_by_id = 'btnAdd'
        self.add_first_name_by_id = 'addCandidate_firstName'
        self.add_last_name_by_id = 'addCandidate_lastName'
        self.add_email_by_id = 'addCandidate_email'
        self.save_by_id = 'btnSave'
        self.back_by_id = 'btnBack'
        self.select_vacancy_by_id = 'addCandidate_vacancy'
        self.recruitment_list_by_xpath = '//tbody//tr'
        self.candidate_by_xpath = '//tbody/tr[{0}]/td[3]'
        self.check_candidate_by_xpath = '//tbody/tr[{0}]/td[1]'
        self.delete_by_id = 'btnDelete'
        self.delete_dialog_by_id = 'dialogDeleteBtn'

    def navigate_to_recruitment(self):
        self.element_click(self.select_recruitment_by_id)

    def add_recruitment(self, first_name, last_name, email, vacancy='Associate IT Manager'):
        self.element_click(self.add_recruitment_by_id)
        self.send_keys(first_name, self.add_first_name_by_id)
        self.send_keys(last_name, self.add_last_name_by_id)
        self.send_keys(email, self.add_email_by_id)
        self.select_from_dropdown(vacancy, self.select_vacancy_by_id)
        self.element_click(self.save_by_id)
        self.element_click(self.back_by_id)

    def find_recruitment(self, name):
        recruitment_list = self.find_elements_list(self.recruitment_list_by_xpath, "xpath")
        index = 1
        for i in range(1,len(recruitment_list)+1):
            candidate_name = self.get_text(self.candidate_by_xpath.format(index), "xpath")
            if name == candidate_name:
                return index
            index += 1

    def delete_recruitment(self, name):
        index = self.find_recruitment(name)
        self.element_click(self.check_candidate_by_xpath.format(index), "xpath")
        self.element_click(self.delete_by_id)
        self.element_click(self.delete_dialog_by_id)


