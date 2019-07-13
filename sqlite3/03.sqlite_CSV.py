import csv, sqlite3

input_file = 'sqlite3/input.csv'

conn=sqlite3.connect('sqlite3/suppliers.db')
cursor=conn.cursor()

# csv 파일에서 데이터를 읽어서 테이블에 insert
file_reader=csv.reader(open(input_file, 'r'),delimiter=',')
# 첫 라인을 읽음(제목행)
header=next(file_reader,None) # next를 쓰면 가져와서 header에 집어넣고 없어짐.
print('header',header)

# header 이후의 2번째 행부터 끝까지 읽어 들이며 insert 즉 csv파일을 가져와서 db화 한다.
for row in file_reader:
    data=[]
# idx에는 0~4가 입력됨
    for idx in range(len(header)):
        data.append(row[idx])
    cursor.execute('insert into suppliers values(?,?,?,?,?)',data)

conn.commit()