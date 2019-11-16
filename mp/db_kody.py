import sqlite3
from sqlite3 import Error

db_file='/home/ee/code/kody'


def create_connection(ulica, nr_domu):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        if nr_domu % 2 == 0:
            kod_query = "select kod from kody where ulica like '%{0}%' and parzyste_od <= {1} and parzyste_do >= {1} and miasto = 'wroclaw'".format(ulica, nr_domu)
        else:
            kod_query = "select kod from kody where ulica like '%{0}%' and nieparzyste_od <= {1} and nieparzyste_do >= {1} and miasto = 'wroclaw'".format(ulica, nr_domu)
        cur.execute(kod_query)

        rows = cur.fetchall()
        if len(rows) > 0:
            z = rows[0]
        else:
            z = ['']


    except Error as e:
        print(e)
    finally:
        conn.close()
    return z


