import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestFairmontSanFrancisco:
    def setup_method(self):
        self.service = webdriver.ChromeService()
        self.driver = webdriver.Chrome(service=self.service)
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_booking_process(self):
        self.driver.get("https://google.com")
        search_input = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search_input.clear()
        search_input.send_keys("Fairmont San Francisco" + Keys.ENTER)

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
        )

        link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Luxury Hotel in San Francisco")
        self.wait.until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Luxury Hotel in San Francisco"))
        )
        link.click()

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "book-btn-wrap"))
        )
        check_link = self.driver.find_element(By.CLASS_NAME, "book-btn-wrap")
        check_link.click()

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "primary-button"))
        )
        select_room = self.driver.find_element(By.CLASS_NAME, "primary-button")
        select_room.click()

        self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "CHOOSE THIS RATE"))
        )
        select_rate = self.driver.find_element(By.LINK_TEXT, "CHOOSE THIS RATE")
        select_rate.click()

        time.sleep(10)
        # Assertions to verify that elements are as expected
        assert "CHOOSE THIS RATE" in self.driver.page_source

    def test_title(self):
        self.driver.get("https://google.com")
        assert "Google" in self.driver.title

# To run this test, you would use the command line:
#pytest -v test_script.py
