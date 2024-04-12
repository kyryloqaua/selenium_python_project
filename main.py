from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service)

driver. get("https://google.com")

first_element_input = driver.find_element(by=By.CLASS_NAME, value="gLFyf")

first_element_input.clear
first_element_input.send_keys("fairmont sanfrancisco" + Keys.ENTER)

WebDriverWait(driver,10). until (
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)


link = driver.find_element(By.PARTIAL_LINK_TEXT,"Luxury Hotel in San Francisco")

WebDriverWait(driver,10).until(
    EC.presence_of_element_located ((By.PARTIAL_LINK_TEXT,"Luxury Hotel in San Francisco"))
)
link.click()


WebDriverWait(driver,10).until(
    EC.presence_of_element_located ((By.CLASS_NAME,"book-btn-wrap"))
)


check_link = driver.find_element(By.CLASS_NAME,"book-btn-wrap")

check_link.click()

WebDriverWait(driver,10).until(
    EC.presence_of_element_located ((By.CLASS_NAME,"primary-button"))
)

select_room = driver.find_element(By.CLASS_NAME,"primary-button")

select_room.click()

WebDriverWait(driver,10).until(
    EC.presence_of_element_located ((By.LINK_TEXT,"CHOOSE THIS RATE"))
)

select_rate = driver.find_element(By.LINK_TEXT,"CHOOSE THIS RATE")
select_rate.click()


time.sleep(10)

driver.quit
