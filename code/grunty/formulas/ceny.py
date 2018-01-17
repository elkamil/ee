import re
from grunty.variables import n_cena_laczna, x_cena_brutto

N = re.compile('.*Cena\\s?łączna\\snieruchomości\\s?:\\s?\\b([^zł]+)(?=\\s?z?ł?\\s?okre).*')
Y = re.compile('Typ\\s?właś.*\\s?:\\s?(osoba fizyczna|\\s?osoba\\s?fizyczna|\\s?osoba\\s?prawna|gmina|\\s?gmina\\s?|\
               \\s?Skarb\\s?Państwa\\s?)', re.IGNORECASE)
Z_uwagi_do_ceny = re.compile('.*Uwagi\\s?do\\s?ceny\\s?:\\s?(.*?)(?=\\s?Nr\\s?dok).*', re.S)
G = re.compile('.*Cena\\s?:\\s?\\b([^zł]+)(?=\\s?z?ł?\\s?cena\\s?1).*', re.IGNORECASE)


def ceny(line):
    brutto = re.compile('(brr?utt?o|vat|brut)', re.IGNORECASE)
    netto = re.compile('(netto|nett?o|net)', re.IGNORECASE)
    res = Y.search(line)

    if Y.search(line):
        res_y1 = res.group(1)
    else:
        res_y1 = ''

    if Z_uwagi_do_ceny.search(line):
        res11 = Z_uwagi_do_ceny.search(line)
        uwagi_do_ceny = res11.group(1)
    else:
        uwagi_do_ceny = ''

    # print(N.search(line))
    if N.search(line):
        res6 = N.search(line)
        res6prim = res6.group(1)
        res6prim1 = re.sub(r'\s+', '', res6prim)
        if res_y1 in ['osoba fizyczna', 'gmina']:
            n_cena_laczna.append(res6prim1)
            x_cena_brutto.append(res6prim1)
        elif res_y1 in ['osoba prawna']:
            if brutto.search(uwagi_do_ceny) is None:
                if netto.search(uwagi_do_ceny) is not None:
                    n_cena_laczna.append(round(float(res6prim1), 2))
                    brutto = float(res6prim1)*1.23
                    x_cena_brutto.append(round(brutto, 2))
                else:
                    x_cena_brutto.append(round(float(res6prim1), 2))
                    netto = float(res6prim1)/1.23
                    n_cena_laczna.append(round(netto, 2))
                    uwagi_do_ceny = "Brak informacji czy cena netto/brutto, ceny unettowiono " + uwagi_do_ceny
            else:
                x_cena_brutto.append(round(float(res6prim1), 2))
                netto = float(res6prim1)/1.23
                n_cena_laczna.append(round(netto, 2))
        else:
            x_cena_brutto.append('')
            n_cena_laczna.append('')

    else:
        if G.search(line):
            res6 = G.search(line)
            res6prim = res6.group(1)
            res6prim1 = re.sub(r'\s+', '', res6prim)
            if res_y1 in ['osoba fizyczna', 'gmina']:
                n_cena_laczna.append(res6prim1)
                x_cena_brutto.append(res6prim1)
            elif res_y1 in ['osoba prawna']:
                if brutto.search(uwagi_do_ceny) is None:
                    if netto.search(uwagi_do_ceny) is not None:
                        n_cena_laczna.append(round(float(res6prim1), 2))
                        brutto = float(res6prim1)*1.23
                        x_cena_brutto.append(round(brutto, 2))
                    else:
                        x_cena_brutto.append(round(float(res6prim1), 2))
                        netto = float(res6prim1)/1.23
                        n_cena_laczna.append(round(netto, 2))
                        uwagi_do_ceny = "Brak informacji czy cena netto/brutto, ceny unettowiono " + uwagi_do_ceny
                else:
                    x_cena_brutto.append(round(float(res6prim1), 2))
                    netto = float(res6prim1)/1.23
                    n_cena_laczna.append(round(netto, 2))
            else:
                x_cena_brutto.append('')
                n_cena_laczna.append('')
        else:
            x_cena_brutto.append('')
            n_cena_laczna.append('')
    # cena brutto
    # if ab_cena_brutto[0] !='' and m_powierzchnia_uzytkowa[0] !='':
        # brutto_za_m2=float(ab_cena_brutto[0])/float(m_powierzchnia_uzytkowa[0])
        # ac_cena_brutto_mp2.append(round(brutto_za_m2,2))
    # else:
        # ac_cena_brutto_mp2.append('')

    # cena netto
    # if n_cena_laczna[0] !='' and m_powierzchnia_uzytkowa[0] !='' :
        # netto_za_m2=float(n_cena_laczna[0])/float(m_powierzchnia_uzytkowa[0])
        # o_cena_mp2.append(round(netto_za_m2,2))
    # else:
        # o_cena_mp2.append('')
    # print(n_cena_laczna)
    if n_cena_laczna[0]:
        n_cena_laczna_2f = ['%.2f' % elem for elem in [float(i) for i in n_cena_laczna]]
    else:
        n_cena_laczna_2f = ['']
    if x_cena_brutto[0]:
        x_cena_brutto_2f = ['%.2f' % elem for elem in [float(i) for i in x_cena_brutto]]
    else:
        x_cena_brutto_2f = ['']
    return n_cena_laczna_2f, x_cena_brutto_2f, uwagi_do_ceny
