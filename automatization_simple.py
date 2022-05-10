import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
driver.get("http://thedemosite.co.uk/savedata.php")
elem = driver.find_element_by_name("username")
elem.send_keys("cirley")
elem = driver.find_element_by_name("password")
elem.send_keys("123456")
button = driver.find_element_by_name("FormsButton2").click()
driver.close()



