import re
from grunty.variables import ab_nr_aktu

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+).*')


def nr_dok(line):
    nospace = re.sub(r'\\s+', '', line)
    if AH.search(nospace):
        res9 = AH.search(nospace)
        ab_nr_aktu.append(res9.group(2))
    else:
        ab_nr_aktu.append('')
    return ab_nr_aktu
