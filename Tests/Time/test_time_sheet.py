from Pages.Time.time_sheet import TimeSheet
import pytest
import unittest
from ddt import data,unpack,ddt


@pytest.mark.usefixtures('setup')
@ddt
class TimeSheetTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,setup):
        self.ts = TimeSheet(setup)

    @data(['orange test','Fresh Books Software Ltd - Fresh Books Software Ltd - Phase I','Bug Fixes'])
    @unpack
    def test_time_sheet_submit(self,user,project_name,activity):
        self.ts.navigate_to_time_sheets()
        self.ts.search_employee_view(user)
        self.ts.add_time_sheet()
        self.ts.add_time_sheet_info(project_name,activity)
        result = self.ts.get_time_sheet_status()
        print(result)
        assert 'Submitted' in result



