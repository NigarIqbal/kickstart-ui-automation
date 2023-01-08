from PageObjects.LoginPage import LoginPage
from Utilities.utils import Utils
from Utilities.custom_logger import CustomLogger
from Utilities.data_reader import DataReader

class TestLoginCases:

    util = Utils
    data_reader = DataReader('login')
    log = CustomLogger.generate_log()
    url = data_reader.get_base_url()

    log.debug(f'Running cases on {url}')

    def test_successful_login(self, setup):

        self.driver = setup
        self.driver.get(self.url)

        test_title = self.util.get_test_case_title(self)
        self.log.info(f'Running test case: {test_title}')

        data = self.data_reader.get_test_case_data(test_title)
        self.page = LoginPage(self.driver)
        self.page.set_username(data['user_name'])
        self.page.set_password(data['password'])

        self.page.click_login()


