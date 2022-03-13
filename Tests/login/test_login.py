import os

from Pages.login import LoginPage
import pytest
import unittest
from ddt import data,unpack,ddt
from utilities.util import get_csv_data
from utilities.util import get_proj_dir



@pytest.mark.usefixtures('setup')
@ddt
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.lp = LoginPage(setup)
        # setup.implicitly_wait(10)

    @pytest.mark.run(order=2)
    @data(*get_csv_data(get_proj_dir() + '\\HRM\\Tests\\login\\test_valid_user.csv'))
    @unpack
    def test_valid_login(self,username,password):
        #self.lp.logout()
        self.lp.enter_user_name(username)
        self.lp.enter_password(password)
        self.lp.click_login_button()
        assert self.lp.check_valid_login()


    @pytest.mark.run(order=1)
    def test_invalid_login(self, username="Admin1", password='admin123'):
        self.lp.logout()
        self.lp.enter_user_name(username)
        self.lp.enter_password(password)
        self.lp.click_login_button()
        assert self.lp.check_invalid_login()

