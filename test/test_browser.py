from selenium import webdriver
import unittest


class BrowserTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get("http://localhost:5000")
