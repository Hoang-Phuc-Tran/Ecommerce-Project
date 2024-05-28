import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestDropdownSelection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximizes the browser window
        self.driver.get("https://shoppingonline.up.railway.app/")  # URL to your store

    def test_select_t_shirts(self):
        # Step 1: Click the dropdown button to expand the dropdown menu
        dropdown_button = self.driver.find_element(By.CLASS_NAME, "dropdown-toggle")
        dropdown_button.click()

        # Step 2: Wait for the dropdown menu to be visible and click the 't Shirts' link
        t_shirts_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "t Shirts"))
        )
        t_shirts_link.click()

        # Optional: Assert the current URL to verify navigation if needed
        current_url = self.driver.current_url
        self.assertIn("/store/category/t-shirts/", current_url, "URL does not contain the t-shirt category path.")

    def test_search_product(self):
        # Navigate to the store page
        self.driver.get("https://shoppingonline.up.railway.app/")

        # Enter search query in the search bar
        search_box = self.driver.find_element(By.NAME, "keyword")
        search_box.send_keys("shirt")

        # Submit the search form
        search_button = self.driver.find_element(By.CSS_SELECTOR, "i.fa.fa-search")
        search_button.click()

         # Verify that search results are displayed and count the items
        items_text = self.driver.find_element(By.CSS_SELECTOR, "div.form-inline span").text
        # Extract the number from the text
        items_count = int(items_text.split()[0])  # Assumes the format "X Items found" and X is an integer

        # Assert the number of items is greater than 0
        self.assertGreater(items_count, 0, "Expected more than 0 items to be found, but none were found.")

    def test_product_details(self):
        # Navigate to the store page
        self.driver.get("https://shoppingonline.up.railway.app/")

        # Enter search query in the search bar
        search_box = self.driver.find_element(By.NAME, "keyword")
        search_box.send_keys("shirt")

        # Submit the search form
        search_button = self.driver.find_element(By.CSS_SELECTOR, "i.fa.fa-search")
        search_button.click()

         # Verify that search results are displayed and count the items
        items_text = self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-block.btn-primary")
        items_text.click()

        # Verify registration success by checking the confirmation message and the login link
        add_cart = self.driver.find_element(By.CSS_SELECTOR, "span.text")
        self.assertIn("Add to Cart", add_cart.text)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()