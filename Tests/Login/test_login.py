from Pages.Login.login import LoginPage
import pytest
import unittest
from ddt import data, unpack, ddt
from utilities.util import get_csv_data
from utilities.util import get_proj_dir


@pytest.mark.usefixtures('setup',)
@ddt
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.lp = LoginPage(setup)

    @data(*get_csv_data(get_proj_dir() + '/HRM/Tests/Login/test_valid_user.csv'))
    @unpack
    @pytest.mark.run(order=2)
    def test_valid_login(self, username, password):
        self.lp.logout()
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
