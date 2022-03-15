import unittest
import pytest
from Pages.Directory.directory import Directory
from ddt import ddt,data,unpack


@pytest.mark.usefixtures("setup")
@ddt
class DirectoryTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.dr = Directory(setup)


    @data(['Orange Test'],['Admin A'])
    @unpack
    def test_search_directory(self,emp_name):
        self.dr.navigate_to_directory()
        self.dr.search_directory(emp_name)
        assert emp_name == self.dr.verify_user_search()
