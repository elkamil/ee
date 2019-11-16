import re

UZ = re.compile('Uzbrojenie\\s?:\\s?(.*?)(?=Rodzaj).*')


def uzbrojenie(line):
    opis_uzbrojenie = ''
    if UZ.search(line):
        uzb = UZ.search(line)
        if uzb.group(1):
            opis_uzbrojenie = 'uzbrojenie: {0}' .format(uzb.group(1))
        else:
            opis_uzbrojenie = uzb.group(1)
    else:
        opis_uzbrojenie = ''
    return opis_uzbrojenie
