from PageObjects.LoginPage import LoginPage
from Utilities.utils import Utils
from Utilities.custom_logger import CustomLogger
from Utilities.data_reader import DataReader
from Utilities.base import Base

from unittest import TestCase
import pytest
class TestLoginCases(TestCase):
    def setUp(self):
        self.util = Utils
        self.data_reader = DataReader('login')
        self.log = CustomLogger.generate_log()
        url = self.data_reader.get_base_url()
        self.page = LoginPage(url)
        self.log.debug(f'Using URL: {url}')
        self.driver = self.page.driver
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        self.test_title = self.util.get_test_case_title()
        self.log.info(f'Running test case: {self.test_title}')
        data = self.data_reader.get_test_case_data(self.test_title)
        self.page.set_username(data['user_name'])
        self.page.set_password(data['password'])
        self.page.click_login()
        self.assertTrue(self.page.check_visibility_of_element(self.page.dashboard))
        self.page.take_screenshot(self.test_title)

    def test_unsuccessful_login(self):
        self.test_title = self.util.get_test_case_title()
        self.log.info(f'Running test case: {self.test_title}')
        data = self.data_reader.get_test_case_data(self.test_title)
        self.page.set_username(data['user_name'])
        self.page.set_password(data['password'])
        self.page.click_login()
        error_message = self.page.get_text_of_locator(self.page.error_alert)
        self.assertEqual('Invalid credentials', error_message)

