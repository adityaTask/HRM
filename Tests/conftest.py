import pytest
from configs.config_parser import ConfigParser
from base.web_driver import WebDriver
from Pages.Login.login import LoginPage


@pytest.fixture(scope="class")
def setup(headless):
    config = ConfigParser()
    wd = WebDriver(url=config.get_url(), head_less=headless)
    driver = wd.create_driver_instance()
    lp = LoginPage(driver)
    lp.login(username=config.get_username(), password=config.get_password())
    # not required
    # if request.cls is not None:
    #     request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--headless")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")
