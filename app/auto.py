import os
import time

from selenium.webdriver.common.by import By

from parser import Parser, basedir

class AutoParser(Parser):
    def __init__(self):
        Parser.__init__(self, service="auto", debug=True)
        self.price = 85000
        self.advertisement = dict()
        self.url = f'https://auto.ru/moskva/cars/all/?top_days=2&price_to={self.price}&with_discount=false&sort=cr_date-desc&damage_group=ANY&page='

    def parse_page(self):
        try:
            page = 0
            while True:
                page += 1
                print(page)
                if page == 1:
                    self.load_cookie(url=self.url+str(page))
                else:
                    self.driver.get(url=self.url+str(page))

                # delete infinity advertisement scrolling
                self.driver.execute_script('const remove = (sel) => document.querySelectorAll(sel).forEach(el => el.remove()); remove(".ListingInfiniteDesktop__snippet");')

                href = self.driver.find_elements(by=By.XPATH, value='//a[@class="Link ListingItemTitle__link"]')
                if len(href) != 0:
                    price = self.driver.find_elements(by=By.XPATH, value='//div[@class="ListingItemPrice__content"]')
                    tech_details = self.driver.find_elements(by=By.XPATH, value='//div[@class="ListingItemTechSummaryDesktop ListingItem__techSummary"]')
                    mileage = self.driver.find_elements(by=By.XPATH, value='//div[@class="ListingItem__kmAge"]')
                    year = self.driver.find_elements(by=By.XPATH, value='//div[@class="ListingItem__yearBlock"]')

                    ad_href = list(map(lambda x: x.get_attribute('href'), href))
                    ad_name = list(map(lambda x: x.text, href))
                    ad_price = list(map(lambda x: x.text, price))
                    ad_details = list(map(lambda x: x.text, tech_details))
                    ad_milage = list(map(lambda x: x.text, mileage))
                    ad_year = list(map(lambda x: x.text, year))

                    for i in range(len(ad_href)):
                        self.advertisement[ad_href[i]] = {
                            "href": ad_href[i],
                            "name": ad_name[i],
                            "price": ad_price[i],
                            "details": ad_details[i],
                            "milage": ad_milage[i],
                            "year": ad_year[i],
                        }
                else:
                    break

            print(self.advertisement)


        except Exception as e:
            return e

        # finally:
        #     self.close_parser()

ap = AutoParser()
ap.parse_page()
print(ap.advertisement)