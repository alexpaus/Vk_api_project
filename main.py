import sqlite3 as sql

con = sql.connect('test.db')

group_id = input()
with con:
    cur = con.cursor()
    cur.execute(f"INSERT INTO GROUPS VALUES ('{group_id}')")
    con.commit()