from Pages.Recruitment.candidate import Candidate
import pytest
import unittest
from ddt import data, unpack, ddt


@pytest.mark.usefixtures('setup')
@ddt
class RecruitmentTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.rc = Candidate(setup)

    @data(['z', 'b', 'a@b.com', 'Associate IT Manager'])
    @unpack
    def test_candidate(self, first_name, last_name, email, vacancy):
        self.rc.navigate_to_recruitment()
        self.rc.add_candidate(first_name, last_name, email, vacancy)
        name = first_name + ' ' + last_name
        self.rc.find_delete_candidate(name)
