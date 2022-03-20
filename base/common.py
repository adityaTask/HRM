from base.selenium_driver import SeleniumDriver


class Common(SeleniumDriver):
    def __init__(self, driver):
        self.driver = driver
        self.next_page_by_xpath = "//a[text()='Next']"
        self.columns_by_xpath = '//thead//th//*'
        self.rows_in_table_by_xpath = '//tbody//tr'
        self.item_in_table_by_xpath = '//tbody//tr[{0}]//td[{1}]//a'
        self.check_row_by_xpath = "//tbody//tr[{0}]//td[1]//input"
        self.page_top_by_xpath = "//ul[@class='paging top']//li[@class='desc']"

    def find_column_index_in_table(self,column_name):
        column_list = self.find_elements_list(self.columns_by_xpath, "xpath")
        col_index = 1
        for column in column_list:
            if self.get_text_by_element(column) == column_name:
                return col_index
            col_index += 1

    def find_row_index_in_table(self, column_name, value):
        col_index = self.find_column_index_in_table(column_name)
        page_by_top = self.find_elements_list(self.page_top_by_xpath,"xpath")
        if len(page_by_top) > 0:
            text = self.get_text(self.page_top_by_xpath,"xpath")
            rows = int(text.split(' of ')[-1])
            pages = (rows//50) + 1
        else:
            pages = 1
        print("\nTotal Pages found ",pages)
        current_page = 1
        while current_page <= pages:
            row_index = 1
            for i in range(1, len(self.find_elements_list(self.rows_in_table_by_xpath, "xpath")) + 1):
                current_name = self.get_text(self.item_in_table_by_xpath.format(i, col_index),"xpath")
                if current_name == value:
                    return row_index
                row_index += 1
            self.element_click(self.next_page_by_xpath, "xpath")
            current_page += 1

    def find_and_check_row_in_table(self, column_name, value):
        row_index = self.find_row_index_in_table(column_name, value)
        self.element_click(self.check_row_by_xpath.format(row_index), "xpath")
