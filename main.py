import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
driver.get("https://newdesign.millionandup.com/")
elem = driver.find_element_by_name("email")
elem.send_keys("csf1075@gmail.com")
elem = driver.find_element_by_name("name")
elem.send_keys("Cirley Salazar")
elem = driver.find_element_by_name("phone")
elem.send_keys("3057367765")
button = driver.find_element_by_id("btnSendModal").click()
elem = driver.find_element_by_class_name("icon-arrow-down").click()
elem = driver.find_element_by_css_selector(".fc-icon.fc-icon-chevron-right").click()
elem = driver.find_element_by_xpath("//a[text()='18' and @class='fc-daygrid-day-number']").click()
elem = driver.find_element_by_xpath("//li[@class='options li-selected'][1]").click()

#Por aca estuvo Jonathan.






