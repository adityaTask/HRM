import unittest
import pytest
from ddt import ddt, data, unpack
from Pages.Recruitment.vacancies import Vacancies


@pytest.mark.usefixtures('setup')
@ddt
class VacanciesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.vc = Vacancies(setup)

    @data(['Automation Tester','Z','Orange Test',10,'test desc'])
    @unpack
    def test_vacancies(self,job_title,vacancy_name,hiring_manager,positions,description):
        self.vc.navigate_to_vacancies()
        self.vc.add_vacancies(job_title,vacancy_name,hiring_manager,positions,description)
        self.vc.find_delete_vacancy(vacancy_name)