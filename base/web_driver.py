from selenium import webdriver


class WebDriver():
    def __init__(self, url, head_less, browser='Chrome'):
        self.browser = browser
        self.url = url
        self.head_less = head_less

    def create_driver_instance(self):
        '''
        Method used to create a driver instance
        '''
        if self.browser == 'Chrome':
            if self.head_less is None:
                self.head_less = 'false'
            if self.head_less.lower() == 'true':
                op = webdriver.ChromeOptions()
                op.add_argument('headless')
                op.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver = webdriver.Chrome(executable_path="../utilities/chromedriver.exe", options=op)
            else:
                op = webdriver.ChromeOptions()
                op.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver = webdriver.Chrome(executable_path="../utilities/chromedriver.exe",options=op)
            driver.maximize_window()
            driver.get(url=self.url)
            driver.implicitly_wait(5)
        return driver

