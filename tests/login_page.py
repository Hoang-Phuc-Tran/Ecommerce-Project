from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        username_input = self.driver.find_element(By.NAME, "email")
        username_input.clear()
        username_input.send_keys(username)

    def set_password(self, password):
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)

    def submit(self):
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
        submit_btn.click()
