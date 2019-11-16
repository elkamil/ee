from mp.variables import w_stan_prawny_gruntu
import re

X = re.compile('Sprzedał\\s?:\\s?(.*)\\s+-.*')


def stan_prawny_gruntu(line):
    if X.search(line):
        res1 = X.search(line)
        w_stan_prawny_gruntu.append(res1.group(1))
    else:
        w_stan_prawny_gruntu.append('')
    return w_stan_prawny_gruntu
