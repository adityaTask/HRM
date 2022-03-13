import pytest
from configs.config_parser import ConfigParser
from base.web_driver import WebDriver
from Pages.login import LoginPage


@pytest.fixture(scope="class")
def setup(request):
    config = ConfigParser()
    wd = WebDriver(url=config.get_url())
    driver = wd.create_driver_instance()
    lp = LoginPage(driver)
    lp.login(username=config.get_username(), password=config.get_password())
    # if request.cls is not None:
    #     request.cls.driver = driver
    yield driver
    driver.quit()
