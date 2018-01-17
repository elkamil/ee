import re
Z_uwagi_do_ceny = re.compile('.*Uwagi\\s?do\\s?ceny\\s?:\\s?(.*?)(?=\\s?Nr\\s?dok).*', re.S)


def uwagi_do_ceny(line):
    if Z_uwagi_do_ceny.search(line):
        res11 = Z_uwagi_do_ceny.search(line)
        uwagi_do_ceny = res11.group(1)
    else:
        uwagi_do_ceny = ''
    return uwagi_do_ceny
