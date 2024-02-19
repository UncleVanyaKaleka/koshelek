import time
import pytest
import chromedriver_autoinstaller
import Data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
chromedriver_autoinstaller.install()


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    # Переходим на страницу регистрации
    driver.get('https://koshelek.ru/authorization/signup')

    driver.maximize_window()
    yield driver

    driver.quit()


def test_negative_aut_password_upper_case(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.InvalidPasswordUpperCase)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Проверяем что появляется подсказка
    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > '
                         'div > div > div > div > span').text
    assert text == "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры"


def test_negative_aut_password_lower_case(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.InvalidPasswordLowerCase)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Проверяем что появляется подсказка
    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > '
                         'div > div > div > div > span').text
    time.sleep(2)
    assert text == "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры"


def test_negative_aut_password_cyrillic_alphabet(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.InvalidPasswordCyrillicAlphabet)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Проверяем что появляется подсказка
    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > '
                         'div > div > div > div > span').text
    assert text == "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры"


def test_negative_aut_password_special_characters(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.InvalidPasswordSpecialCharacters)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Проверяем что появляется подсказка
    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > '
                         'div > div > div > div > span').text
    assert text == "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры"


def test_negative_password_seven_characters(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.InvalidPasswordSevenCharacters)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Проверяем что появляется подсказка
    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > '
                         'div > div > div > div > span').text
    assert text == "Пароль должен содержать минимум 8 символов"


def test_negative_password_sixty_five_characters(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.InvalidPasswordSixtyFiveCharacters)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Проверяем что появляется подсказка
    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > '
                         'div > div > div > div > span').text
    assert text == "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры"


def test_negative_password_symbols_not_entered(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.InvalidPasswordSymbolsNotEntered)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Проверяем что появляется подсказка
    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > '
                         'div > div > div > div > span').text
    assert text == "Поле не заполнено"


def test_negative_email_cyrillic_alphabet(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.InvalidEmailCyrillicAlphabet)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.password)
    # Проверяем что появляется подсказка

    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(2) > div > div > div.v-text-field__details > div > div > div >'
                         ' div > div > span').text
    assert text == "Формат e-mail: somebody@somewhere.ru"


def test_negative_email_not_entered(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.login)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.InvalidEmailSymbolsNotEntered)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.password)

    # Проверяем что появляется подсказка

    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(2) > div > div > div.v-text-field__details > div > div > div >'
                         ' div > div > span').text
    assert text == "Поле не заполнено"



def test_negative_login_upper_case(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.InvalidLoginUpperCase)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.password)
    # Проверяем что появилась ошибка введеном логине
    wdw(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div > div > div > div > div.k-text-k-typography-body-2-regular')))


def test_negative_login_cyrillic_alphabet(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.InvalidLoginCyrillicAlphabet)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.password)
    # Проверяем что появилась ошибка введеном логине
    wdw(driver, 60).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div > div > div > div > div.k-text-k-typography-body-2-regular')))


def test_negative_login_symbols_not_entered(driver):
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-header"]/div[1]/a/div/div[3]')))
    shadow_root = driver.find_element(By.XPATH, '//*[@id="attach_modal"]/section/div/div[2]/div').shadow_root
    # вводим логин
    shadow_root.find_element(By.CSS_SELECTOR, '#input-127').send_keys(Data.InvalidLoginSymbolsNotEntered)
    # вводим email
    shadow_root.find_element(By.CSS_SELECTOR, '#username').send_keys(Data.email)
    # Вводим пароль
    shadow_root.find_element(By.CSS_SELECTOR, '#new-password').send_keys(Data.password)
    # Проверяем что появляется подсказка

    text = shadow_root.find_element(
        By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > '
                         'form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div > div > '
                         'div > div > span').text
    time.sleep(2)
    assert text == 'Поле не заполнено'


