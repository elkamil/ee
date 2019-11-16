import re
from mp.variables import ac_sprzedajacy, aa_zrodlo_informacji
Y = re.compile('Typ\\s?właś.*\\s?:\\s?(osoba fizyczna|\\s?osoba\\s?fizyczna|\\s?osoba\\s?prawna|gmina|\\s?gmina\\s?|\
               \\s?Skarb\\s?Państwa\\s?)', re.IGNORECASE)


def rodzaj_osoby(line):
    if Y.search(line):
        res = Y.search(line)
        res_y1 = res.group(1)
        ac_sprzedajacy.append(res.group(1))
        if res_y1 in ['osoba fizyczna']:
            res_y = "Umowa ostateczna sprzedaży rynek wtórny"
            aa_zrodlo_informacji.append(res_y)
        elif res_y1 in ['osoba prawna']:
            res_y = "Umowa ostateczna sprzedaży rynek pierwotny"
            aa_zrodlo_informacji.append(res_y)
        else:
            res_y = "Przetarg (w przypadku transakcji przetargowych)"
            aa_zrodlo_informacji.append(res_y)
    else:
        aa_zrodlo_informacji.append('')
        ac_sprzedajacy.append('')
    return ac_sprzedajacy, aa_zrodlo_informacji
