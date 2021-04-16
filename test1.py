import sqlite3 as sql

con = sql.connect('test.db')
def create_table():
    with con:
        cur = con.cursor()
        groups = cur.execute(f"SELECT * from groups").fetchall()
        # print(cur.description)
        # print(groups)
        for g in groups:
            # print(g[0])
            cur.execute(
                f"CREATE TABLE IF NOT EXISTS '{g[0]}' ('monday' STRING, 'tuesday' STRING, 'wednesday' STRING,"
                f" 'thursday' STRING, 'friday' STRING, 'saturday' STRING, 'sunday' STRING)")
        con.commit()
