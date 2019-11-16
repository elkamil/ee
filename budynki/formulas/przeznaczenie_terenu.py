import re
from budynki.variables import bz_przeznaczenie_terenu

BZ = re.compile('Przez.*terenu\\s?:\\s?(.*?)(?=Opis)', re.DOTALL)


def przeznaczenie_terenu(line):
    if BZ.search(line):
        bz = BZ.search(line)
        bz_przeznaczenie_terenu.append(bz.group(1))
    else:
        bz_przeznaczenie_terenu.append('')
    return bz_przeznaczenie_terenu
