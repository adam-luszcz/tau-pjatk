import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.drivers = [webdriver.Chrome(), webdriver.Firefox()]

    def test_sauce_demo_login_and_add_to_cart(self):
        for driver in self.drivers:
            driver.get("https://www.saucedemo.com/")
            driver.implicitly_wait(10)

            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()

            driver.find_element(By.CLASS_NAME, "btn_primary").click()

            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

            product_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
            self.assertTrue(product_in_cart, "Product not found in cart")

    def test_wikipedia_search(self):
        for driver in self.drivers:
            driver.get("https://www.wikipedia.org/")

            search_input = driver.find_element(By.ID, "searchInput")

            search_input.send_keys("Python")
            search_input.send_keys(Keys.RETURN)

            time.sleep(2)
            self.assertIn("Python", driver.title, "Search did not work correctly")

    def tearDown(self):
        for driver in self.drivers:
            driver.close()

if __name__ == "__main__":
    unittest.main()
