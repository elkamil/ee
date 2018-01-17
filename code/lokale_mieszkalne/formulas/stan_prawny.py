import re
from lokale_mieszkalne.variables import x_stan_prawny_gruntu

X = re.compile('Sprzedał\\s?:\\s?(.*)\\s+-.*')


def stan_prawny(line):
    if X.search(line):
        res1 = X.search(line)
        x_stan_prawny_gruntu.append(res1.group(1))
    else:
        x_stan_prawny_gruntu.append('')
    return x_stan_prawny_gruntu
