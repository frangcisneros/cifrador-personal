from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from flask import Flask, jsonify, request


class BrowserTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get("http://localhost:5000")
        input_username = self.browser.find_element(By.ID, "new_username")
        input_username.send_keys("fran2")
        input_password = self.browser.find_element(By.ID, "new_password")
        input_password.send_keys("fran2")
        input_email = self.browser.find_element(By.ID, "email")
        input_email.send_keys("exampleemail@email.com")
        input_firstname = self.browser.find_element(By.ID, "firstname")
        input_firstname.send_keys("fran")
        input_lastname = self.browser.find_element(By.ID, "lastname")
        input_lastname.send_keys("fran")
        input_phone = self.browser.find_element(By.ID, "phone")
        input_phone.send_keys("123456789")
        input_address = self.browser.find_element(By.ID, "address")
        input_address.send_keys("fran")
        input_city = self.browser.find_element(By.ID, "city")
        input_city.send_keys("fran")
        input_country = self.browser.find_element(By.ID, "country")
        input_country.send_keys("fran")
        self.browser.find_element(By.ID, "register_submit").click()

    def test_user_panel(self):
        self.browser.get("http://localhost:5000/user_panel")


if __name__ == "__main__":
    unittest.main()
