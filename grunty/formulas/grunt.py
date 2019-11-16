from variables import obreby_plik
import re
import pandas as pd
from grunty.variables import h_obreb_geodezyjny, i_arkusz, e_gmina, l_nr_dzialki,\
                             f_miejscowosc, g_dzielnica


obreby_csv = pd.read_csv(obreby_plik, sep=';', encoding='utf-8')
H = re.compile('.*Obręb\\s?:\\s?\\d{2}(\\d{2})\\s?-\\s?([^,]+),\\s?Ark\\.:\\s?\\b(.*)(?=\\s?,\\s?Nr\\s?dz\\.)\\s?,\\s?Nr\\s?dz\\.:\\s?(.*?)(?=\\s?(Funkcja|\\s?Funkcja)).*', re.DOTALL)
H_lokal = re.compile('.*Obręb\\s?:\\s?\\d{2}(\\d{2})\\s?-\\s?([^,]+),\\s?Ark\\.:\\s?\\b(.*)(?=\\s?,\\s?Nr\\s?dz\\.)\\s?,\\s?Nr\\s?dz\\.:\\s?(.*?)(?=\\s?Liczba\\s?izb)\\s?Liczba\\s?izb\\s?:\\s?(\\d{1})\\s?(.*?)\\s?(?=(\\s?\\d+?Funkcja|\\s?Funkcja)).*', re.DOTALL)
H_budynek = re.compile('.*Obręb\\s?:\\s?\\d{2}(\\d{2})\\s?-\\s?([^,]+),\\s?Ark\\.:\\s?\\b(.*)(?=\\s?,\\s?Nr\\s?dz\\.)\\s?,\\s?Nr\\s?dz\\.:\\s?(.*?)(?=\\s?Liczba\\s?kondygn\\.)\\s?Liczba\\s?kondygn\\.\\s?:\\s?(\\d{1})\\s?(.*?)\\s?(?=(\\s?\\d+?Funkcja|\\s?Funkcja)).*', re.DOTALL)
budynek = re.compile('BUDYNEK')
lokal = re.compile('LOKAL')


def lokalizacja(line):
    if budynek.search(line) is not None:
        if H_budynek.search(line):
            res3 = H_budynek.search(line)
            obr = res3.group(2)+" ("+res3.group(1)+")"
            h_obreb_geodezyjny.append(obr)
            nr_dzialki = res3.group(4)+res3.group(6)
            i_arkusz.append(res3.group(3))
            # t_liczba_izb.append(res3.group(5))
            z_obreb = 'Obręb: 00' + res3.group(1) + ' - ' + res3.group(2) + ', Ark.: ' + res3.group(3) + ', Nr dz.: '\
                      + res3.group(4) + res3.group(6)
            G = obreby_csv[obreby_csv['Numer'] == int(res3.group(1))].Dzielnica
            G_val = G.values
            F = "Wrocław-" + G_val
            E = "Wrocław-" + G_val + " (delegatura)"
            e_gmina.append(E)
            f_miejscowosc.append(F)
            g_dzielnica.append(G_val)
            l_nr_dzialki = res3.group(4) + res3.group(6)
            # l_nr_dzialki = nr_dzialki
        else:
            h_obreb_geodezyjny.append('')
            i_arkusz.append('')
            e_gmina.append('')
            f_miejscowosc.append('')
            g_dzielnica.append('')
            l_nr_dzialki = ''
            z_obreb = ''

    elif lokal.search(line) is not None:
        if H_lokal.search(line):
            res3 = H_lokal.search(line)
            obr = res3.group(2) + " (" + res3.group(1) + ")"
            h_obreb_geodezyjny.append(obr)
            nr_dzialki = res3.group(4) + res3.group(6)
            i_arkusz.append(res3.group(3))
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
            l_nr_dzialki = nr_dzialki
        else:
            h_obreb_geodezyjny.append('')
            i_arkusz.append('')
            e_gmina.append('')
            f_miejscowosc.append('')
            g_dzielnica.append('')
            l_nr_dzialki = ''
            z_obreb = ''

    else:
        if H.search(line):
            res3 = H.search(line)
            obr = res3.group(2)+" ("+res3.group(1)+")"
            h_obreb_geodezyjny.append(obr)
            l_nr_dzialki = res3.group(4)
            i_arkusz.append(res3.group(3))
            z_obreb = 'Obręb: 00'+res3.group(1) + ' - ' + res3.group(2)+', Ark.: ' + res3.group(3) + ', Nr dz.: '\
                      + res3.group(4)
            G = obreby_csv[obreby_csv['Numer'] == int(res3.group(1))].Dzielnica
            G_val = G.values
            F = "Wrocław-"+G_val
            E = "Wrocław-"+G_val+" (delegatura)"
            e_gmina.append(E)
            g_dzielnica.append(G_val)
            f_miejscowosc.append(F)
        else:
            h_obreb_geodezyjny.append('')
            i_arkusz.append('')
            e_gmina.append('')
            f_miejscowosc.append('')
            g_dzielnica.append('')
            l_nr_dzialki = ''
            z_obreb = ''
    return h_obreb_geodezyjny, i_arkusz, e_gmina, f_miejscowosc, g_dzielnica, l_nr_dzialki, z_obreb
