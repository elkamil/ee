import re
from grunty.variables import be_funkcja

# B = re.compile('.*określono\s?[wW]\s?dniu\s?(.*)')
B = re.compile('.*Funkcja\\s?:\\s?(.*?)(?=Pow).*', re.DOTALL)


def funkcja(line):
    if B.search(line):
        res2 = B.search(line)
        be_funkcja.append(res2.group(1))
    else:
        be_funkcja.append('')
    return be_funkcja
