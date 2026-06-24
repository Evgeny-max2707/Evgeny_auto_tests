from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "https://suninjuly.github.io/get_attribute.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	x_element = browser.find_element(By.ID, "treasure")
	x = x_element.get_attribute("valuex")
	y = calc(x)
	input = browser.find_element(By.ID, "answer")
	input.send_keys(y)
	checkbox = browser.find_element(By.ID, "robotCheckbox")
	checkbox.click()
	radiobutton = browser.find_element(By.ID, "robotsRule")
	radiobutton.click()
	submitt = browser.find_element(By.CSS_SELECTOR, "button.btn")
	submitt.click()
finally:
	time.sleep(10)
	browser.quit()
