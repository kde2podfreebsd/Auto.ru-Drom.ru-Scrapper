import schedule
import time

from auto import AutoParser
from drom import DromParser

def AutoParse():
    ap = AutoParser(price=85000, debug=True)
    ap.parse_page()
    print(ap.advertisement)
    return True


def DromParse():
    dp = DromParser(price=85000, debug=True)
    dp.parse_page()
    print(dp.advertisement)
    return True

def ParseSources():
    AutoParse()
    DromParse()


schedule.every(1).minutes.do(ParseSources)

while True:
    schedule.run_pending()
    time.sleep(1)
