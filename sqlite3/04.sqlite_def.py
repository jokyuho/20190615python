import sqlite3

#테이블 생성 함수
def create_table():
    conn=sqlite3.connect('my_books.db')
    cursor=conn.cursor()
    #my_books테이블 생성(제목,출판일자,출판사,페이지수,추천여부)
    cursor.execute('''create table if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer
        )''')
    conn.commit()
    conn.close()
#테이블 생성 함수 호출
create_table()
#데이터 입력 함수
def insert_books():
    conn=sqlite3.connect("my_books.db") #db연결
    cursor=conn.cursor()
    #데이타 입력방법1
    cursor.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    #데이타 입력방법2
    sql='insert into books values(?,?,?,?,?)'
    cursor.execute(sql,('Python','201001','한빛',584,20))
    #데이타 입력방법3
    items=[('빅데이터','2014-07-02','삼성',296,11), ('안드로이드','2010-02-02','삼성',526,20), ('spring','2013-12-02','삼성',248,15)]
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()
#데이터 입력 함수 호출
insert_books()
#전체 데이터 출력 함수
def all_books():
    conn=sqlite3.connect("my_books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books")
    print('[1] 전체 데이터 출력하기')
    books=cursor.fetchall()
    print(type(books))
    print(len(books)) #레코드 개수 출력

    for book in books:
        for i in book:
            print(i,end=" ")
        print()
    conn.close()
#전체 데이타 출력 함수 호출
all_books()
#레코드 개수 정하여 출력
def some_books(number):
    conn=sqlite3.connect("my_books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books")
    books=cursor.fetchmany(number)

    for book in books:
        for i in book:
            print(i,end=" ")
        print()
    conn.close()

#
some_books(3)
#1개의 데이타 출력하는 함수
def one_book():
    conn=sqlite3.connect("my_books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books")
    book=cursor.fetchone()
    print(type(book))
    print(book)
    conn.close()

one_book()