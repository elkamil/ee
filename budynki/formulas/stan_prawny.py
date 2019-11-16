from budynki.variables import y_stan_prawny_gruntu
import re

X = re.compile('Sprzedał\\s?:\\s?(.*)\\s+-.*')


def stan_prawny_gruntu(line):
    if X.search(line):
        res1 = X.search(line)
        y_stan_prawny_gruntu.append(res1.group(1))
    else:
        y_stan_prawny_gruntu.append('')
    return y_stan_prawny_gruntu
