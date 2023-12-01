import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sauce_demo_cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.CLASS_NAME, "btn_primary").click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        product_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        self.assertTrue(product_in_cart, "Product not found in cart at checkout")
        print(f"Sauce Demo checkout test passed on Google Chrome")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
