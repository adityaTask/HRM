import configparser

class ConfigParser():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('../configs/config.ini')

    def get_url(self):
        return self.config['test_chrome']['url']

    def get_browser(self):
        return self.config['test_chrome']['browser']

    def get_username(self):
        return self.config['test_chrome']['username']

    def get_password(self):
        return self.config['test_chrome']['password']
