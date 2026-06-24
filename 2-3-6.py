from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "https://suninjuly.github.io/redirect_accept.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
	windows = browser.window_handles
	browser.switch_to.window(windows[1])
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	answer = browser.find_element(By.ID, "answer")
	answer.send_keys(y)
	submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
	time.sleep(20)
	browser.quit()