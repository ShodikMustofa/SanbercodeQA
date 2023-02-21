import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def  setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_add_cart(self):
        #Steps
        auto = self.browser #open web browser
        auto.get("https://www.saucedemo.com/") #open website
        time.sleep(2)
        auto.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        auto.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        auto.find_element(By.ID, "login-button").click()
        time.sleep(1)
        auto.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(1)

        #validation
        response_data = auto.find_element(By.XPATH,"//*[@id='remove-sauce-labs-backpack']").text
        self.assertIn(response_data,"REMOVE")

    def test_b_remove_cart_at_homepage(self):
        #Steps
        auto = self.browser #open web browser
        auto.get("https://www.saucedemo.com/") #open website
        time.sleep(2)
        auto.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        auto.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        auto.find_element(By.ID, "login-button").click()
        time.sleep(1)
        auto.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(1)
        auto.find_element(By.XPATH, "//*[@id='remove-sauce-labs-backpack']").click()

        #validation
        response_data = auto.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").text
        self.assertIn(response_data,"ADD TO CART")

    def test_c_remove_cart_in_checkout_menu(self):
        #Steps
        auto = self.browser #open web browser
        auto.get("https://www.saucedemo.com/") #open website
        time.sleep(2)
        auto.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        auto.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        auto.find_element(By.ID, "login-button").click()
        time.sleep(1)
        auto.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(1)
        auto.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        auto.find_element(By.XPATH,"//*[@id='remove-sauce-labs-backpack']").click()

        #validation
        response_data = auto.find_element(By.CLASS_NAME,"cart_quantity_label").text
        self.assertIn(response_data,"QTY")

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()