import re
from lokale_mieszkalne.variables import ah_nr_aktu

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+).*')


def nr_dok(line):
    nospace = re.sub(r'\s+', '', line)
    if AH.search(nospace):
        res9 = AH.search(nospace)
        ah_nr_aktu.append(res9.group(2))
    else:
        ah_nr_aktu.append('')
    return ah_nr_aktu
