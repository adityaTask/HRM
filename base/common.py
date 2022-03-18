from base.selenium_driver import SeleniumDriver


class Common(SeleniumDriver):
    def __init__(self, driver):
        self.driver = driver
        self.next_page_by_xpath = "//a[text()='Next']"
        self.columns_by_xpath = '//thead//th//a'
        self.rows_in_table_by_xpath = '//tbody//tr'
        self.item_in_table_by_xpath = '//tbody//tr[{0}]//td[{1}]//a'
        self.check_row_by_xpath = "//tbody//tr[{0}]//td[1]//input"

    def find_row_index_in_table(self, column_name, value):
        column_list = self.find_elements_list(self.columns_by_xpath, "xpath")
        col_index = 0
        index = 2
        for column in column_list:
            if self.get_text_by_element(column) == column_name:
                col_index = index
                break
            index += 1
        while True:
            row_index = 1
            for i in range(1, len(self.find_elements_list(self.rows_in_table_by_xpath, "xpath")) + 1):
                current_name = self.get_text(self.item_in_table_by_xpath.format(i, col_index),"xpath")
                if current_name == value:
                    return row_index
                row_index += 1
            self.element_click(self.next_page_by_xpath, "xpath")

    def find_and_check_row_in_table(self, column_name, value):
        row_index = self.find_row_index_in_table(column_name, value)
        self.element_click(self.check_row_by_xpath.format(row_index), "xpath")
