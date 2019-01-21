import re
from variables import obreby_plik
import pandas as pd
from lokale_mieszkalne.variables import h_obreb_geodezyjny, i_arkusz, ca_nr_dzialki, t_liczba_izb, e_gmina,\
     f_miejscowosc, g_dzielnica
H = re.compile('.*Obręb\\s?:\\s?\\d{2}(\\d{2})\\s?-\\s?([^,]+),\\s?\\s?Ark\\.:\\s?\\b(.*)(?=\\s?,\\s?\\s?Nr\\s?dz\\.)\\s?,\\s?\\s?Nr\\s?dz\\.:\\s?(.*?)(?=\\s?Liczba\\s?izb)\\s?Liczba\\s?izb\\s?:\\s?(\\d{1})\\s?(.*?)\\s?(?=(\\s?\\d+?Funkcja|\\s?Funkcja)).*', re.DOTALL)


# e_gmina = ['']
# f_miejscowosc = ['']
# g_dzielnica = ['']
# h_obreb_geodezyjny = ['']
# i_arkusz = ['']
# h_obreb_geodezyjny = ['']
# ca_nr_dzialki = ['']
# t_liczba_izb = ['']
# obreby_plik = "/home/ee/code/data/obreby.csv"

obreby_csv = pd.read_csv(obreby_plik, sep=';', encoding='utf-8')
# line = "1. Wrocław, FERDYNANDA MAGELLANA 19 m.14 (przetargowy)\
# Sprzedał : (ww - współużytkowanie wieczyste) -\
# Kupił : - Udział: 673/100000\
# Typ właściciela : osoba fizyczna\
# GRUNT                            LOKAL\
# Gmina : 026401_1, M. Wrocław\
# Obręb : 0064 - Swojczyce,  Ark.: 25,  Nr dz.: Liczba izb: 3\
# 24/37,24/56,24/61,24/63,24/77,24/84\
# Funkcja : B                   Funkcja : M\
# Pow. :  1.3510 ha           Pow. użytk. :57.38 m kw.\
# Cena:                          Cena:\
#     Cena 1 m kw.:                 Cena 1 m kw.:\
#         Cena łączna nieruchomości:320 000 złokreślono w dniu 17.12.2016\
#         Uwagi do ceny:brutto\
#         Nr dok.: AN32036/2016-640/2017,  KW: WR1K/00320655/5,WR1K/00353924/2\
#         Uzbrojenie: w, e,            Rodzaj bud. : wielorodzinne\
#         Przeznaczenie terenu :\
#             Opis dodatkowy : IV piętro,3 pokoje,w tym jeden z aneksem kuchennym połączony z\
#             przedpokojem,łazienka,wyłączne prawo korzystania z miejsca postojowego nr 1 P\
#             "

def lokalizacja(line):
    if H.search(line):
        res3 = H.search(line)
        obr = res3.group(2) + " (" + res3.group(1) + ")"
        h_obreb_geodezyjny.append(obr)
        nr_dzialki = res3.group(4)+res3.group(6)

        i_arkusz.append(res3.group(3))
        ca_nr_dzialki.append(nr_dzialki)
        t_liczba_izb.append(res3.group(5))
        z_obreb = 'Obręb: 00' + res3.group(1) + ' - ' + res3.group(2) + ', Ark.: ' + res3.group(3) +\
                  ', Nr dz.: ' + res3.group(4) + res3.group(6)
        G = obreby_csv[obreby_csv['Numer'] == int(res3.group(1))].Dzielnica
        G_val = G.values
        F = "Wrocław-" + G_val
        E = "Wrocław-" + G_val + " (delegatura)"
        e_gmina.append(E)
        f_miejscowosc.append(F)
        g_dzielnica.append(G_val)
    else:
        h_obreb_geodezyjny.append('')
        i_arkusz.append('')
        ca_nr_dzialki.append('')
        t_liczba_izb.append('')
        e_gmina.append('')
        f_miejscowosc.append('')
        g_dzielnica.append('')
        z_obreb = ''
    return h_obreb_geodezyjny, i_arkusz, ca_nr_dzialki, t_liczba_izb, e_gmina, f_miejscowosc, g_dzielnica, z_obreb


