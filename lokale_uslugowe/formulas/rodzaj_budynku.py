import re
from lokale_uslugowe.variables import t_rodzaj_budynku

V = re.compile('Rodzaj\\s?bud\\.\\s?:\\s?(jednorodzinne|wielorodzinne|wieIorodzinne)')


def rodzaj_budynku(line):
    if V.search(line):
        res7 = V.search(line)
        t_rodzaj_budynku.append(res7.group(1))
    else:
        t_rodzaj_budynku.append('')
    return t_rodzaj_budynku
