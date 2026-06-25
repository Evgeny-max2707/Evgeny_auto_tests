import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration1(unittest.TestCase):
    """Тесты для страницы registration1 (с полем Last name)"""

    def setUp(self):
        """Предусловие: открыть браузер и страницу"""
        self.browser = webdriver.Chrome()
        self.link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(self.link)

    def tearDown(self):
        """Постусловие: закрыть браузер"""
        time.sleep(5)
        self.browser.quit()

    def test_registration_success(self):
        """Тест успешной регистрации на странице 1"""
        # Заполняем обязательные поля
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Вася")

        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Васильев")

        email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("test@example.com")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем результат
        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text,
                        f"Ожидался текст '{expected_text}', получен '{welcome_text}'")


class TestRegistration2(unittest.TestCase):
    """Тесты для страницы registration2 (без поля Last name)"""

    def setUp(self):
        """Предусловие: открыть браузер и страницу"""
        self.browser = webdriver.Chrome()
        self.link = "https://suninjuly.github.io/registration2.html"
        self.browser.get(self.link)

    def tearDown(self):
        """Постусловие: закрыть браузер"""
        time.sleep(5)
        self.browser.quit()

    def test_registration_success(self):
        """Тест успешной регистрации на странице 2"""
        # Заполняем обязательные поля
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Вася")

        # Поле Last name отсутствует на странице 2 — здесь будет исключение NoSuchElementException
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Васильев")

        # На странице 2 нет поля Last name, только email
        email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("test@example.com")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем результат
        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text,
                        f"Ожидался текст '{expected_text}', получен '{welcome_text}'")


if __name__ == "__main__":
    # Запускаем тесты с выводом подробной информации
    unittest.main(verbosity=2)