from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
link = "https://suninjuly.github.io/selects1.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element(By.ID, "num1")
	y_element = browser.find_element(By.ID, "num2")
	x = int(x_element.text)
	print(x)
	y = int(y_element.text)
	print(y)
	sum_value = str(x + y)
	print(sum_value)
	select = Select(browser.find_element(By.TAG_NAME, "select"))
	select.select_by_value(sum_value)
	browser.find_element(By.CSS_SELECTOR, "button.btn").click()
	alert = browser.switch_to.alert
	answer = alert.text
	print(f"Число-ответ: {answer}")
finally:
	time.sleep(10)
	browser.quit()