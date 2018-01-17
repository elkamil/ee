import re
from lokale_uslugowe.variables import ad_nr_aktu

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+).*')


def nr_dok(line):
    nospace = re.sub(r'\s+', '', line)
    if AH.search(nospace):
        res9 = AH.search(nospace)
        ad_nr_aktu.append(res9.group(2))
    else:
        ad_nr_aktu.append('')
    return ad_nr_aktu
