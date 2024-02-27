from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@when('User on the Dashboard page')
def verify_dashboard(context):
    assert context.driver.title == "Dashboard"

@when('User click on the Model dropdown')
def click_model_dropdown(context):
    context.driver.find_element(By.ID, "model").click()

@then('Select the My Models option')
def select_my_models(context):
    context.driver.find_element(By.LINK_TEXT, "My Models").click()

@then('User should be redirected to the My Models page')
def verify_my_models(context):
    WebDriverWait(context.driver, 10).until(EC.title_is("My Models"))

@then('User should take an screenshot')
def take_screenshot_my_models(context):
    context.driver.save_screenshot("my_models.png")

@given('User is on my models page')
def verify_my_models(context):
    assert context.driver.title == "My Models"

@when('Search for "{model_id}" model')
def search_model(context, model_id):
    context.driver.find_element(By.ID, "search").send_keys(model_id + Keys.ENTER)

@then('Right Click on the Model in a Table')
def right_click_model(context):
    model = context.driver.find_element(By.XPATH, "//table//tr[td[text()='{model_id}']]".format(model_id=model_id))
    webdriver.ActionChains(context.driver).context_click(model).perform()

@then('Click on the View Details button')
def click_view_details(context):
    context.driver.find_element(By.LINK_TEXT, "View Details").click()

@then('User take a screenshot')
def take_screenshot_model_details(context):
    context.driver.save_screenshot("model_details.png")
