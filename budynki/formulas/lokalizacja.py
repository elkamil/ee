from variables import obreby_plik
from budynki.variables import h_obreb_geodezyjny, i_arkusz, l_nr_dzialki, g_dzielnica, e_gmina, f_miejscowosc
import re
import pandas as pd

H = re.compile('.*Obręb\\s?:\\s?\\d{2}(\\d{2})\\s?-\\s?([^,]+),\\s?Ark\\.:\\s?\\b(.*)(?=\\s?,\\s?Nr\\s?dz\\.)\\s?,\\s?Nr\\s?dz\\.:\\s?(.*?)(?=\\s?Liczba\\s?kondygn\\.)\\s?Liczba\\s?kondygn\\.\\s?:\\s?(\\d{1})\\s?(.*?)\\s?(?=(\\s?\\d+?Funkcja|\\s?Funkcja)).*', re.DOTALL)
# H = re.compile('.*Obręb\s?:\s?\d{2}(\d{2})\s?-\s?([^,]+),\s?Ark\.:\s?\\b(.*)(?=\s?,\s?Nr\s?dz\.)\s?,\s?Nr\s?dz\.:\s?(.*?)(?=\s?Liczba\s?kondygn\.)\s?Liczba\s?kondygn\.\s?:\s?(\d{1})\s?(.*?)\s?(?=(\s?\d+?Funkcja|\s?Funkcja)).*',re.DOTALL)
obreby_csv = pd.read_csv(obreby_plik, sep=';', encoding='utf-8')


def lokalizacja(line):
    if H.search(line):
        res3 = H.search(line)
        obr = res3.group(2)+" ("+res3.group(1)+")"
        h_obreb_geodezyjny.append(obr)
        nr_dzialki = res3.group(4)+res3.group(6)

        i_arkusz.append(res3.group(3))
        l_nr_dzialki.append(nr_dzialki)
        # t_liczba_izb.append(res3.group(5))
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
        l_nr_dzialki.append('')
        e_gmina.append('')
        f_miejscowosc.append('')
        g_dzielnica.append('')
        z_obreb = ''
        # t_liczba_izb.append('')
    return h_obreb_geodezyjny, i_arkusz, l_nr_dzialki, e_gmina, f_miejscowosc, g_dzielnica, z_obreb
