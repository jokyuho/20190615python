# 웹페이지의 내용을 분석하여 csv파일로 저장
# <table> 내부의 텍스트 저장
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo#playerRanking')
soup = BeautifulSoup(html, 'html.parser')

# class가 wikitable인 태그들 중에서 첫번째 태그 선택

table = soup.find_all('div', {'class':'tbl_box p_head'})[0]
rows=table.find_all('tr')

# wt:텍스트 쓰기 모드
csvFile=open('./python_basic/baseball.csv', 'wt', newline = '', encoding = 'utf-8')

# csv 파일 저장 객체
write = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        # td, th 태그의 내용을 리스트에 추가
        for cell in row.find_all(['td','th']):
            csvRow.append(cell.get_text())
        write.writerow(csvRow)

finally:
    print('csv로 저장되었습니다.')
    csvFile.close()