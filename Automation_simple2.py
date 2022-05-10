import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
elem = driver.find_element_by_name("search_query")
elem.send_keys("Dress")
elem.send_keys(Keys.RETURN)
button = driver.find_element_by_name("submit_search").click()
driver.close()









