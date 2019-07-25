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
    #customer 테이블 생성(아이디,이메일,주소,비밀번호,고유값)
    cursor.execute('''create table if not exists users(
        userid varchar(11) NOT NULL, 
        email varchar(255)  NOT NULL,
        address varchar(255),
        password varchar(255)  NOT NULL,
        PRIMARY KEY (userid)
        )''')
    conn.commit()
    conn.close()

#전체 데이터 출력 함수
def all_users():
    conn=conn_db()
    cursor=conn.cursor()
    cursor.execute("select * from users")
    users=cursor.fetchall()
    print(len(users)) #레코드 개수 출력
    print(users)
    conn.close()
    return users


#데이터 입력 함수
def insert_users(user):
    conn=conn_db()
    cursor=conn.cursor()
    sql='insert into users values(%s,%s,%s,%s)'
    cursor.execute(sql,user)
    conn.commit()
    conn.close()


def one_user(userid):
    conn=conn_db()
    cursor=conn.cursor()
    sql='select * from users where userid=%s'
    cursor.execute(sql,userid)
    user=cursor.fetchone()
    conn.commit()
    conn.close()
    return user

def delete_user(userid):
    conn=conn_db()
    cursor=conn.cursor()
    sql='delete from users where userid=%s'
    cursor.execute(sql,userid)
    conn.commit()
    conn.close()

def update_user(user):
    conn=conn_db()
    cursor=conn.cursor()
    print(user)
    sql='''update users 
            set email=%s,
                address=%s,
                password=%s
            where userid=%s
        '''
    cursor.execute(sql,(user['email'],user['address'],user['password'],user['userid']))
    conn.commit()
    conn.close()


#테이블 생성 함수
def create_table2():
    conn=conn_db()
    cursor=conn.cursor()
    # movie테이블 생성(글번호,평점,영화제목,140자평,날짜)
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
def users_comment():
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