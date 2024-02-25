import time
import os

from data.config import settings
from urllib.parse import urljoin
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.webapp import webapp
from constants.path_login import ACCOUNT_ID_XPATH, PASSWORD_XPATH, USERNAME_XPATH, LOGIN_BUTTON_XPATH, ERROR_MESSAGE_XPATH
from pages.login import login


@when('I enter my username "{username}" and account ID "{account_id}" and password "{password}"')
def step_impl(context, username, account_id, password):
    time.sleep(4)
    login.fill_login_details(username, account_id, password)


@then('I click the login button')
def step_impl(context):
    webapp.click_on('xpath',LOGIN_BUTTON_XPATH)
    time.sleep(3)

@then('I should be redirected to the dashboard page')
def step_impl(context):
    dashboard_url = urljoin(settings['url'], "dashboard")
    WebDriverWait(webapp.get_driver(), 20).until(EC.url_matches(dashboard_url))
    time.sleep(4)


@then('I take a screenshot of the dashboard')
def step_impl(context):
    time.sleep(3)
    webapp.take_screenshot_of_current_page();
    


@when('I enter invalid username "{username}" and account ID "{account_id}" and password "{password}"')
def step_impl(context, username, account_id, password):
    time.sleep(2)
    login.fill_login_details(username, account_id, password)


@then('I should see an error massage "{error_massage}"')
def step_impl(context, error_massage):
    time.sleep(2)
    error_massage_element = webapp.find_element("xpath", ERROR_MESSAGE_XPATH)
    assert error_massage_element.text == error_massage
    # time.sleep(2)


@then('I take a screenshot of the error massage')
def step_impl(context):
    time.sleep(3)
    webapp.take_screenshot_of_current_page();

@given('User should loggedin')
def step_impl(context):
    return login.isLoggedIn()

@when('User clicks on logout button')
def step_impl(context):
    login.logout()

@then('User should be logged out successfully')
def step_impl(context):
    assert not login.isLoggedIn()

@then('Take a screenshot of the landing page')
def step_impl(context):
    webapp.take_screenshot_of_current_page()
