import pymysql

conn = pymysql.connect(host = 'localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

c = conn.cursor()

# Do this instead
t = ('ibm')
sql='SELECT * FROM stocks WHERE symbol=%s'
c.execute(sql, t)
print(c.fetchall())
print()

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
        ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
        ('2006-04-06', 'SELL', 'IBM', 500, 53.00)
        ]

c.executemany('INSERT INTO stocks VALUES (%s,%s,%s,%s,%s)', purchases)
conn.commit()

c.execute('select * from stocks ORDER BY price')
rows=c.fetchall()
for row in rows:
    print(row)

c.close()