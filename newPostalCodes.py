import sqlite3
from sqlite3 import Error
import pandas as pd
from variables import pdf_folder


db_file = '/home/ee/code/kody1'


def newPostalCode(filename):
    print(filename)
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        df = pd.read_csv(pdf_folder+filename, sep='\t',)
        # import file to db
        df.to_sql('kody', conn, if_exists='replace', index=False)
        # change polish letters to normal and replace all spaces
        q_a = "update kody set ulica = replace(ulica,'ą','a')"
        q_e = "update kody set ulica = replace(ulica,'ę','e')"
        q_o = "update kody set ulica = replace(ulica,'ó','o')"
        q_s = "update kody set ulica = replace(ulica,'ś','s')"
        q_c = "update kody set ulica = replace(ulica,'ć','c')"
        q_l = "update kody set ulica = replace(ulica,'ł','l')"
        q_n = "update kody set ulica = replace(ulica,'ń','n')"
        q_z = "update kody set ulica = replace(ulica,'ź','z')"
        q_zz = "update kody set ulica = replace(ulica,'ż','z')"
        q_A = "update kody set ulica = replace(ulica,'Ą','a')"
        q_E = "update kody set ulica = replace(ulica,'Ę','e')"
        q_O = "update kody set ulica = replace(ulica,'Ó','o')"
        q_S = "update kody set ulica = replace(ulica,'Ś','s')"
        q_C = "update kody set ulica = replace(ulica,'Ć','c')"
        q_L = "update kody set ulica = replace(ulica,'Ł','l')"
        q_N = "update kody set ulica = replace(ulica,'Ń','n')"
        q_Z = "update kody set ulica = replace(ulica,'Ź','z')"
        q_ZZ = "update kody set ulica = replace(ulica,'Ż','z')"
        update_query = 'update kody set ulica=lower(ulica)'
        update_spaces = "update kody set ulica=replace(ulica,' ','')"

        [cur.execute(i) for i in [q_a, q_e, q_o, q_s, q_c, q_l, q_n, q_z, q_zz, q_A, q_E, q_O, q_S, q_C, q_L, q_N, q_Z, q_ZZ, update_query, update_spaces]]

        conn.commit()

    except Error as e:
        print(e)
    finally:
        conn.close()
    return ("Finito")
