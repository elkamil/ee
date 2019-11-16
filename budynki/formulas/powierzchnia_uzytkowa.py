import re
from budynki.variables import n_powierzchnia_uzytkowa

M = re.compile('.*Pow\\.\\s?użytk\\.\\s?:\\s?\\b(.*)(?=\\s?m\\s?kw\\.).*')


def powierzchnia_uzytkowa(line):
    if M.search(line):
        res5 = M.search(line)
        n_powierzchnia_uzytkowa.append(round(float(res5.group(1)), 2))
        o_podstawa_ustalenia = 'RCiWN'
    else:
        n_powierzchnia_uzytkowa.append('')
        o_podstawa_ustalenia = 'Pomiary własne z map i pow. zabudowy'
    return n_powierzchnia_uzytkowa, o_podstawa_ustalenia
