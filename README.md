# Parser_Avito-Auto.ru-Drom.ru-Ula_TgBot
Auto.ru, Drom.ru, Avito.ru, Ula.ru auto parser + tg bot
---------------------------
#### Auto.ru:
1) Необходимо сохранение кукис в сессию для обхода re-captcha
1) Все параметры поиска конфигурируются в url кроме радиуса поиска (радиус конфигурируется в кукис)
2) На последней странице поиска убирает все объявления с бесконечным поиском не попадающими под поисковый запрос
3) при отсутсвии элементов на странице заканчивает парсинг и заносит результат в бд (добавляет новые посты)

#### Drom.ru:
1) Все параметры поиска конфигурируются в url
2) Скрол страниц идет до первого совпадения объявления с бд
---------------------------

#### Edit Selenium webdriver source
```.txt
Edit in webdriver.py (from webdriver.Firefox) DEFAULT_SERVICE_LOG_PATH to = "logs/geckodriver.log"
```

#### Install deps on your system for virtual display (requires by cli server)
##### For arch linux
```.sh
yay xvfb
yay Xephyr
```
