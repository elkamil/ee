import re
from grunty.variables import q_przeznaczenie_terentu

BZ = re.compile('Przez.*terenu\\s?:\\s?(.*?)(?=Opis)', re.DOTALL)


def przeznaczenie_terenu(line):
    if BZ.search(line):
        bz = BZ.search(line)
        q_przeznaczenie_terentu.append(bz.group(1))
    else:
        q_przeznaczenie_terentu.append('')
    return q_przeznaczenie_terentu
