from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

driver = webdriver.Chrome(options=chrome_options, executable_path='chromedriver.exe')
driver.get('https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb_azl')

deal_title_elems = driver.find_elements_by_css_selector('a#dealTitle >span')
deal_titles = []

for deal_title_elem in deal_title_elems:
    deal_titles.append(deal_title_elem.text)

price_elems = driver.find_elements_by_css_selector('span.dealPriceText')
prices = []
for price_elem in price_elems:
    prices.append(price_elem.text)

title_with_prices = dict(zip(deal_titles, prices))
print(title_with_prices)
