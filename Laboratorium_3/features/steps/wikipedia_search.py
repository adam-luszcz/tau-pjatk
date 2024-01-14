from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from behave import *

@given('I am on the Wikipedia home page')
def step_impl(context):
    context.driver.get("https://www.wikipedia.org/")

@when('I search for "Python"')
def step_impl(context):
    search_input = context.driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Python")
    search_input.send_keys(Keys.RETURN)

@then('the search results should include "Python"')
def step_impl(context):
    time.sleep(2)
    assert "Python" in context.driver.title, "Search did not work correctly"
