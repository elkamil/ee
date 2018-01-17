from grunty.variables import r_stan_prawny
import re

X = re.compile('Sprzedał\\s?:\\s?(.*?)(?=Kupi).*',re.DOTALL)


def stan_prawny_gruntu(line):
    if X.search(line):
        res1 = X.search(line)
        r_stan_prawny.append(res1.group(1))
    else:
        r_stan_prawny.append('')
    return r_stan_prawny
