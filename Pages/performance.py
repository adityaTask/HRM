from base.selenium_driver import SeleniumDriver

class Performance(SeleniumDriver):
    def __init__(self,driver):
        self.driver = driver
        self.performance_tab_by_id = 'menu__Performance'
        self.my_trackers_by_id = 'menu_performance_viewMyPerformanceTrackerList'
        self.commitment_deadline_by_href = 'Commitments and Deadlines'
        self.add_tracker_by_id = 'btnAdd'
        self.add_performance_log_by_id = 'addperformanceTrackerLog_log'
        self.select_achievment_by_id = 'addperformanceTrackerLog_achievement'
        self.add_performance_comment_by_id = 'addperformanceTrackerLog_comment'
        self.save_tracker_by_id = 'saveBtn'

    def navigate_to_my_trackers(self):
        self.mouse_hovering(self.performance_tab_by_id)
        self.element_click(self.my_trackers_by_id)

    def add_tracker(self,log,achievment,comment):
        self.element_click(self.commitment_deadline_by_href,"linktext")
        self.element_click(self.add_tracker_by_id)
        self.send_keys(log,self.add_performance_log_by_id)
        self.select_from_dropdown(achievment,self.select_achievment_by_id)
        self.send_keys(comment,self.add_performance_comment_by_id)
        self.element_click(self.save_tracker_by_id)

