import re
from mp.variables import z_nr_aktu

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+).*')


def nr_dok(line):
    nospace = re.sub(r'\s+', '', line)
    if AH.search(nospace):
        res9 = AH.search(nospace)
        z_nr_aktu.append(res9.group(2))
    else:
        z_nr_aktu.append('')
    return z_nr_aktu
