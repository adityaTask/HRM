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


    @data(['ESS','Orange Test','orange' + str(time.time()),'Enabled','orange123'])
    @unpack
    def test_user(self,role, emp_name, username, status, password):
        self.um.navigate_to_users()
        self.um.add_users(role,emp_name,username,status,password)
        self.um.delete_user(username)