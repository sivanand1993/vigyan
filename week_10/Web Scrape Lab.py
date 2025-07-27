# amazon deal of the day
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import amazon as am

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

driver=webdriver.Chrome(options=chrome_options,executable_path='chromedriver.exe')

driver.get('https://www.amazon.com/events/holidaydash?ref_=nav_td_dash_dt_cr')

deal_title_elems =driver.find_element_by_css_selector('#dealTitle > span')
deal_titles=[]
for deal_title_elem in deal_title_elems:
    deal_titles.append(deal_title_elem)

price_elems=driver.find_element_by_css_selector('.priceBlock > span')
prices=[]

for price_elem in price_elems:
    prices.append(price_elem)

title_with_prices=dict(zip(deal_titles,prices))

print(title_with_prices)
print(len(title_with_prices))

amazon = am.Amazon()
amazon.reset_database() # only need to call this one unless you want to drop your table everytime.

for key, value in title_with_prices.items():
    amazon.add(key, value)