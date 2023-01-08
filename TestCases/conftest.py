from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if str.lower(browser) == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif str.lower(browser) == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install)
    elif str.lower(browser) == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif str.lower(browser) == 'ie':
        driver = webdriver.ie(IEDriverManager().install())
    driver.maximize_window()

    return driver

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# def pytest_configure(config):
#     config._meta_data['Project'] = 'Automated cases of OrangeHRM website'
#     config._meta_data['Test Automation Engineer'] = 'Nigar Iqbal'
