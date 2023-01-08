from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    username_textbox = "//div[@class='orangehrm-login-form']//input[@name='username']"
    password_textbox = "//div[@class='orangehrm-login-form']//input[@name='password']"
    login_button = "//div[@class='orangehrm-login-form']//button[contains(@class,'orangehrm-login-button')]"

    def __init__(self, driver):
        self.driver = driver
        self.wd_wait = WebDriverWait(self.driver, 1000)

    def set_username(self, username):
        self.wd_wait.until(EC.presence_of_element_located((By.XPATH, self.username_textbox)))
        self.driver.find_element('xpath', self.username_textbox).clear()
        self.driver.find_element('xpath', self.username_textbox).send_keys(username)

    def set_password(self, password):
        self.wd_wait.until(EC.presence_of_element_located((By.XPATH, self.password_textbox)))
        self.driver.find_element('xpath', self.password_textbox).clear()
        self.driver.find_element('xpath', self.password_textbox).send_keys(password)

    def click_login(self):
        self.wd_wait.until(EC.presence_of_element_located((By.XPATH, self.login_button))).click()
