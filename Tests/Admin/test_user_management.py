import datetime
import time

from Pages.Admin.user_management import UserManagement
import pytest,unittest
from ddt import ddt,data,unpack

@ddt
@pytest.mark.usefixtures("setup")
class UserTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.um = UserManagement(setup)

    now = datetime.datetime.now()
    @data(['ESS','Orange Test','zorange'+str(now.hour)+str(now.min),'Enabled','orange123'])
    @unpack
    def test_user(self,role, emp_name, username, status, password):
        self.um.navigate_to_users()
        self.um.add_users(role,emp_name,username,status,password)
        self.um.find_delete_user(username)