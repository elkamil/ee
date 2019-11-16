import re
from mp.variables import cc_udzial

BX = re.compile('.*Udzia[lł]\\s?:\\s?(.*?)(?=Typ).*', re.DOTALL)


def udzial(line):
    if BX.search(line):
        res5 = BX.search(line)
        cc_udzial.append(res5.group(1))
    else:
        cc_udzial.append('')
    return cc_udzial
