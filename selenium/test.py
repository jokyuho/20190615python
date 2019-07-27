import pymysql, re, time
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver as wd

driver = wd.Chrome(executable_path='selenium/data/chromedriver')
url = "https://movie.daum.net/premovie/released"
driver.get(url)
time.sleep(3)
response=  driver.page_source
soup = BeautifulSoup(response, 'lxml')
results = soup.select('.num_page')
print(results)
print(results[-1].text)
if len(results) == 1:
    page=1
else:
    page=int(results[-1].text)

movie_title = [] #영화제목
movie_genre = [] #영화연령
movie_img = []  #영화포스터
movie_img_Processing =[] #영화포스터주소(가공후)
movie_open = [] #영화오픈날짜
movie_story = [] #영화줄거리

for movie_page in range(1,page+1): # range는 마지막숫자 +1
    print(movie_page)
    url = "https://movie.daum.net/premovie/released?opt=reserve&page={}".format(movie_page)
    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html,'html.parser')
        
    #영화 타이틀 추출.
    movietitles = soup.find_all('a',class_='name_movie #title')
        
    for movietitle in movietitles:
        movie_title.append(movietitle.text)
        
    #영화 연령 추출
    movieGenres = soup.find_all('em',class_='ico_movie')
        
    for movieGenre in movieGenres:
        if movieGenre.text == "독점":
            continue
        else:
            movie_genre.append(movieGenre.text)
    #영화 이미지 추출
    movieImgs = soup.select("div span img")
        
    for movieImg in movieImgs:
        movie_img.append(movieImg['src'])

        #영화 평점 추출
        #movieScores = soup.find_all('span',class_='num_grade')
        #for moiveScore in movieScores:
            #print(moiveScore.text)

    #영화개봉날짜 추출
    movieOpens = soup.find_all('span',class_='info_state')

    #영화개봉날짜 정규표현씩 활용하여 추출.
    for movieOpen in movieOpens:
        movieOpen_cleand = re.sub('[a-zA-Z]' , '', movieOpen.text)
        movieOpen_cleand = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                        '', movieOpen.text)              
        movieOpen_cleand_final = movieOpen_cleand.split()
        movie_open.append(movieOpen_cleand_final[0])
        movieStorys = soup.find_all('a' , class_="desc_movie #synop")
        
    for movieStory in movieStorys:
        movieStory_cleand = movieStory.text.strip()
        movieStroy_cleand_final = movieStory_cleand.replace("\n","")
        movie_story.append(movieStroy_cleand_final)        
#영화이미지주소 가공
for moviesoso in range(len(movie_img)):
    movie_img_Processing.append(movie_img[moviesoso].replace("//img1.daumcdn.net/thumb/C236x340/?fname=","")) 

# print(movie_title) #영화제목
# print(movie_genre) #영화연령
# print(movie_img)  #영화포스터
# print(movie_img_Processing) #영화포스터주소(가공후)
# print(movie_open) #영화오픈날짜
# print(movie_story) #영화줄거리

conn=pymysql.connect(host='127.0.0.1',
user='root',
password='qwer1234',
db='movie',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

#데이터삭제 및 등록
try:
    with conn.cursor() as cursor:
        sql="delete from current_movie"
        cursor.execute(sql)
        conn.commit()
        for insert in range(len(movie_title)):    
            sql="insert into current_movie(current_movie_title,current_movie_img,current_movie_genre,current_movie_open,current_movie_story) values(%s,%s,%s,%s,%s);"
            cursor.execute(sql,(movie_title[insert],movie_img_Processing[insert],movie_genre[insert],movie_open[insert],movie_story[insert])) # insert는 인덱스 값
            conn.commit()
finally:
    conn.close()