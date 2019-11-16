import re
from lokale_uslugowe.variables import v_stan_prawny_gruntu

X = re.compile('Sprzedał\\s?:\\s?(.*)\\s+-.*')


def stan_prawny(line):
    if X.search(line):
        res1 = X.search(line)
        v_stan_prawny_gruntu.append(res1.group(1))
    else:
        v_stan_prawny_gruntu.append('')
    return v_stan_prawny_gruntu
