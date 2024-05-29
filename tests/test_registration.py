from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        # Configure ChromeOptions
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-gpu")  # Applicable for windows OS and Chrome. See documentation for more details
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        chrome_options.add_argument("--window-size=1920,1080")  # Explicitly set window size for headless mode

        # Initialize the WebDriver with options
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://shoppingonline.up.railway.app/accounts/register/")  # Navigate to the registration page

    def test_registration(self):
        driver = self.driver

        # Fill in the registration form
        first_name = driver.find_element(By.NAME, "first_name")
        last_name = driver.find_element(By.NAME, "last_name")
        phone_number = driver.find_element(By.NAME, "phone_number")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_felement(By.NAME, "password")
        confirm_password_input = driver.find_element(By.NAME, "confirm_password")

        register_btn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")

        first_name.send_keys("Hoang Phuc")
        last_name.send_keys("Tran")
        phone_number.send_keys("5127815512")
        email_input.send_keys("newuser123@example.com")
        password_input.send_keys("Securepassword123")
        confirm_password_input.send_keys("Securepassword123")

        register_btn.click()

        # Verify registration success by checking the confirmation message
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "errorlist")))
        confirmation_message = driver.find_element(By.CLASS_NAME, "errorlist")

        self.assertIn("Account with this Email already exists.", confirmation_message.text)

    def tearDown(self):
        time.sleep(3)  # Allow some time before closing the browser
        self.driver.quit()

