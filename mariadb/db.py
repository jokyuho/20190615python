import pymysql

def conn_db():
    conn = pymysql.connect(host='localhost',
                             user='root',
                             password='qwer1234',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return conn


#테이블 생성 함수
def create_table():
    conn=conn_db()
    cursor=conn.cursor()
    # my_books테이블 생성(글번호,평점,영화제목,140자평,날짜)
    # (no integer, grade integer, title text, content text, writer text, date text)
    cursor.execute('''create table if not exists movie(
        no int NOT NULL, 
        grade int,
        title varchar(255),
        content varchar(300),
        writer varchar(30),
        date varchar(20)
        )''')
    conn.commit()
    conn.close()

#전체 데이터 출력 함수
def all_users():
    conn=conn_db()
    cursor=conn.cursor()
    cursor.execute("select * from movie")
    items=cursor.fetchall()
    print(len(items)) #레코드 개수 출력
    print(items)
    conn.close()
    return items


#데이터 입력 함수
def insert_movie(items):
    conn=conn_db()
    cursor=conn.cursor()
    sql='INSERT INTO movie VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()

