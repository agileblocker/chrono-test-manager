# python3

# Test Case 4 - Search Bar Functionality

# This is importing the necessary modules
# Unittest is for executing this script like a test case with a result at the end
# Selenium is the automated test module. Importing Keys allows inputs

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# This is building the actual test case
class yahoo_searchbar(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_top_header_in_yahoo(self):
        driver=self.driver
        driver.get("http://www.yahoo.com/")
        self.assertIn("Yahoo", driver.title)

# Blow up that window
        driver.maximize_window()

# Verify enter search in search bar and hit enter key yields results page.
    #def verify_search_by_enter_key(self):
        time.sleep(3)
        driver.find_element_by_id("uh-search-box").send_keys("Chicago Python User Group", Keys.ENTER)
        time.sleep(3)
        assert "Chicago Python Usergroup" in driver.title
        time.sleep(2)
        driver.back()

# Verify enter search in search bar and click button yields results page.
    #def verify_search_by_search_button(self):
        time.sleep(3)
        driver.find_element_by_id("uh-search-box").send_keys("Ars Technica")
        time.sleep(2)
        driver.find_element_by_id("uh-search-button").click()
        time.sleep(3)
        assert "Ars Technica" in driver.title
        time.sleep(2)
        driver.back()



# Closes current tab; if no other tabs are open, closes browser.
    def tearDown(self):
        self.driver.close()

# This is the code to run the test suite.
# if __name__ == "__main__":
    # unittest.main()
