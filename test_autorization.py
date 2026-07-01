import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

LESSONS = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

secret_message_parts = []

@pytest.fixture(scope="session")
def authorized_browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    
    browser.get("https://stepik.org/lesson/236895/step/1")
    wait = WebDriverWait(browser, 30)
    
    try:
        button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Войти"))).click()
        email = browser.find_element(By.ID, "id_login_email")
        email.send_keys("dust-06@mail.ru")
        pas = browser.find_element(By.ID, "id_login_password")
        pas.send_keys("Uld270781!")
        button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        time.sleep(5)
        print("Авторизация успешна")
    except:
        print("Уже авторизованы")
    
    yield browser
    browser.quit()

@pytest.mark.parametrize("link", LESSONS)
def test_autorization(authorized_browser, link):
    global secret_message_parts
    
    browser = authorized_browser
    browser.get(link)
    wait = WebDriverWait(browser, 30)
    time.sleep(5)
    
    # Вычисление ответа
    answer = math.log(int(time.time()))
    print(f"\nОтвет для {link}: {answer}")
    
    # Ввод ответа через JavaScript (единственный надежный способ для Ember.js)
    try:
        # Ждем появления поля
        fild = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area")))
        
        # Используем JavaScript для установки значения и триггера событий Ember
        browser.execute_script("""
            var element = arguments[0];
            var value = arguments[1];
            
            // Фокусируемся на элементе
            element.focus();
            
            // Устанавливаем значение через нативный сеттер
            var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
            nativeSetter.call(element, value);
            
            // Триггерим события для Ember
            element.dispatchEvent(new Event('input', { bubbles: true }));
            element.dispatchEvent(new Event('change', { bubbles: true }));
            
            // Дополнительные события для Ember
            element.dispatchEvent(new KeyboardEvent('keydown', { bubbles: true }));
            element.dispatchEvent(new KeyboardEvent('keypress', { bubbles: true }));
            element.dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));
        """, fild, str(answer))
        
        print("Ответ введен через JavaScript")
        time.sleep(3)
        
        # После ввода должна появиться кнопка "Отправить"
        # Ищем её и кликаем
        buttons = browser.find_elements(By.TAG_NAME, "button")
        submit_found = False
        
        for btn in buttons:
            if "Отправить" in btn.text:
                print(f"Найдена кнопка: '{btn.text}'")
                browser.execute_script("arguments[0].click();", btn)
                submit_found = True
                print("Клик по кнопке Отправить")
                break
        
        if not submit_found:
            # Если кнопка не найдена, пробуем отправить через JavaScript
            print("Кнопка не найдена, отправка через JavaScript")
            browser.execute_script("""
                var buttons = document.querySelectorAll('button');
                for(var i = 0; i < buttons.length; i++) {
                    if(buttons[i].textContent.includes('Отправить')) {
                        buttons[i].click();
                        return;
                    }
                }
                // Если кнопка так и не нашлась, ищем форму и сабмитим
                var form = document.querySelector('form');
                if(form) form.submit();
            """)
        
        time.sleep(5)
        
    except Exception as e:
        print(f"Ошибка при вводе: {e}")
        return
    
    # Получение фидбека
    try:
        feedback_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        feedback_text = feedback_element.text
        print(f"ФИДБЕК: '{feedback_text}'")
        
        # Извлекаем часть послания
        if "Correct!" in feedback_text:
            if ":" in feedback_text:
                parts = feedback_text.split(":", 1)
                if len(parts) > 1:
                    message_part = parts[1].strip()
                    secret_message_parts.append(message_part)
                    print(f"Извлечена часть послания: '{message_part}'")
        
        # ТЕСТ ДОЛЖЕН УПАСТЬ, ЕСЛИ НЕТ "Correct!"
        assert "Correct!" in feedback_text, f"Для {link} получен фидбек: '{feedback_text}'"
        
    except Exception as e:
        print(f"Ошибка получения фидбека: {e}")
        raise

# Вывод послания после тестов
def pytest_sessionfinish(session, exitstatus):
    print("\n" + "="*60)
    print("СОБРАННОЕ СЕКРЕТНОЕ ПОСЛАНИЕ:")
    full_message = " ".join(secret_message_parts)
    print(full_message)
    print("="*60)
    print(f"\nКоличество частей: {len(secret_message_parts)}")