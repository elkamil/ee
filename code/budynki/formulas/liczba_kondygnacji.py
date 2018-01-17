import re
from budynki.variables import ak_liczba_kondygnacji

AK = re.compile('.*Liczba\\s?kondygn\\.\\s?:\\s?(\\d+)')


def liczba_kondygnacji(line):
    if AK.search(line):
        res5 = AK.search(line)
        ak_liczba_kondygnacji.append(res5.group(1))
    else:
        ak_liczba_kondygnacji.append('')
    return ak_liczba_kondygnacji
