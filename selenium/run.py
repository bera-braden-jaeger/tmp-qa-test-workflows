import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestExample(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run tests in headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)

    def test_google_search(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)
        print(self.driver.title)
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium")
        search_box.submit()
        # self.assertTrue("Selenium" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
