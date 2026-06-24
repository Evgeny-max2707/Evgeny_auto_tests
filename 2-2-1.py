from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/selects1.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	dropdown = browser.find_element(By.ID, "dropdown").click()
	value = browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
	subbmit = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
	time.sleep(10)
	browser.quit()
