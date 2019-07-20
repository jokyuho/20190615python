import urllib.request
import urllib.parse
# https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%98%B8%ED%85%94+%EB%8D%B8%EB%A3%A8%EB%82%98
api = 'https://search.naver.com/search.naver'
values={
    'sm' : 'top_hty',
    'fbm' : '1',
    'ie' : 'utf8',
    'query' : '장마'
}

params = urllib.parse.urlencode(values)
url = api + '?' + params
data=urllib.request.urlopen(url).read()
text=data.decode('utf-8')
print(url)
print(text)