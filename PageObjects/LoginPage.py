from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utilities.base import Base



#Add use of pytest markers, parallel running, 

class LoginPage(Base):
    def __init__(self, url, browser='chrome', driver=None, headless=False):
        Base.__init__(self, driver, url, browser=browser, headless=headless)
        self.wd_wait = WebDriverWait(self.driver, 10)
        self.username_textbox = "//div[@class='orangehrm-login-form']//input[@name='username']"
        self.password_textbox = "//div[@class='orangehrm-login-form']//input[@name='password']"
        self.login_button = "//div[@class='orangehrm-login-form']//button[contains(@class,'orangehrm-login-button')]"
        self.dashboard = "//div[@class='oxd-topbar-header-title']//span//*[normalize-space() = 'Dashboard']"
        self.error_alert = "//div[@class='oxd-alert oxd-alert--error']//div//p"
    def set_username(self, username):
        self.set_value_in_field(self.username_textbox, username)

    def set_password(self, password):
        self.set_value_in_field(self.password_textbox, password)

    def click_login(self):
        self.click_button(self.login_button)