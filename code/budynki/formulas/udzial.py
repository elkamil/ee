
import re
from budynki.variables import bx_udzial

BX = re.compile('.*Udzia[lł]\\s?:\\s?(.*?)(?=Typ).*', re.DOTALL)


def udzial(line):
    if BX.search(line):
        res5 = BX.search(line)
        bx_udzial.append(res5.group(1))
    else:
        bx_udzial.append('')
    return bx_udzial
