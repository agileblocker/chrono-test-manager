# python3

# Test Case 1 - Launching the site / landing page (+)

# This is importing the necessary modules
# Unittest is for executing this script like a test case with a result at the end
# Selenium is the automated test module. Importing Keys allows inputs

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# This is building the actual test case
class yahoo_landing_page(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_landing_page_in_yahoo(self):
        driver=self.driver
        driver.get("http://www.yahoo.com/")
        self.assertIn("Yahoo", driver.title)

# This is looking for the element ID for the big Yahoo! button in the top left corner.
        #elem=driver.find_element_by_id("uh-logo").click()

# Closes current tab; if no other tabs are open, closes browser.
    def tearDown(self):
        self.driver.close()


# NOTE: I wanted to make a positive and a negative first test case to ensure that I am getting actual results
# This is the positive test
