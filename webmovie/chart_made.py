import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

df = pd.read_csv('webmovie/cine.csv',engine='python',encoding='utf-8')
'''
temp = df.groupby('movieNm').sum()
print(temp)
mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
plt.bar(temp.index, temp['audiAcc']) 
plt.title('영화명(movieNm)별 총 매출액 막대 그래프')
plt.xlabel('영화명')
plt.ylabel('관객수')
plt.xticks(fontsize=6, rotation=90)
plt.show()
'''
'''
temp = df.groupby('movieNm').sum()
temp = temp.sort_values(by='audiAcc', ascending=0)
temp = temp.iloc[:10]
print(temp)
mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
mpl.rcParams['font.size'] = 9
plt.pie(temp['audiAcc'], labels=temp.index, autopct='%.1f%%', shadow=True)
plt.title('2019년 총 관람객 상위 10개의 영화명(movieNm) 파이 차트')
plt.show()
'''
date = pd.read_csv('webmovie/cine.csv', engine='python')
date.info()
print(date.head(3))
date = date.sort_index(by='targetDt', ascending=True)
print(date.head(3))


temp1 = date[date['movieNm'] == '기생충']

print(temp1)

temp2 = df[df['movieNm'] == '알라딘']
print(temp2)

mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
fig = plt.figure()
fig.set_size_inches(9.4,4.8)
#분할해 그리기 시작
axe = fig.add_subplot(1,2,1) #1행(row) 2열(column)중 첫 번째 subplot
axe.plot([str(x) for x in temp1['targetDt']], temp1['audiCnt'],label='기생충')
axe.set_title('기생충')
axe.set_xlabel('날짜')
axe.set_ylabel('관객수')
for tick in axe.xaxis.get_major_ticks():
    tick.label.set_fontsize(6) 
    tick.label.set_rotation(90)
axe = fig.add_subplot(1,2,2) #1행(row) 2열(column)중 두번째 subplot
axe.plot([str(x) for x in temp2['targetDt']], temp2['audiCnt'],label='알라딘')
axe.set_title('알라딘')
axe.set_xlabel('날짜')
axe.set_ylabel('관객수')
for tick in axe.xaxis.get_major_ticks():
    tick.label.set_fontsize(6) 
    tick.label.set_rotation(90)
plt.suptitle('영화명 "기생충"의 일별 관객과 영화명 "알라딘"의 일별 관객 선 그래프')
#분할해 그리기 끝
plt.show()
