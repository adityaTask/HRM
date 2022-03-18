import time

from base.selenium_driver import SeleniumDriver
from base.locators import Locators
from base.common import Common

class Vacancies(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = Locators()
        self.common = Common(driver)
        self.driver = driver
        self.select_recruitment_by_id = 'menu_recruitment_viewRecruitmentModule'
        self.select_vacancies_by_id = 'menu_recruitment_viewJobVacancy'
        self.select_job_title_dropdown_by_id = "addJobVacancy_jobTitle"
        self.vacancy_name_by_id = 'addJobVacancy_name'
        self.hiring_manager_by_id = 'addJobVacancy_hiringManager'
        self.number_of_positions_by_id = 'addJobVacancy_noOfPositions'
        self.vacancy_desc_by_id = 'addJobVacancy_description'
        self.vacancy_table_by_xpath = '//tbody//tr'

    def navigate_to_vacancies(self):
        self.element_click(self.select_recruitment_by_id)
        self.element_click(self.select_vacancies_by_id)

    def add_vacancies(self,job_title,vacancy_name,hiring_manager,positions='',description=''):
        self.element_click(self.locators.add_button_by_id)
        self.select_from_dropdown(job_title,self.select_job_title_dropdown_by_id)
        self.send_keys(vacancy_name,self.vacancy_name_by_id)
        self.send_keys(hiring_manager,self.hiring_manager_by_id)
        self.send_keys(positions,self.number_of_positions_by_id)
        self.send_keys(description,self.vacancy_desc_by_id)
        self.element_click(self.locators.save_button_by_id)
        self.element_click(self.locators.back_button_by_id)

    def find_delete_vacancy(self, vacancy_name):
        self.common.find_and_check_row_in_table(column_name='Vacancy',value=vacancy_name)
        self.element_click(self.locators.delete_button_by_id)
        self.element_click(self.locators.dialog_del_button_by_id)


