import re
# from geo import geo
from db_kody import create_connection as get_kod
from budynki.variables import j_ulica, k_nr_budynku


# ulica_re = re.compile('\sm\..*')
# ulica_else = re.compile('\d+\s?\.\s?([^,]+)\s?,\s?([^\d]+)\s?((?!m\.).*)\s?\(.*')
# al_plac = re.compile('^\s?(AL\.|al\.|ALEJA|PL\.|pl\.|PLAC)')
# J = re.compile('\d+\s?\.\s?([^,]+)\s?,\s?([^\d]+)\s?((?!m\.).*)\s?m\.\s?([^(\s]+)\s?.*')

ulica_re = re.compile('\\sm\\..*')
ulica_else = re.compile('\\d+\\s?\\.\\s?([^,]+)\\s?,\\s?([^\\d]+)\\s?((?!m\\.).*)\\s?\\(.*')
al_plac = re.compile('^\\s?(AL\\.|al\\.|ALEJA|PL\\.|pl\\.|PLAC)')
J = re.compile('\\d+\\s?\\.\\s?([^,]+)\\s?,\\s?([^\\d]+)\\s?((?!m\\.).*)\\s?m\\.\\s?([^(\\s]+)\\s?.*')


def ulica(line):
    line = re.sub(r'\sG[Aa]\s',' 6a ', re.sub(r'\sG[gG]\s',' 6g ', re.sub(r'\sG[dD]\s',' 6d ', re.sub(r'G[bB]', '6b', re.sub(r'%', '9b', line.splitlines()[0])))))
    if ulica_re.search(line) is not None:
        res4 = J.search(line)
        if res4 is not None:
            if al_plac.search(res4.group(2)) is not None:
                j_ulica.append(res4.group(2))
                k_nr_budynku.append(res4.group(3))
            elif al_plac.search(res4.group(2)) is None:
                ulica_plac_al = "ul. "+res4.group(2)
                j_ulica.append(ulica_plac_al)
                k_nr_budynku.append(res4.group(3))
            else:
                j_ulica.append(res4.group(2))
                k_nr_budynku.append(res4.group(3))

        else:
            j_ulica.append('')
            k_nr_budynku.append('')

    elif ulica_re.search(line) is None:
        res4 = ulica_else.search(line)
        if al_plac.search(res4.group(2)) is not None:
            ulic = res4.group(2)
            ulica_remove_wolny_rynek = re.sub(r'(\s+|\s?)\((wolny|przetargowy).*\n.*', '', ulic)
            j_ulica.append(ulica_remove_wolny_rynek)
            k_nr_budynku.append(res4.group(3))
        else:
            ulic = res4.group(2)
            ulica_remove_wolny_rynek = re.sub(r'(\s?|\s+)\((przetargowy|wolny).*\n.*', '', ulic)
            if len(ulica_remove_wolny_rynek) <= 1:
                j_ulica.append('')
                k_nr_budynku.append('')
            else:

                j_ulica.append("ul. "+ulica_remove_wolny_rynek)
                k_nr_budynku.append(res4.group(3))
    else:

        j_ulica.append('')
        k_nr_budynku.append('')
    try:
        # find_char_in_nr_domu = re.compile('[,-/|]')
        find_char_in_nr_domu = re.compile('(.*?)(?=(,|-|/))')
        if find_char_in_nr_domu.search(k_nr_budynku[0]):
            K = find_char_in_nr_domu.search(k_nr_budynku[0])
            nr_domu_code = int(re.sub(r'[aA-zZ]','',re.sub(r'\s+','',K.group(1))))
        else:
            nr_domu_code = int(re.sub(r'[aA-zZ]','',re.sub(r'\s+','',k_nr_budynku[0])))
    except:
        pass
        nr_domu_code = ''
   #  xxx_ulica_geo = geo(j_ulica[0], nr_domu_code)
    if j_ulica[0] and nr_domu_code:
        ulica_code = re.sub(r'^ul.\s?','',re.sub(r'\s+','',re.sub(r'[Źź]','z',re.sub(r'[Żż]','z',re.sub(r'[Śś]','s',re.sub(r'[óÓ]','o',re.sub(r'[Ńń]','',re.sub(r'[Łł]','l',re.sub(r'[Ćć]','c', re.sub(r'[Ęę]','e',re.sub(r'[ąĄ]','a',j_ulica[0]))))))))))).lower()
        kod = get_kod(ulica_code, nr_domu_code)
    else:
        kod = ['']
    return j_ulica, k_nr_budynku, kod, j_ulica[0], nr_domu_code
