import time
from locators.path_login import ACCOUNT_ID_XPATH, LOGOUT_BUTTON, PASSWORD_XPATH, USERNAME_XPATH
from framework.webapp import webapp
from selenium.webdriver.common.by import By

class Login():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Login()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
    
    def isLoggedIn(self):
        time.sleep(5)
        current_url = self.driver.current_url
        return 'dashboard' in current_url


    def fill_login_details(self, username,account_id,password):
        # username_field = webapp.find_element("xpath", USERNAME_XPATH)
        # account_id_field = webapp.find_element("xpath",ACCOUNT_ID_XPATH)
        # password_field = webapp.find_element("xpath",PASSWORD_XPATH)
        # time.sleep(5)
        # username_field.send_keys(username)
        # account_id_field.send_keys(account_id)
        # password_field.send_keys(password)
        time.sleep(2)
        webapp.input_element((By.XPATH,USERNAME_XPATH),username)
        webapp.input_element((By.XPATH,ACCOUNT_ID_XPATH),account_id)
        webapp.input_element((By.XPATH,PASSWORD_XPATH),password)
    
    def logout(self):
        # # Use the existing webapp methods to find and click the logout button
        # webapp.click_on("xpath", "//button[@title='Logout']//*[name()='svg']")
        webapp.click_element((By.XPATH,LOGOUT_BUTTON))
    
login = Login.get_instance()
