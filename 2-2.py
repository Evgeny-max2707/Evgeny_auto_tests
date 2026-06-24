from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
link = "http://suninjuly.github.io/selects1.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	time.sleep(5)
	x = browser.find_element(By.ID, "num1")
	y = browser.find_element(By.ID, "num2")
	def sum(x, y):
		return result_sum = str(x + y)
	print(f"Найдены числа: {x} и {y}. Сумма: {result_sum}")
	select = Select(browser.find_element(By.ID, "dropdown")
	select.select_by_value("result_sum")
	button = browser.find_element(By.CSS_SELECTOR, "result_sum")
	button.click()
finally:
	time.sleep(10)
	browser.quit()
		