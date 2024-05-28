from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from .login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Or path to the WebDriver
        self.driver.maximize_window()  # Maximizes the browser window
        self.driver.get("https://shoppingonline.up.railway.app/accounts/login/")  # Adjust the URL

    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.set_username("ptran9102@gmail.com")
        login_page.set_password("admin")
        login_page.submit()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://shoppingonline.up.railway.app/accounts/"))
        # Verify login success, for example, by checking the URL or looking for a logout link
        self.assertEqual("https://shoppingonline.up.railway.app/accounts/", self.driver.current_url)

    def test_login_failure(self):
        login_page = LoginPage(self.driver)
        login_page.set_username("invalid_user@gmail.com")
        login_page.set_password("invalid_password")
        login_page.submit()
        # Verify login failure, for example, by checking error messages
        error_message_div = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger")
        error_message = error_message_div.text
        self.assertIn("Error: Invalid login credentials", error_message)

    def test_logout(self):
        # Perform login first
        login_page = LoginPage(self.driver)
        login_page.set_username("ptran9102@gmail.com")
        login_page.set_password("admin")
        login_page.submit()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://shoppingonline.up.railway.app/accounts/"))

        # Locate and click the logout link
        logout_link = self.driver.find_element(By.LINK_TEXT, "Logout")
        logout_link.click()

        # Wait for redirection to login page or verify logout through UI changes
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://shoppingonline.up.railway.app/accounts/login/"))
        self.assertEqual("https://shoppingonline.up.railway.app/accounts/login/", self.driver.current_url)


    def tearDown(self):
        self.driver.quit()


