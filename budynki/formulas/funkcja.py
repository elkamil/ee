import re
from budynki.variables import by_funkcja

# B = re.compile('.*określono\s?[wW]\s?dniu\s?(.*)')
B = re.compile('.*Funkcja\\s?:\\s?(.*?)(?=Pow).*', re.DOTALL)


def funkcja(line):
    if B.search(line):
        res2 = B.search(line)
        by_funkcja.append(res2.group(1))
    else:
        by_funkcja.append('')
    return by_funkcja
