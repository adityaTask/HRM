import unittest
from Pages.performance import Performance
import pytest
from ddt import ddt, data, unpack


@ddt
@pytest.mark.usefixtures('setup')
class PerformanceTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.pf = Performance(setup)

    @pytest.mark.run(order=5)
    @data(('Test', 'Positive', 'Positive Comment added'), ('Test', 'Negative', 'Negative Comment added'))
    @unpack
    def test_add_mytracker(self, log, achievment, comment):
        self.pf.navigate_to_my_trackers()
        self.pf.add_tracker(log, achievment, comment)
