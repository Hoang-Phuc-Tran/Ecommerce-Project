from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class TestRegistration(unittest.TestCase):
    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximizes the browser window
        self.driver.get("https://shoppingonline.up.railway.app/accounts/register/")

    def test_registration(self):
        driver = self.driver

        # Fill in the registration form
        first_name = driver.find_element(By.NAME, "first_name")
        last_name = driver.find_element(By.NAME, "last_name")
        phone_number = driver.find_element(By.NAME, "phone_number")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        confirm_password_input = driver.find_element(By.NAME, "confirm_password")

        register_btn = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")

        first_name.send_keys("Hoang Phuc")
        last_name.send_keys("Tran")
        phone_number.send_keys("5127815512")
        email_input.send_keys("newuser123@example.com")
        password_input.send_keys("Securepassword123")
        confirm_password_input.send_keys("Securepassword123")

        register_btn.click()

        # Verify registration success by checking the confirmation message and the login link
        confirmation_message = driver.find_element(By.CLASS_NAME, "errorlist")

        self.assertIn("Account with this Email already exists.", confirmation_message.text)


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


