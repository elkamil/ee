import re
from budynki.variables import ac_nr_aktu_notarialnego

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+).*')


def nr_dok(line):
    nospace = re.sub(r'\\s+', '', line)
    if AH.search(nospace):
        res9 = AH.search(nospace)
        ac_nr_aktu_notarialnego.append(res9.group(2))
    else:
        ac_nr_aktu_notarialnego.append('')
    return ac_nr_aktu_notarialnego
