import re
import numpy as np
from mp.variables import *
from geo import geo
from is_online import is_online

from mp.formulas.b_data_transakcji import b_data
from mp.formulas.lokalizacja import lokalizacja
from mp.formulas.ulica import ulica
from mp.formulas.ceny import ceny
from mp.formulas.stan_prawny import stan_prawny_gruntu
# from mp.formulas.rodzaj_budynku import rodzaj_budynku
from mp.formulas.pole_powierzchni import pole_powierzchni
from mp.formulas.powierzchnia_uzytkowa import powierzchnia_uzytkowa
from mp.formulas.nr_dok import nr_dok
from mp.formulas.kw import kw
# from mp.formulas.udzial import udzial
from mp.formulas.opis import opis as opis_f
from mp.formulas.rodzaj_osoby import rodzaj_osoby

# file = "/home/ee/ee_convert/data/obreby.csv"

# obreby_csv = pd.read_csv(file, sep=';', encoding='utf-8')


def if_statements(line):
    for i in kolumny:
        del i[:]

    dane_adresowe = lokalizacja(line)
    dane_ulica = ulica(line)
    r_osoby = rodzaj_osoby(line)

    cena = ceny(line)
    kw_all = kw(line)
    # opis_all = '{0};{1};{2};księga gruntowa: {3}' .format(cena[2], opis_f(line), dane_adresowe[7], kw_all[1])

    a_id = ['']
    b_data_transakcji = b_data(line)
    c_wojewodztwo = ['dolnośląskie']
    d_powiat = ['Wrocław']
    e_gmina = dane_adresowe[3]
    f_miejscowosc = dane_adresowe[4]
    g_dzielnica = dane_adresowe[5]
    h_obreb_geodezyjny = dane_adresowe[0]
    i_arkusz = dane_adresowe[1]
    j_ulica = dane_ulica[0]
    k_nr_budynku = dane_ulica[1]
    l_nr_dzialki = dane_adresowe[2]
    m_oznaczenie = dane_ulica[2]
    n_pole_powierzchni = pole_powierzchni(line)
    o_powierzchnia_uzytkowa = powierzchnia_uzytkowa(line)
    p_cena = cena[0]
    q_cena_mp2pu = ['']
    # r_opis = ['']
    s_konstrukcja_budynku = ['']
    t_rok_budowy = ['']
    u_cena_brutto = cena[1]
    v_cena_brutto_mp2 = ['']
    w_stan_prawny_gruntu = stan_prawny_gruntu(line)
    x_nr_kw = kw_all[0]
    y_sad = ['Sąd Rejonowy dla Wrocławia - Krzyków']
    z_nr_aktu = nr_dok(line)
    aa_zrodlo_informacji = r_osoby[1]
    ab_zrodlo_danych = ['RCiWN']
    ac_sprzedajacy = r_osoby[0]
    ad_kupujacy = ['']
    ae_typ_garazu = ['']
    af_powierzchnia_zabudowy = ['']
    ag_kubatura = ['']
    ah_liczba_kondygnacji = ['']
    ai_pozostale_obiekty = ['']
    aj_kod_pocztowy = dane_ulica[3]
    ak_osiedle = ['']
    al_strefa_miasta = ['']
    am_otoczenie = ['']
    an_dostepnosc = ['']
    ao_zrodlo_ceny = ['Transakcja']
    ap_cena_waluta = ['PLN']
    aq_waluta = ['PLN']
    ar_kurs_waluty = ['']
    as_stan_prawny = ['Prawo własności']
    at_dzial_kw = ['']
    au_wartosc_rynkowa = ['']
    av_wartosc_odtworzeniowa = ['']
    aw_stawka_VAT = ['']
    ax_data_utworzenia = ['']
    ay_data_modyfikacji = ['']
    az_wpisana_przez = ['']
    ba_modyfikowana_przez = ['']
    bb_winda = ['']
    xxx_ulica_geo = ['']
    #if is_online():
        #xxx_ulica_geo = geo(dane_ulica[4], dane_ulica[5])
    #    xxx_ulica_geo = ['']
    #else:
    #    xxx_ulica_geo = ['']
    if cena[2]:
        cena_opis = cena[2]
    else:
        cena_opis = ''

    if opis_f(line):
        opis_opis = opis_f(line)
    else:
        opis_opis = ''

    if dane_adresowe[6]:
        adres_opis = dane_adresowe[6]
    else:
        adres_opis = ''

    if kw_all[1]:
        kw_opis = 'księgi podane w RCiWn: {0}'.format(kw_all[1])
    else:
        kw_opis = ''

    tt = ''
    for i in [cena_opis, opis_opis, adres_opis, kw_opis]:
        if i:
            tt += str(i) + ';'
    tt = re.sub(r';$', '', re.sub(r'\n', '', tt))
    # s_opis = re.sub(r'^$', '', re.sub(r'^;', '', re.sub(r';{2,}', '',
    # re.sub(r'\n', '', '{0};{1};{2};księgi podane w RCiWN: {3};{4}' .format(cennik[2],
    # opis(line), dane_adresowe[6], nr_kw[1], uzbrojenie(line))))))
    # t_opis = tt
    # opis_all = re.sub(r'^$', '', re.sub(r'^;', '', re.sub(r';{2,}', '', re.sub(r'\n', '', '{0};{1};{2};księga gruntowa: {3}' .format(cena[2], opis_f(line), dane_adresowe[7], kw_all[1])))))
    r_opis = tt
    z = np.column_stack((a_id, b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc, g_dzielnica,
                         h_obreb_geodezyjny, i_arkusz, j_ulica, k_nr_budynku, l_nr_dzialki, m_oznaczenie,
                         n_pole_powierzchni, o_powierzchnia_uzytkowa, p_cena, q_cena_mp2pu, r_opis,
                         s_konstrukcja_budynku, t_rok_budowy, u_cena_brutto, v_cena_brutto_mp2,
                         w_stan_prawny_gruntu, x_nr_kw, y_sad, z_nr_aktu, aa_zrodlo_informacji, ab_zrodlo_danych,
                         ac_sprzedajacy, ad_kupujacy, ae_typ_garazu, af_powierzchnia_zabudowy, ag_kubatura,
                         ah_liczba_kondygnacji, ai_pozostale_obiekty, aj_kod_pocztowy, ak_osiedle, al_strefa_miasta,
                         am_otoczenie, an_dostepnosc, ao_zrodlo_ceny, ap_cena_waluta, aq_waluta, ar_kurs_waluty,
                         as_stan_prawny, at_dzial_kw, au_wartosc_rynkowa, av_wartosc_odtworzeniowa, aw_stawka_VAT,
                         ax_data_utworzenia, ay_data_modyfikacji, az_wpisana_przez, ba_modyfikowana_przez, bb_winda,
                         xxx_ulica_geo))
    return z
