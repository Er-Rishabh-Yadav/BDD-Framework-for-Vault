from behave import given, when, then
from pages.dashboard import dashboard
from framework.webapp import webapp
from locators.path_dashboard import REPORT_BUTTON
from selenium.webdriver.common.by import By
@when('I click on the report button')
def step_impl(context):
    webapp.click_element((By.XPATH,REPORT_BUTTON))



@then('I should directed to report')
def step_impl(context):
    url = webapp.get_page_url("dashboard")
    webapp.wait_for_url_match(url,20)



@then('I take a screenshot of the report')
def step_impl(context):
    webapp.take_screenshot_of_current_page("report_screenshot")