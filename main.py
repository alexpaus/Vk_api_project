import sqlite3 as sql

con = sql.connect('test.db')


def add_id(id):
    group_id = id
    with con:
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM GROUPS""").fetchall()
        c = 0
        for i in result:
            if i[0] == id:
                c += 1
        if c == 0:
            cur.execute(f" INSERT INTO GROUPS VALUES  ('{group_id}')")
            con.commit()


def show(id, day):
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = week[int(day)]
    cur = con.cursor()
    s = ''
    try:
        result = cur.execute("""SELECT {} FROM '{}'  '' """.format(day, id)).fetchall()
        res = result[0][0].split()
        res = [i.capitalize() for i in res]
        for i in res:
            s += str(res.index(i) + 1) + '. ' + i + '\n'
        return (s)
    except:
        return '❌Расписание не найдено❌'


def change(id, day, rasp):
    cur = con.cursor()
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = week[int(day)]
    rasp = ' '.join(rasp)
    print(day, id, rasp)
    cur.execute("""DELETE from '{}' where {} <> ''""".format(id, day))
    s = """INSERT INTO '{}'('{}') VALUES('{}')""".format(id, day, rasp)
    cur.execute(s)
    con.commit()
