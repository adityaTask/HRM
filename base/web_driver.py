from selenium import webdriver


class WebDriver():
    def __init__(self, url, browser='Chrome'):
        self.browser = browser
        self.url = url

    def create_driver_instance(self):
        if self.browser == 'Chrome':
            driver = webdriver.Chrome("../utilities/chromedriver.exe")
            driver.maximize_window()
            driver.get(url = self.url)
            driver.implicitly_wait(10)
        return driver

