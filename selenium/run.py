import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # Optional: for headless mode
        options.add_argument('--no-sandbox')  # Optional: for environments with restricted permissions
        options.add_argument('--disable-dev-shm-usage')  # Optional: to avoid issues with /dev/shm

        # Define the desired capabilities (not used directly, but can be part of options if needed)
        capabilities = options.to_capabilities()

        # Create a WebDriver instance using Remote WebDriver
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options  # Pass options, not desired_capabilities
        )
       
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Python")

        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        print(driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()