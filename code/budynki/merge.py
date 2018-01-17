import re
import numpy as np
# from geo import geo
from budynki.variables import *
# from budynki.regexp import *
from budynki.formulas.b_data import b_data
from budynki.formulas.lokalizacja import lokalizacja
from budynki.formulas.ulica import ulica
from budynki.formulas.powierzchnia_gruntu import powierzchnia_gruntu
from budynki.formulas.powierzchnia_uzytkowa import powierzchnia_uzytkowa
from budynki.formulas.typ_budynku import typ_budynku
from budynki.formulas.stan_prawny import stan_prawny_gruntu
from budynki.formulas.liczba_kondygnacji import liczba_kondygnacji
from budynki.formulas.udzial import udzial
from budynki.formulas.rodzaj_osoby import rodzaj_osoby
from budynki.formulas.funkcja import funkcja
from budynki.formulas.ceny import ceny
from budynki.formulas.nr_dok import nr_dok
from budynki.formulas.kw import kw
from budynki.formulas.przeznaczenie_terenu import przeznaczenie_terenu
from budynki.formulas.opis import opis
from budynki.formulas.uzbrojenie import uzbrojenie


def if_statements(line):
    for i in kolumny:
        del i[:]
        # Formuły
    dane_adresowe = lokalizacja(line)
    dane_ulica = ulica(line)
    p_uzytkowa = powierzchnia_uzytkowa(line)
    r_osoby = rodzaj_osoby(line)
    cennik = ceny(line)
    kw_all = kw(line)

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
    m_powierzchnia_gruntu = powierzchnia_gruntu(line)
    n_powierzchnia_uzytkowa = p_uzytkowa[0]
    o_podstawa_ustalenia = p_uzytkowa[1]
    p_cena = cennik[0]
    q_cena_m2 = ['']
    r_typ_domu = ['']
    s_zrodlo_informacji = r_osoby[1]
    # t_opis = ['']
    u_konstrukcja_budynku = ['']
    v_rok_budowy = ['']
    w_cena_brutto = cennik[1]
    x_cena_brutto_m2 = ['']
    y_stan_prawny_gruntu = stan_prawny_gruntu(line)
    z_typ_budynku = typ_budynku(line)
    aa_nr_kw = kw_all[0]
    ab_sad_wieczystoksiegowy = ['Sąd Rejonowy dla Wrocławia - Krzyków']
    ac_nr_aktu_notarialnego = nr_dok(line)
    ad_zrodlo_danych = ['RCiWN']
    ae_sprzedajacy = r_osoby[0]
    af_kupujacy = ['']
    ag_powierzchnia_zabudowy = ['']
    ah_powierzchnia_calkowita = ['']
    ai_cena_m2_pc = ['']
    aj_kubatura = ['']
    ak_liczba_kondygnacji = liczba_kondygnacji(line)
    al_standard_techniczny = ['']
    am_modernizowany = ['']
    an_pozostale_obiekty = ['']
    ao_funkcjonalnosc_budynku = ['']
    ap_ekspozycja_budynku = ['']
    aq_powierzchnia_wynajmu = ['']
    ar_stawka_czynszu = ['']
    as_ksztalkt = ['']
    at_dlugosc_frontu_dzialki = ['']
    au_glebokosc_dzialki = ['']
    av_uzbrojenie = ['']
    aw_kod_pocztowy = dane_ulica[2]
    ax_osiedle = ['']
    ay_strefa_miasta = ['']
    az_otoczenie = ['']
    ba_dostepnosc_komunikacyjna = ['']
    bb_zrodlo_ceny = ['Transakcja']
    bc_cena_waluta = ['']
    bd_waluta = ['PLN']
    be_kurs_waluty = ['']
    bf_stan_prawny = ['Prawo własności']
    bg_numer_kw_budynku = ['']
    bh_prawo_do_wieczystego = ['']
    bi_dzial_iii_kw = ['']
    bj_wartosc_rynkowa = ['']
    bk_wartosc_odtworzeniowa = ['']
    bl_stawka_vat = ['']
    bm_data_utworzenia = ['']
    bn_data_modyfikacji = ['']
    bo_wpisana_przez = ['']
    bp_modyfikowana_przez = ['']
    bq_winda = ['']
    br_swiadectwo_ch = ['']
    bs_nr_sw_ener = ['']
    bt_wskaznik_ep = ['']
    bu_wskaznik_ek = ['']
    bv_garaz = ['']
    bw_inne_pomieszczenia = ['']
    bx_udzial = udzial(line)
    by_funkcja = funkcja(line)
    bz_przeznaczenie_terenu = przeznaczenie_terenu(line)

    t_opis = re.sub(r'^$', '', re.sub(r'^;', '', re.sub(r';{2,}', '',
             re.sub(r'\n', '', '{0};{1};{2};księgi podane w RCiWN: {3};{4}' .format(cennik[2],
             opis(line), dane_adresowe[6], kw_all[1], uzbrojenie(line))))))
    # a_id = geo(dane_ulica[0], dane_ulica[1])
    z = np.column_stack((a_id, b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc, g_dzielnica,
                         h_obreb_geodezyjny,
                         i_arkusz, j_ulica, k_nr_budynku, l_nr_dzialki, m_powierzchnia_gruntu, n_powierzchnia_uzytkowa,
                         o_podstawa_ustalenia,
                         p_cena, q_cena_m2, r_typ_domu, s_zrodlo_informacji, t_opis, u_konstrukcja_budynku,
                         v_rok_budowy,
                         w_cena_brutto, x_cena_brutto_m2, y_stan_prawny_gruntu, z_typ_budynku, aa_nr_kw,
                         ab_sad_wieczystoksiegowy,
                         ac_nr_aktu_notarialnego, ad_zrodlo_danych, ae_sprzedajacy, af_kupujacy,
                         ag_powierzchnia_zabudowy,
                         ah_powierzchnia_calkowita, ai_cena_m2_pc, aj_kubatura, ak_liczba_kondygnacji,
                         al_standard_techniczny,
                         am_modernizowany, an_pozostale_obiekty, ao_funkcjonalnosc_budynku, ap_ekspozycja_budynku,
                         aq_powierzchnia_wynajmu,
                         ar_stawka_czynszu, as_ksztalkt, at_dlugosc_frontu_dzialki, au_glebokosc_dzialki, av_uzbrojenie,
                         aw_kod_pocztowy, ax_osiedle, ay_strefa_miasta, az_otoczenie, ba_dostepnosc_komunikacyjna,
                         bb_zrodlo_ceny, bc_cena_waluta, bd_waluta, be_kurs_waluty, bf_stan_prawny, bg_numer_kw_budynku,
                         bh_prawo_do_wieczystego, bi_dzial_iii_kw, bj_wartosc_rynkowa, bk_wartosc_odtworzeniowa,
                         bl_stawka_vat,
                         bm_data_utworzenia, bn_data_modyfikacji, bo_wpisana_przez, bp_modyfikowana_przez,
                         bq_winda, br_swiadectwo_ch,
                         bs_nr_sw_ener, bt_wskaznik_ep, bu_wskaznik_ek, bv_garaz, bw_inne_pomieszczenia, bx_udzial,
                         by_funkcja, bz_przeznaczenie_terenu))
    return z
