import urllib.request

url='https://sports.news.naver.com/esports/news/read.nhn?oid=109&aid=0004053193'

mem=urllib.request.urlopen(url).read()
print(mem)
print(mem.decode('utf-8'))