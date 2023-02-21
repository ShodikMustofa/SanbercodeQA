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
        auto.find_element(By.XPATH,"//*[@id='menu_button_container']/div/div[1]/div").click()
        time.sleep(1)
        auto.find_element(By.XPATH,"//*[@id='logout_sidebar_link']").click()
        time.sleep(1)
        #validation
        response_data = auto.find_element(By.ID,"login_credentials").text
        self.assertIn('Accepted usernames are:', response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()