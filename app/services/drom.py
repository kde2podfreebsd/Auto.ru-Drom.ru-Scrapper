from typing import Optional
from selenium.webdriver.common.by import By
from parser import Parser

class DromParser(Parser):
    def __init__(self, price: int, debug: Optional[bool] = False):
        Parser.__init__(self, service="drom", debug=debug)
        self.price = price
        self.advertisement = dict()
        self.url = f'https://moscow.drom.ru/auto/all/page2/?maxprice={self.price}&ph=1&unsold=1&distance=100'

    def parse_page(self):
        try:
            self.driver.get(url=self.url)

            href = self.driver.find_elements(by=By.XPATH, value='//a[@class="css-xb5nz8 ewrty961"]')
            price = self.driver.find_elements(by=By.XPATH, value='//span[@data-ftid="bull_price"]')
            title = self.driver.find_elements(by=By.XPATH, value='//span[@data-ftid="bull_title"]')
            details = self.driver.find_elements(by=By.XPATH, value='//div[@class="css-1fe6w6s e162wx9x0"]')

            ad_href = list(map(lambda x: x.get_attribute('href'), href))
            ad_price = list(map(lambda x: x.text, price))
            ad_details = list(map(lambda x: x.text, details))
            ad_title = list(map(lambda x: x.text, title))

            for i in range(len(ad_href)):
                self.advertisement[ad_href[i]] = {
                    "href": ad_href[i],
                    "name": ad_title[i],
                    "price": ad_price[i],
                    "details": ad_details[i]
                }


        except Exception as e:
            return e

        finally:
            self.close_parser()



#
dp = DromParser(price=85000, debug=True)
dp.parse_page()
print(dp.advertisement)