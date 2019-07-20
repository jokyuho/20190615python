import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
req = urllib.request.urlopen(url)
res = req.read()

soup = BeautifulSoup(res, 'html.parser')
keywords = soup.find_all('span', class_='ah_k')
# get_text() == 데이터에서 문자열만 추출
# strip() == 데이터의 양옆 공백제거
# [:20]의 이유? == 인기검색어의 중복을 막고 20위까지만 출력하기 위함

keywords = [each_line.get_text().strip() for each_line in keywords[:20]]
print(keywords)

# results=soup.select("ul > li > a > span.ah_k")

#for result in results:
    # print(result.string)