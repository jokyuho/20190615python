import urllib.request
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
results=soup.select('span.value') # span태그에 클래스가 value인 것.
for result in results:
    print(result.string)

print('원달러 환율 : ', results[0].string)