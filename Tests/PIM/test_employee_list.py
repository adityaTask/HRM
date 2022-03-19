from Pages.PIM.employee import Employee
import pytest
import unittest
from ddt import data, unpack, ddt


@pytest.mark.usefixtures('setup')
@ddt
class RecruitmentTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.el = Employee(setup)

    @data(['aa', 'a'])
    @unpack
    def test_employee(self, first_name, last_name):
        self.el.navigate_to_employee()
        emp_id = self.el.add_employee(first_name,last_name)
        self.el.find_delete_employee(emp_id)
