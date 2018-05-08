# python3

# Test Case 3 - Top Header Functionality

# This is importing the necessary modules
# Unittest is for executing this script like a test case with a result at the end
# Selenium is the automated test module. Importing Keys allows inputs

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# This is building the actual test case
class yahoo_top_header(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("C:\\Users\\ryan.miller\\Desktop\\chronotester\\main\\uisrc\\selenium\\chromedriver.exe")
    def test_top_header_in_yahoo(self):
        driver=self.driver
        driver.get("http://www.yahoo.com/")
        self.assertIn("Yahoo", driver.title)

# Blow up that window
        driver.maximize_window()

# This is looking for the top header links, clicking them, and returning to the main page.
        elem=driver.find_element_by_link_text("Home").click()
        time.sleep(2)
        assert "Yahoo" in driver.title
        driver.back()

        elem=driver.find_element_by_link_text("Mail").click()
        time.sleep(2)
        assert "login" in driver.title
        driver.back()

        elem = driver.find_element_by_link_text("Flickr").click()
        time.sleep(2)
        assert "Flickr" in driver.title
        driver.back()

        elem = driver.find_element_by_link_text("Tumblr").click()
        time.sleep(2)
        assert "Tumblr" in driver.title
        driver.back()

        elem = driver.find_element_by_link_text("Entertainment").click()
        time.sleep(2)
        assert "Entertainment" in driver.title
        driver.back()

        elem = driver.find_element_by_link_text("Lifestyle").click()
        time.sleep(2)
        assert "Lifestyle" in driver.title
        driver.back()

        elem = driver.find_element_by_link_text("Mobile").click()
        time.sleep(2)
        assert "Mobile" in driver.title
        driver.back()

        elem = driver.find_element_by_link_text("View").click()
        time.sleep(2)
        assert "View" in driver.title
        driver.back()

        elem = driver.find_element_by_link_text("More").click()
        time.sleep(2)
        driver.back()


# Closes current tab; if no other tabs are open, closes browser.
    def tearDown(self):
        self.driver.close()

# This is the code to run the test suite.
if __name__ == "__main__":
    unittest.main()