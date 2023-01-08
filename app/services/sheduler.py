import schedule
import time

from auto import AutoParser
from drom import DromParser
import json

def AutoParse():
    with open('../data.json') as json_file:
        data = json.load(json_file)
    ap = AutoParser(price=int(data['price']), debug=True)
    ap.parse_page()
    print(ap.advertisement)
    return True


def DromParse():
    with open('../data.json') as json_file:
        data = json.load(json_file)
    dp = DromParser(price=int(data['price']), debug=True)
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
    print('sleep...')

