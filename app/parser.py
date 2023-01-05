import os
import time
import pickle
from typing import Optional
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.service import Service

basedir = os.path.abspath(os.path.dirname(__file__))


class Parser:
    __instance = None

    def __init__(self, debug: Optional[bool] = False):
        if not Parser.__instance:
            self.__ser = Service(f'{basedir}/geckodriver')
            self.__op = webdriver.FirefoxOptions()
            self.__op.add_argument("--no-sandbox")
            self.__op.add_argument("--disable-dev-shm-usage")
            # self.__op.add_argument(f"--log-path={basedir}/logs/parser.log")
            self.__display = Display(visible=debug, size=(800, 800))
            self.__display.start()
            self.driver = webdriver.Firefox(basedir)

        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Parser()
        return cls.__instance

p = Parser(debug=True)
p.driver.get(url="https://auto.ru/moskva/cars/used/?top_days=2&price_to=85000")

# save cookie
# time.sleep(45)
# pickle.dump(p.driver.get_cookies(), open('session', 'wb'))

for cookie in pickle.load(open('sessions/session', 'rb')):
    p.driver.add_cookie(cookie)

print('all loaded')
p.driver.get(url="https://auto.ru/moskva/cars/used/?top_days=2&price_to=85000")
