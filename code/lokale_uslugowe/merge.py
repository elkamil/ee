import numpy as np
import re
from lokale_uslugowe.variables import *
# from geo import geo

from lokale_uslugowe.formulas.b_data_transakcji import b_data
from lokale_uslugowe.formulas.lokalizacja import lokalizacja
from lokale_uslugowe.formulas.ulica import ulica
from lokale_uslugowe.formulas.ceny import ceny
from lokale_uslugowe.formulas.stan_prawny import stan_prawny
from lokale_uslugowe.formulas.rodzaj_budynku import rodzaj_budynku
from lokale_uslugowe.formulas.pole_powierzchni import pole_powierzchni
from lokale_uslugowe.formulas.nr_dok import nr_dok
from lokale_uslugowe.formulas.kw import kw
from lokale_uslugowe.formulas.funkcja import funkcja
from lokale_uslugowe.formulas.opis import opis as opis_f

# file = "/home/ee/ee_convert/data/obreby.csv"

# obreby_csv = pd.read_csv(file, sep=';', encoding='utf-8')


def if_statements(line):
    for i in kolumny:
        del i[:]

    dane_adresowe = lokalizacja(line)
    dane_ulica = ulica(line)

    cena = ceny(line)
    kw_all = kw(line)

    a_id = ['']
    b_data_transakcji = b_data(line)
    c_wojewodztwo = ['dolnośląskie']
    d_powiat = ['Wrocław']
    e_gmina = dane_adresowe[4]
    f_miejscowosc = dane_adresowe[5]
    g_dzielnica = dane_adresowe[6]
    h_obreb_geodezyjny = dane_adresowe[0]
    i_arkusz = dane_adresowe[1]
    j_ulica = dane_ulica[0]
    k_nr_domu = dane_ulica[1]
    l_nr_lokalu = dane_ulica[2]
    m_powierzchnia_uzytkowa = cena[5]
    n_cena_laczna = cena[3]
    o_cena_mp2 = cena[7]
    p_kondygnacja = ['']
    q_liczba_kondygnacji = ['']
    r_liczba_izb = dane_adresowe[3]
    s_rok_budowy = ['']
    t_rodzaj_budynku = rodzaj_budynku(line)
    u_stan_prawny_lokalu = ['Prawo własności']
    v_stan_prawny_gruntu = stan_prawny(line)
    w_zrodlo_informacji = cena[0]
    # w_zrodlo_informacji = ['']
    x_funkcja = funkcja(line)
    y_stopa = ['']
    aa_konstrukcja = ['']
    ab_nr_kw = kw_all[0]
    ac_sad_wieczysty = ['Sąd Rejonowy dla Wrocławia - Krzyków']
    ad_nr_aktu = nr_dok(line)
    ae_zrodlo_danych = ['RCiWN']
    af_sprzedajacy = cena[1]
    ag_kupujacy = ['']
    ah_pom_przynalezne_ilosc = ['']
    ai_pom_przynalezne_opis = ['']
    aj_cena_pom_przyn = ['']
    ak_cena_pom_przyn_sztuka = ['']
    al_liczba_miejsc_post = ['']
    am_rodzaj_miejsca_post = ['']
    an_cena_miejsca_post = ['']
    ao_miejsce_post_cena = ['']
    ap_pom_inne_przyn = ['']
    aq_pozostale_obiekty = ['']
    ar_funkcjonalnosc_lokalu = ['']
    as_standard_lokalu = ['']
    at_powierzchnia_uzytkowa_budynky = ['']
    au_stand_tech = ['']
    av_mod_last_5_y = ['']
    aw_ekspozycja_lokalu = ['']
    ax_winda = ['']
    ay_kod_pocztowy = dane_ulica[4]
    az_osiedle = ['']
    ba_strefa_miasta = ['']
    bb_otoczenie = ['']
    bc_dostepnosc_kom = ['']
    bd_zrodlo_ceny = ['Transakcja']
    be_cena_waluta = ['']
    bf_waluta = ['PLN']
    bg_kurs_waluty = ['']
    bh_stan_prawny_budynku = ['Prawo własności']
    bi_dzial_3 = ['']
    bj_dzial_3_grunt = ['']
    bk_wartosc_rynkowa = ['']
    bl_wartosc_odtworzeniowa = ['']
    bm_data_utworzenia = ['']
    bn_data_modyfikacji = ['']
    bo_wpisana_przez = ['']
    bp_modyfikowana_przez = ['']
    bq_sw_ch_energ = ['']
    br_nr_sw_ch_energ = ['']
    bs_wsk_zapot = ['']
    bt_wsk_zapot_EK = ['']
    bu_nr_dzialki = dane_adresowe[2]
    bv_pole_powierzchni_gruntu = pole_powierzchni(line)
    bw_cena_brutto = cena[4]

    # y_typ_wlasciciela = cena[0]
    # cc_udzial = udzial(line)
    # ulica_geo = ['']
    if cena[2]:
        cena_opis = cena[2]
    else:
        cena_opis = ''

    if opis_f(line):
        opis_opis = opis_f(line)
    else:
        opis_opis = ''

    if dane_adresowe[7]:
        adres_opis = dane_adresowe[7]
    else:
        adres_opis = ''

    if kw_all[1]:
        kw_opis = 'księga gruntowa: {0}'.format(kw_all[1])
    else:
        kw_opis = ''

    tt = ''
    for i in [cena_opis, opis_opis, adres_opis, kw_opis]:
        if i:
            tt+=str(i) + ';'
    tt = re.sub(r';$', '', re.sub(r'\n', '', tt))
    # s_opis = re.sub(r'^$', '', re.sub(r'^;', '', re.sub(r';{2,}', '',
     #        re.sub(r'\n', '', '{0};{1};{2};księgi podane w RCiWN: {3};{4}' .format(cennik[2],
     #        opis(line), dane_adresowe[6], nr_kw[1], uzbrojenie(line))))))
    # t_opis = tt
    # opis_all = re.sub(r'^$', '', re.sub(r'^;', '', re.sub(r';{2,}', '', re.sub(r'\n', '', '{0};{1};{2};księga gruntowa: {3}' .format(cena[2], opis_f(line), dane_adresowe[7], kw_all[1])))))
    z_opis = tt

    # a_id = geo(dane_ulica[0], dane_ulica[1])
    z = np.column_stack((a_id, b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc, g_dzielnica,
                         h_obreb_geodezyjny, i_arkusz, j_ulica, k_nr_domu, l_nr_lokalu, m_powierzchnia_uzytkowa,
                         n_cena_laczna, o_cena_mp2, p_kondygnacja, q_liczba_kondygnacji, r_liczba_izb, s_rok_budowy,
                         t_rodzaj_budynku, u_stan_prawny_lokalu, v_stan_prawny_gruntu, w_zrodlo_informacji, x_funkcja,
                         y_stopa, z_opis, aa_konstrukcja, ab_nr_kw, ac_sad_wieczysty, ad_nr_aktu, ae_zrodlo_danych,
                         af_sprzedajacy, ag_kupujacy, ah_pom_przynalezne_ilosc, ai_pom_przynalezne_opis,
                         aj_cena_pom_przyn, ak_cena_pom_przyn_sztuka, al_liczba_miejsc_post, am_rodzaj_miejsca_post,
                         an_cena_miejsca_post, ao_miejsce_post_cena, ap_pom_inne_przyn, aq_pozostale_obiekty,
                         ar_funkcjonalnosc_lokalu, as_standard_lokalu, at_powierzchnia_uzytkowa_budynky,
                         au_stand_tech, av_mod_last_5_y, aw_ekspozycja_lokalu, ax_winda, ay_kod_pocztowy, az_osiedle,
                         ba_strefa_miasta, bb_otoczenie, bc_dostepnosc_kom, bd_zrodlo_ceny, be_cena_waluta, bf_waluta,
                         bg_kurs_waluty, bh_stan_prawny_budynku, bi_dzial_3, bj_dzial_3_grunt, bk_wartosc_rynkowa,
                         bl_wartosc_odtworzeniowa, bm_data_utworzenia, bn_data_modyfikacji, bo_wpisana_przez,
                         bp_modyfikowana_przez, bq_sw_ch_energ, br_nr_sw_ch_energ, bs_wsk_zapot, bt_wsk_zapot_EK,
                         bu_nr_dzialki, bv_pole_powierzchni_gruntu, bw_cena_brutto))
    # g = z.decode("utf-8")
    # [re.sub(r'\s+$', '', i) for i in g]
    # print(z)
    return z
