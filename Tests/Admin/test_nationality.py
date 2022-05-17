import time
from Pages.Admin.nationalities import Nationalities
from ddt import ddt,data,unpack
import unittest,pytest
from utilities.util import get_proj_dir,get_csv_data


@pytest.mark.usefixtures('setup')
@ddt
class NationalityTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.nt = Nationalities(setup)

    @data(*get_csv_data(get_proj_dir() + '/HRM/Tests/Admin/test_nationalities.csv'))
    @unpack
    def test_nationalities(self,nationality):
        self.nt.navigate_to_nationalities()
        self.nt.add_nationality(nationality)
        time.sleep(1)
        self.nt.find_delete_nationality(nationality)