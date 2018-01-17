import re
from mp.variables import n_pole_powierzchni

CB = re.compile('.*Pow\\.\\s?:\\s?(.*)\\sha.*')


def pole_powierzchni(line):
    if CB.search(line):
        res8 = CB.search(line)
        res8prim = res8.group(1)
        res8prim2 = re.sub(r'\.', '', res8prim)
        res8prim3 = re.sub(r'^[0]+', '', res8prim2)
        n_pole_powierzchni.append(res8prim3)
    else:
        n_pole_powierzchni.append('')
    return n_pole_powierzchni
