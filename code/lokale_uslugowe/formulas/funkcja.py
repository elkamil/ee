import re
from lokale_uslugowe.variables import x_funkcja

# B = re.compile('.*określono\s?[wW]\s?dniu\s?(.*)')
B = re.compile('.*Funkcja\\s?:\\s?(.*?)(?=Pow).*', re.DOTALL)


def funkcja(line):
    if B.search(line):
        res2 = B.search(line)
        x_funkcja.append(res2.group(1))
    else:
        x_funkcja.append('')
    return x_funkcja
