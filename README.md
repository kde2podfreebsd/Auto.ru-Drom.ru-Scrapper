# Parser_Avito-Auto.ru-Drom.ru-Ula_TgBot
Auto.ru, Drom.ru, Avito.ru, Ula.ru auto parser + tg bot
---------------------------
#### Auto.ru:
1) Необходимо сохранение cookie в сессию для обхода re-captcha
2) Все параметры поиска конфигурируются в url кроме радиуса поиска (радиус конфигурируется в cookie)
3) На последней странице поиска убирает все объявления с бесконечным поиском не попадающими под поисковый запрос
```.js
const remove = (sel) => document.querySelectorAll(sel).forEach(el => el.remove()); remove(".ListingInfiniteDesktop__snippet");
```
4) При отсутсвии элементов на странице заканчивает парсинг и заносит результат в бд (добавляет новые посты)

#### Drom.ru:
1) Все параметры поиска конфигурируются в url
2) Скрол страниц идет до первого совпадения объявления с бд
---------------------------
#### Создание сессии с cookie для Auto.ru
##### app.services.parser
```.py
p = Parser()
p.create_session(url = <auto.ru search configured url>)
```
##### Pass Re-Captcha and configure search radius; Session will be saved in app.sessions.auto
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
