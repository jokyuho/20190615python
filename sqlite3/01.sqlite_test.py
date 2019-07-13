import sqlite3

print(sqlite3.version)

conn=sqlite3.connect('sqlite3/example.db') # 자동으로 만들어짐.
c=conn.cursor()

# Create table
c.execute('''
            CREATE TABLE if not exists stocks(
                data text,
                trans text,
                symbol text,
                qty real,
                price real
            )
        ''')

c.execute('''

            insert into stocks(data, trans, symbol, qty, price)
                        values('2006-01-05','BUY','RHAT',100,35.14)
        ''')

# Save (commit) the changes
conn.commit()

conn.close()