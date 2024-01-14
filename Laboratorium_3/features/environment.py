import os
from selenium import webdriver

def before_all(context):
    browser = os.environ.get('BROWSER', 'chrome').lower()
    if browser == 'firefox':
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()
