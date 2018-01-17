import re
# from itertools import islice
import numpy as np
from grunty.variables import kolumny
from grunty.formulas.b_data import b_data
from grunty.formulas.grunt import lokalizacja
from grunty.formulas.ulica import ulica
from grunty.formulas.rodzaj_osoby import rodzaj_osoby
from grunty.formulas.powierzchnia_gruntu import powierzchnia_gruntu
from grunty.formulas.stan_prawny import stan_prawny_gruntu
from grunty.formulas.udzial import udzial
from grunty.formulas.funkcja import funkcja
from grunty.formulas.ceny import ceny
from grunty.formulas.nr_dok import nr_dok
from grunty.formulas.kw import kw
from grunty.formulas.opis import opis
from grunty.formulas.uzbrojenie import uzbrojenie


def if_statements(line):
    for i in kolumny:
        del i[:]

# Funkcje
    dane_adresowe = lokalizacja(line)
    dane_ulica = ulica(line)
    sprzedajacy = rodzaj_osoby(line)
    pow_gruntu = powierzchnia_gruntu(line)
    cennik = ceny(line)
    nr_kw = kw(line)

    a_id = ['']
    b_data_transakcji = b_data(line)
    c_wojewodztwo = ['dolnośląskie']
    d_powiat = ['Wrocław']
    e_gmina = dane_adresowe[2]
    f_miejscowosc = dane_adresowe[3]
    g_dzielnica = dane_adresowe[4]
    h_obreb_geodezyjny = dane_adresowe[0]
    i_arkusz = dane_adresowe[1]
    j_ulica = dane_ulica[0]
    k_nr_budynku = dane_ulica[1]
    l_nr_dzialki = dane_adresowe[5]
    m_powierzchnia_gruntu = pow_gruntu[0]
    n_cena_laczna = cennik[0]
    o_cena_mp2 = ['']
    p_przeznaczenie_typ_dokumentu = ['']
    q_przeznaczenie_terentu = ['']
    r_stan_prawny = stan_prawny_gruntu(line)
    # s_opis = ['']
    t_pum_potencjalny_m2 = ['']
    u_gla_potencjalny = ['']
    v_cena_pum = ['']
    w_cena_gla = ['']
    x_cena_brutto = cennik[1]
    y_cena_brutto_m2 = ['']
    z_nr_kw = nr_kw[0]
    aa_sad = ['Sąd Rejonowy dla Wrocławia - Krzyków']
    ab_nr_aktu = nr_dok(line)
    ac_zrodlo_informacji = sprzedajacy[1]
    ad_zrodlo_danych = ['RCiWN']
    ae_sprzedajacy = sprzedajacy[0]
    af_kupujacy = ['']
    ag_ksztalt = ['']
    ah_dlugosc_frontu_dzialki = ['']
    ai_glebokosc_dzialki = ['']
    aj_uzbrojenie = ['']
    ak_kod_pocztowy = dane_ulica[2]
    al_osiedle = ['']
    am_strefa_miasta = ['']
    an_otoczenie = ['']
    ao_dosteponosc_kom = ['']
    ap_zrodlo_ceny = ['Transakcja']
    aq_cena_waluta = ['']
    ar_waluta = ['PLN']
    as_kurs_waluty = ['']
    at_prawo_do_wieczystego = ['']
    au_dzial_iii_kw = ['']
    av_wartosc_rynkowa = ['']
    aw_wartosc_odtworzeniowa = ['']
    ax_stawka_VAT = ['']
    ay_data_utworzenia = ['']
    az_data_modyfikacji = ['']
    ba_wpisana_przez = ['']
    bb_modyfikowana_przez = ['']
    bc_pozostale_obiekty = ['']
    bd_udzial = udzial(line)
    be_funkcja = funkcja(line)
    s_opis = re.sub(r'^$', '', re.sub(r'^;', '', re.sub(r';{2,}', '',
             re.sub(r'\n', '', '{0};{1};{2};księgi podane w RCiWN: {3};{4}' .format(cennik[2],
             opis(line), dane_adresowe[6], nr_kw[1], uzbrojenie(line))))))

    z = np.column_stack((a_id, b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc, g_dzielnica,
                         h_obreb_geodezyjny, i_arkusz, j_ulica, k_nr_budynku, l_nr_dzialki, m_powierzchnia_gruntu,
                         n_cena_laczna, o_cena_mp2, p_przeznaczenie_typ_dokumentu, q_przeznaczenie_terentu,
                         r_stan_prawny, s_opis, t_pum_potencjalny_m2, u_gla_potencjalny, v_cena_pum,
                         w_cena_gla, x_cena_brutto, y_cena_brutto_m2, z_nr_kw, aa_sad, ab_nr_aktu,
                         ac_zrodlo_informacji, ad_zrodlo_danych, ae_sprzedajacy, af_kupujacy, ag_ksztalt,
                         ah_dlugosc_frontu_dzialki, ai_glebokosc_dzialki, aj_uzbrojenie, ak_kod_pocztowy,
                         al_osiedle, am_strefa_miasta, an_otoczenie, ao_dosteponosc_kom, ap_zrodlo_ceny,
                         aq_cena_waluta, ar_waluta, as_kurs_waluty, at_prawo_do_wieczystego, au_dzial_iii_kw,
                         av_wartosc_rynkowa, aw_wartosc_odtworzeniowa, ax_stawka_VAT, ay_data_utworzenia,
                         az_data_modyfikacji, ba_wpisana_przez, bb_modyfikowana_przez, bc_pozostale_obiekty,
                         bd_udzial, be_funkcja))

    return z
