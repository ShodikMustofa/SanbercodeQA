import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def  setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_login_success(self):
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

        #validation
        response_data = auto.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

    def test_b_login_failed_wrong_password(self):
        auto = self.browser
        auto.get("https://www.saucedemo.com/") #open website
        time.sleep(2)
        auto.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        auto.find_element(By.ID, "password").send_keys("xxxx")
        time.sleep(1)
        auto.find_element(By.ID, "login-button").click()
        time.sleep(1)

        #validation
        response_data = auto.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        self.assertEqual(response_data, "Epic sadface: Username and password do not match any user in this service")

    def test_c_login_failed_blank_password(self):
        auto = self.browser
        auto.get("https://www.saucedemo.com/") #Open website
        time.sleep(2)
        auto.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        auto.find_element(By.ID, "password").send_keys("")
        time.sleep(1)
        auto.find_element(By.ID, "login-button").click()
        time.sleep(1)

        #validation
        response_data = auto.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        self.assertIn('Epic sadface: Password is required', response_data)
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()