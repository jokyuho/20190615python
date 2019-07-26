from bs4 import BeautifulSoup

import requests

starbugs = requests.get('https://www.istarbucks.co.kr/store/store_map.do')

st_bs=BeautifulSoup(starbugs.text,'lxml')

print(st_bs.select('li.quickResultLstCon'))

driver = webdriver.Chrome('./crawling/data/chromedriver')
driver.get('https://www.istarbucks.co.kr/store/store_map.do')
