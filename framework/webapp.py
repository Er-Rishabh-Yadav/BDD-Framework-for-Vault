import os
import time
from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def find_element(self, type, element):
        if type == "id":
            return self.driver.find_element(By.ID, element)
        elif type == "xpath":
            return self.driver.find_element(By.XPATH, element)
        elif type == "css":
            return self.driver.find_element(By.CSS_SELECTOR, element)
        else:
            return None

    def click_on(self, type, element):
        if type in ["id", "xpath", "css"]:
            self.find_element(type, element).click()

    def send_value_to_element(self, type, element, value):
        if type in ["id", "xpath", "css"]:
            input_field = self.find_element(type, element)
            input_field.clear()
            input_field.send_keys(value)

    def wait_and_click(self, type, element, timeout=10):
        if type in ["id", "xpath", "css"]:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((getattr(By, type.upper()), element)))
            self.find_element(type, element).click()
    def wait_for_element( self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    def take_screenshot_of_current_page(self):
        current_page = self.driver.current_url.split('/')[-1]
        screenshot_path = os.path.join(os.getcwd(), f"{current_page}_screenshot.png")
        self.driver.save_screenshot(screenshot_path)

    def verify_component_exists(self, component):
        assert component in self.driver.find_element(By.TAG_NAME, 'body').text, \
            f"Component {component} not found on page"

webapp = WebApp.get_instance()
