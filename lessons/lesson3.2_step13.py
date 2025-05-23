import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        time.sleep(1)
        self.browser.quit()

    def fill_and_submit_form(self, url):
        self.browser.get(url)

        first_block = self.browser.find_element(By.CSS_SELECTOR, "div.first_block")

        input1 = first_block.find_element(By.CSS_SELECTOR, "input.form-control.first")
        input1.send_keys("Ivan")

        input2 = first_block.find_element(By.CSS_SELECTOR, "input.form-control.second")
        input2.send_keys("Petrov")

        input3 = first_block.find_element(By.CSS_SELECTOR, "input.form-control.third")
        input3.send_keys("example@gmail.com")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        return welcome_text

    def test_registration1(self):
        welcome_text = self.fill_and_submit_form("http://suninjuly.github.io/registration1.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 
                         "Registration1 failed")

    def test_registration2(self):
        welcome_text = self.fill_and_submit_form("http://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 
                         "Registration2 failed")

if __name__ == "__main__":
    unittest.main()