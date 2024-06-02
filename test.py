import sqlite3

conn=sqlite3.connect('todos.db')
c=conn.cursor()

c.execute('select * from todos')
results=c.fetchall()

print(results)

