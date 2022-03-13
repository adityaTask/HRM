# import unittest
# from Tests.test_login import LoginTest
# from Tests.test_recruitment import RecruitmentTest
# from Tests.test_time_sheet import TimeSheetTest
#
# #get all tests from the test classes
#
# tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(RecruitmentTest)
# tc3 = unittest.TestLoader().loadTestsFromTestCase(TimeSheetTest)
#
#
# #create test suite
#
# smokeTest = unittest.TestSuite([tc1,tc2,tc3])
#
# unittest.TextTestRunner(verbosity=2).run(smokeTest)