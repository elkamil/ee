import re
from grunty.variables import z_nr_kw
AF = re.compile('.*KW\\s?:\\s?(.*?)(?=[uU]zbrojenie)', re.DOTALL)


def kw(line):
    if AF.search(line):
        res12 = AF.search(line)
        res12prim = res12.group(1)
        res12prim2 = re.sub(r',$', '', res12prim)
        if (len(re.findall('(,|;)', res12prim2)) == 0):
            z_nr_kw.append(re.sub(r'\s', '', re.sub(r'l', '/', res12prim2)))
            pozostale_ksiegi = ""
        elif (len(re.findall(',|;', res12prim2)) == 1):
            druga_ksiega_search = re.compile('(.*)(;|,)(.*)')
            druga_ksiega = druga_ksiega_search.search(res12prim2)
            d_ksiega = re.sub(r'\s', '', druga_ksiega.group(3))
            d_ksiega_pierwsza1 = re.sub(r'\s', '',  re.sub(r'l', '/', druga_ksiega.group(1)))
            z_nr_kw.append(d_ksiega_pierwsza1)
            pozostale_ksiegi = d_ksiega
        elif (len(re.findall(',|;', res12prim2)) > 1):
            d_ksiega_trzecia_search = re.compile('(.*?)(?=(,|;))[,;](.*)', re.DOTALL)
            d_ksiega_trz = d_ksiega_trzecia_search.search(res12prim2)
            d_ksiega_trzecia = re.sub(r'l', '/', d_ksiega_trz.group(3))
            d_ksiega_pierwsza = re.sub(r'\s', '', re.sub(r'l', '/', d_ksiega_trz.group(1)))
            z_nr_kw.append(re.sub(r'\s', '', d_ksiega_pierwsza))
            pozostale_ksiegi = '{0}' .format(d_ksiega_trzecia)
        else:
            z_nr_kw.append('')
            d_ksiega_pierwsza = ""

    else:
        z_nr_kw.append('')
        pozostale_ksiegi = ""
    return z_nr_kw, pozostale_ksiegi
