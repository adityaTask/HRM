from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type='id'):
        if locator_type == 'id':
            return By.ID
        elif locator_type.lower() == 'linktext':
            return By.LINK_TEXT
        elif locator_type.lower() == 'class':
            return By.CLASS_NAME
        elif locator_type.lower() == 'xpath':
            return By.XPATH

    def find_element(self, locator, locator_type='id'):
        by_type = self.get_by_type(locator_type)
        try:
            self.driver.find_element(by_type, locator)
        except Exception as e:
            print(e)

    def find_elements_list(self, locator, locator_type='id'):
        try:
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            return elements
        except Exception as e:
            print(e)

    def send_keys(self, data, locator, locator_type='id'):
        by_type = self.get_by_type(locator_type)
        element = self.driver.find_element(by_type, locator)
        try:
            element.clear()
            element.send_keys(data)
        except Exception as e:
            print(e)

    def element_click(self, locator, locator_type='id'):
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            element.click()
        except Exception as e:
            print(e)

    def is_displayed(self, locator, locator_type='id'):
        by_type = self.get_by_type(locator_type)
        element = self.driver.find_element(by_type, locator)
        try:
            return element.is_displayed()
        except Exception as e:
            print(e)

    def get_text(self, locator, locator_type='id'):
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            return element.text
        except Exception as e:
            print(e)

    def select_from_dropdown(self,text,locator, locator_type='id'):
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            sel = Select(element)
            sel.select_by_visible_text(text)
        except Exception as e:
            print(e)

