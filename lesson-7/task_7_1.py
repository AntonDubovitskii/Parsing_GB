"""
Задание:

Любая работа с JS на сайте со сбором данных, обсуждение на вебинаре

Пояснение:

Преподаватель на видео сказал подергать любую информацию с любых сайтов при помощи
Selenium, лишь бы там был динамический контент.

Поэтому я сделал логин на сайт pikabu.ru, прокрутку ленты и сохранение ссылок на статьи с высоким рейтингом из неё.
"""
import json

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://pikabu.ru')
driver.implicitly_wait(15)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Логин']")))

login = driver.find_element(By.XPATH, "//input[@placeholder='Логин']")
login.send_keys("GbSel")

password = driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
password.send_keys("t137946")
password.send_keys(Keys.ENTER)

actions = ActionChains(driver)
links_list = []
objs = {}

for i in range(500):
    # Так как статьи на данном сайте подгружаются при скролле, то прокручиваем к последней статье, после которой
    # подгрузятся новые
    articles = driver.find_elements(By.TAG_NAME, "article")
    control_article = articles[-1]

    actions.move_to_element(control_article)
    actions.perform()

    print(i)

for article in articles:
    try:
        article_rate = int(article.find_element(By.XPATH, ".//div[@class='story__rating-count']").text)
        if article_rate >= 1000:
            links_list.append(article.find_element(By.XPATH, ".//a[@class='story__title-link']").get_property('href'))
    except Exception:
        continue

for number, link in enumerate(links_list):
    objs[number] = link

with open('pikabu_links.json', 'w', encoding='utf-8') as f:
    json.dump(objs, f, indent=4, ensure_ascii=False)
