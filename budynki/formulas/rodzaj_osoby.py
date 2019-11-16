import re
from budynki.variables import ae_sprzedajacy, s_zrodlo_informacji
Y = re.compile('Typ\\s?właś.*\\s?:\\s?(osoba fizyczna|\\s?osoba\\s?fizyczna|\\s?osoba\\s?prawna|gmina|\\s?gmina\\s?|\
               \\s?Skarb\\s?Państwa\\s?)', re.IGNORECASE)


def rodzaj_osoby(line):
    if Y.search(line):
        res = Y.search(line)
        res_y1 = res.group(1)
        ae_sprzedajacy.append(res.group(1))
        if res_y1 in ['osoba fizyczna']:
            res_y = "Umowa ostateczna sprzedaży rynek wtórny"
            s_zrodlo_informacji.append(res_y)
        elif res_y1 in ['osoba prawna']:
            res_y = "Umowa ostateczna sprzedaży rynek pierwotny"
            s_zrodlo_informacji.append(res_y)
        else:
            res_y = "Przetarg (w przypadku transakcji przetargowych)"
            s_zrodlo_informacji.append(res_y)
    else:
        s_zrodlo_informacji.append('')
        ae_sprzedajacy.append('')
    return ae_sprzedajacy, s_zrodlo_informacji
