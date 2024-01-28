from Utilities.custom_logger import CustomLogger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import DesiredCapabilities, Remote, Chrome, Firefox, ActionChains
from datetime import datetime, timedelta, date
import os
"""
It's a wrapper class for selenium webdriver methods. Instead of directly calling webdriver methods repeatedly for each case,
we can encapsulate webdriver methods here and call them as & when required.
"""

class Base(object):

    def __init__(self, driver, url, browser, headless):
        if driver is None:
            self.driver = self.get_driver(url, browser, headless)
        else:
            self.driver = driver
        self.wd_wait = WebDriverWait(self.driver, 60)

    def get_driver(self, url, browser, headless):
        if browser == "edge":
                options = EdgeOptions()
                options.use_chromium = True
                if headless:
                    options.add_argument('--headless')
                #self.driver = Edge(options=options)
        elif browser == "firefox":
                options = FirefoxOptions()
                if headless:
                    options.add_argument('--headless')
                self.driver = Firefox(options=options)
        elif browser == "chrome" or browser is None:
                options = ChromeOptions()
                if headless:
                    options.add_argument('--headless')
                self.driver = Chrome(options=options)
        else:
            pass
            # df_client = boto3.client("devicefarm", region_name="us-west-2")
            # testgrid_url_response = df_client.create_test_grid_url (
            #     projectArn="arn:aws:devicefarm:us-west-2:249535075320:testgrid-project:a3e4c786-784f-4f95-a2cf-2addea18a9d4",
            #     expiresInSeconds=300
            # )
            # capabilities = DesiredCapabilities.CHROME
            # capabilities["platform"] = "windows"
            # self.driver = Remote(testgrid_url_response['url'], capabilities)

        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(2)
        self.driver.get(url)

        self.session_url = self.driver.command_executor._url
        self.session_id = self.driver.session_id

        return self.driver

    def generate_date_with_seconds(self):
        now = datetime.now()
        return now.strftime("%Y%m%d%H%M%S")

    def set_value_in_field(self, locator, value):
        self.wd_wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        self.driver.find_element('xpath', locator).clear()
        self.driver.find_element('xpath', locator).send_keys(value)
    
    def click_button(self, locator):
        try:
           self.wd_wait.until(EC.presence_of_element_located((By.XPATH, locator))).click()
        except Exception as e:
            print(e)
            return False
        
    def check_element_visibility(self, locator, timeout=5):
        self.wd_wait = WebDriverWait(self.driver, timeout)
        try:
           self.wd_wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
            return False
        
    def take_screenshot(self, prefix, sizes=[[1920,1080]]):
        if os.getenv('WORKING_DIRECTORY') is not None:
            path = "{}/test_results/{}".format(os.getenv('WORKING_DIRECTORY').strip("/").strip("\\"), prefix)
        else:
            path = f'{os.getcwd()}/test_results/screenshots/{prefix}_{self.generate_date_with_seconds()}'
        
        for size in sizes:
            self.driver.set_window_size(size[0], size[1])
            try:
                os.makedirs(path)
            except FileExistsError:
                pass
            self.driver.save_screenshot(f'{path}/{size[0]}x{size[1]}.png')

    def check_visibility_of_element(self, locator):
        try:
            self.wd_wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            bool = self.driver.find_element('xpath', locator).is_displayed()
            return bool
        except Exception as e:
            print(e)
            return False

    def get_text_of_locator(self, locator):
        try:
            self.wd_wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            text = self.driver.find_element('xpath', locator).text
            return text
        except Exception as e:
            print(e)
            return False
        
    

