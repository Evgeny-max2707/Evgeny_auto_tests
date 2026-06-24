from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "https://suninjuly.github.io/execute_script.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	input = browser.find_element(By.ID, "answer")
	input.send_keys(y)
	checkbox = browser.find_element(By.ID, "robotCheckbox")
	browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
	checkbox.click()
	radiobatton = browser.find_element(By.ID, "robotsRule").click()
	submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
	time.sleep(10)
	browser.quit()
