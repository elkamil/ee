import re
from mp.variables import o_powierzchnia_uzytkowa

M = re.compile('.*Pow\\.\\s?użytk\\.\\s?:\\s?\\b(.*)(?=\\s?m\\s?kw\\.).*')


def powierzchnia_uzytkowa(line):
    if M.search(line):
        res5 = M.search(line)
        o_powierzchnia_uzytkowa.append(round(float(res5.group(1)), 2))
    else:
        o_powierzchnia_uzytkowa.append('1')
    return o_powierzchnia_uzytkowa
