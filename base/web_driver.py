from selenium import webdriver


class WebDriver():
    def __init__(self, url, head_less, browser='Chrome'):
        self.browser = browser
        self.url = url
        self.head_less = head_less
        print("Type of head_less",type(self.head_less),self.head_less)

    def create_driver_instance(self):
        if self.browser == 'Chrome':
            if self.head_less.lower() == 'true':
                op = webdriver.ChromeOptions()
                op.add_argument('headless')
                driver = webdriver.Chrome(executable_path="../utilities/chromedriver.exe", options=op)
            else:
                driver = webdriver.Chrome(executable_path="../utilities/chromedriver.exe")
            driver.maximize_window()
            driver.get(url=self.url)
            driver.implicitly_wait(10)
        return driver

