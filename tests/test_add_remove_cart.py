from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from tests.login_page import LoginPage
import time
from selenium.webdriver.support.ui import Select

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
        self.driver.get("https://shoppingonline.up.railway.app/store/")  # Adjust the URL

        product_details = self.driver.find_element(By.CSS_SELECTOR, ".card.card-product-grid")
        product_details.click()

        dropdown_color = self.driver.find_element(By.NAME, "color")
        # Create a Select object
        select = Select(dropdown_color)
        # Select by visible text
        select.select_by_visible_text("Red")

        dropdown_size = self.driver.find_element(By.NAME, "size")
        # Create a Select object
        select = Select(dropdown_size)
        # Select by visible text
        select.select_by_visible_text("Small")

        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary:has(span.text)")
        add_to_cart_button.click()

        checkout_button = self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.btn-block")
        self.assertIn("Checkout", checkout_button.text)


         # Click the Remove link
        remove_link = self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-danger")
        remove_link.click()

         # Handle the alert by accepting it (clicking "OK")
        WebDriverWait(self.driver, 10).until(EC.alert_is_present(),
                                              "Timed out waiting for confirmation popup to appear.")

        alert = self.driver.switch_to.alert
        alert.accept()  # Click the OK button on the confirmation box

        # Locate the message element
        empty_cart_message = self.driver.find_element(By.CSS_SELECTOR, "h2.text-center")

        # Assert that the message is correct
        self.assertEqual("Your Shopping Cart is Empty", empty_cart_message.text, "The cart is not empty as expected.")

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()