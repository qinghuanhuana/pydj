from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    bbs_login_usr_loc = (By.XPATH, '//div[@id="mzCust"]/div/img')
    bbs_login_button_loc = (By.ID, "mzLogin")

    def bbs_login(self):
        self.find_element(*self.bbs_login_usr_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.ID, 'account')
    login_password_loc = (By.ID, 'password')
    login_button_loc = (By.ID, 'login')

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self, username, password):
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH, '//span[@for="account"]')
    pawd_error_hint_loc = (By.XPATH, '//span[@for="password"]')
    user_login_success_loc = (By.ID, 'mzCustName')

    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text