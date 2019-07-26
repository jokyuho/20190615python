import urllib.request, db
from bs4 import BeautifulSoup

def lionking_comment():
    params=urllib.parse.urlencode({'page':1})
    url = 'https://movie.naver.com/movie/bi/mi/point.nhn?code=169637%s' %params
    print(url)

    response = urllib.request.urlopen(url)
    navigator=BeautifulSoup(response, 'html.parser')
    table=navigator.find('div', class_='score_result')
    print(table)

    list_records=[]
    for i,r in enumerate(table.find_all('li')): # i는 인덱스 r은 tr 개체
        for j,c in enumerate(r.find_all('div')): # j는 인덱스값 c는 개체
            if j==1:
                record1=int(c.text.strip())
            elif j==2:
                record2=str(c.find('a', class_='movie').text.strip())
                record3=str(c.text).split("\n")[2]
            elif j==3:
                record4=str(c.find('a', class_='author').text.strip())
                record5=str(c.text).split("****")[1]
        try:
            record_t=tuple([record1, record2, record3, record4, record5])
            list_records.append(record_t)
        except:
            pass

    print(list_records)

    db.conn_db()
    db.create_table3()
    db.insert_lionking(list_records)
