from Pages.Recruitment import Recruitment
import pytest
import unittest
from ddt import data,unpack,ddt
from utilities.util import get_csv_data


@pytest.mark.usefixtures('setup')
@ddt
class RecruitmentTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.rc = Recruitment(setup)
        setup.implicitly_wait(10)

    @pytest.mark.run(order=3)
    @data(['z','b','a@b.com','Associate IT Manager'])
    @unpack
    def test_recruitment(self,first_name,last_name,email,vacancy):
        self.rc.navigate_to_recruitment()
        self.rc.add_recruitment(first_name,last_name,email,vacancy)
        name = first_name+' '+last_name
        self.rc.delete_recruitment(name)



