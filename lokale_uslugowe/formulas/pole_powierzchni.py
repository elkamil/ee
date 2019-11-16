import re
from lokale_uslugowe.variables import bv_pole_powierzchni_gruntu

CB = re.compile('.*Pow\\.\\s?:\\s?(.*)\\sha.*')


def pole_powierzchni(line):
    if CB.search(line):
        res8 = CB.search(line)
        res8prim = res8.group(1)
        res8prim2 = re.sub(r'\.', '', res8prim)
        res8prim3 = re.sub(r'^[0]+', '', res8prim2)
        bv_pole_powierzchni_gruntu.append(res8prim3)
    else:
        bv_pole_powierzchni_gruntu.append('')
    return bv_pole_powierzchni_gruntu
