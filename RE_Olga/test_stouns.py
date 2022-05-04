import unittest

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestRocks(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        # Initialisation
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_stones(self):
            self.driver.get("https://techstepacademy.com/trial-of-the-stones")
            # step1 input 'rock'
            input_1 = self.driver.find_element(By.ID, 'r1Input')
            input_2 = self.driver.find_element(By.ID, 'r2Input')

            btn_answer_1 = self.driver.find_element(By.ID, 'r1Btn')
            btn_answer_2 = self.driver.find_element(By.ID, 'r2Butn')

            answer_1 = self.driver.find_element(By.CSS_SELECTOR, '#passwordBanner h4')
            answer_2 = self.driver.find_element(By.CSS_SELECTOR, '#successBanner1 h4')

            input_1.send_keys('rock')
            btn_answer_1.click()
            text_password_1 = answer_1.text

            input_2.send_keys(text_password_1)
            btn_answer_2.click()
            text_banner_2 = answer_2.text

            expected_answer = 'Success!'
            self.assertTrue(text_banner_2, expected_answer)

            # def test_merchants_(self):
            merchant_1 = self.driver.find_element(By.XPATH, '(//div/span/b)[1]').text
            merchant_2 = self.driver.find_element(By.XPATH, '(//div/span/b)[2]').text
            total_wealth_1 = self.driver.find_element(By.XPATH, '(// div / span / b)[1] /../../ p')
            total_wealth_2 = self.driver.find_element(By.XPATH, '(// div / span / b)[2] /../../ p')

            merch_1 = int(total_wealth_1.text)
            merch_2 = int(total_wealth_2.text)

            if (merch_1 > merch_2):
                    richest = merchant_1
            else:
                richest = merchant_2

            input_3 = self.driver.find_element(By.ID, "r3Input")
            input_3.send_keys(richest)

            btn_answer_3 = self.driver.find_element(By.ID, 'r3Butn')
            btn_answer_3.click()

            answer_3 = self.driver.find_element(By.CSS_SELECTOR, '#successBanner2 h4')
            text_answer_3 = answer_3.text


            self.assertEqual(text_answer_3, expected_answer)

            btn_check_answers = self.driver.find_element(By.ID, 'checkButn')
            btn_check_answers.click()

            text_check_answers = self.driver.find_element(By.CSS_SELECTOR, '#trialCompleteBanner>h4').text
            expected_answer = "Trial Complete"
            self.assertTrue(text_check_answers == expected_answer)

            time.sleep(5)


def tearDown(self) -> None:
    # destroy driver instance
        self.driver.close()


if __name__ == '__main__':
     unittest.main()