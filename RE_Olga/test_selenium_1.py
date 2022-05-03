import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestMePlease(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        # Initialisation
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(1024, 768)

    def test_1(self):
        # test
        self.driver.get("https://www.google.com/")

    def test_2(self):
        # test
        self.driver.get("https://www.google.com/")

    def tearDown(self) -> None:
        # destroy driver instance
        self.driver.close()

if __name__ == '__main__':
    unittest.main()