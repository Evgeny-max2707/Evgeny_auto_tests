from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
link = "https://suninjuly.github.io/file_input.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
	first_name.send_keys("Вася")
	last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
	last_name.send_keys("Васильев")
	mail = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
	mail.send_keys("qwe@mail.ru")
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'try.txt')
	file_input = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
	file_input.send_keys(file_path)
	submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
	time.sleep(10)
	browser.quit()