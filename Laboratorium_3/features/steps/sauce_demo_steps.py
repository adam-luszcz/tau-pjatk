from selenium.webdriver.common.by import By
from behave import *

@given('I am on the Sauce Demo login page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.implicitly_wait(10)

@when('I enter valid credentials')
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()

@when('I add a product to the cart')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "btn_primary").click()

@then('the product should be added to the cart successfully')
def step_impl(context):
    product_in_cart = context.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert product_in_cart, "Product not found in cart"
