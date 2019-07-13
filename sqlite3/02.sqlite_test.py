import sqlite3

conn=sqlite3.connect('sqlite3/example.db')
c=conn.cursor()
symbol='RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
items = c.fetchall()

for item in items:
    print(item) # 튜플로 저장되어서 출력됨

t=('RHAT',)
sql='select * from stocks where symbol=?'
c.execute(sql,t)
print(c.fetchall())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00), ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),('2006-04-06', 'SELL', 'IBM', 500, 53.00),]

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
conn.commit()
c.execute('select * from stocks ORDER BY price')
rows=c.fetchall()
for row in rows:
    print(row)
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

c.close()