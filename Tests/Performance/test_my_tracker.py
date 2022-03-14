import unittest
from Pages.Performance.my_tracker import MyTracker
import pytest
from ddt import ddt, data, unpack


@ddt
@pytest.mark.usefixtures('setup')
class MyTrackerTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.pf = MyTracker(setup)

    @data(('Test', 'Positive', 'Positive Comment added'), ('Test', 'Negative', 'Negative Comment added'))
    @unpack
    def test_add_my_tracker(self, log, achievment, comment):
        self.pf.navigate_to_my_trackers()
        self.pf.add_tracker(log, achievment, comment)
