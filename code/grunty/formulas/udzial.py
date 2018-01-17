
import re
from grunty.variables import bd_udzial

BD = re.compile('.*Udzia[lł]\\s?:\\s?(.*?)(?=Typ).*', re.DOTALL)


def udzial(line):
    if BD.search(line):
        res5 = BD.search(line)
        bd_udzial.append(res5.group(1))
    else:
        bd_udzial.append('')
    return bd_udzial
