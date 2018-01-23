a_id = ['']
b_data_transakcji = ['']
c_wojewodztwo = ['']
d_powiat = ['']
e_gmina = ['']
f_miejscowosc = ['']
g_dzielnica = ['']
h_obreb_geodezyjny = ['']
i_arkusz = ['']
j_ulica = ['']
k_nr_budynku = ['']
l_nr_dzialki = ['']
m_oznaczenie = ['']
n_pole_powierzchni = ['']
o_powierzchnia_uzytkowa = ['']
p_cena = ['']
q_cena_mp2pu = ['']
r_opis = ['']
s_konstrukcja_budynku = ['']
t_rok_budowy = ['']
u_cena_brutto = ['']
v_cena_brutto_mp2 = ['']
w_stan_prawny_gruntu = ['']
x_nr_kw = ['']
y_sad = ['']
z_nr_aktu = ['']
aa_zrodlo_informacji = ['']
ab_zrodlo_danych = ['']
ac_sprzedajacy = ['']
ad_kupujacy = ['']
ae_typ_garazu = ['']
af_powierzchnia_zabudowy = ['']
ag_kubatura = ['']
ah_liczba_kondygnacji = ['']
ai_pozostale_obiekty = ['']
aj_kod_pocztowy = ['']
ak_osiedle = ['']
al_strefa_miasta = ['']
am_otoczenie = ['']
an_dostepnosc = ['']
ao_zrodlo_ceny = ['']
ap_cena_waluta = ['']
aq_waluta = ['']
ar_kurs_waluty = ['']
as_stan_prawny = ['']
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

header_csv = ["Id", "Data transakcji / wyceny", "Województwo", "Powiat", "Gmina", "Miejscowość", "Dzielnica",
              "Obręb geodezyjny", "Arkusz mapy", "Ulica", "Nr budynku", "Numer działki",
              "Oznaczenie parkingu / miejsca", "Pole powierzchni gruntu (m2)", "Powierzchnia użytkowa (m2)",
              "Cena", "Cena m2 p.u.", "Opis", "Konstrukcja budynku", "Rok budowy", "Cenabrutto",
              "Cena brutto m2 p.u.", "Stan prawny gruntu", "Nr KW", "Sąd wieczystoksięgowy",
              "Nr aktu notarialnego", "Źródło informacji", "Źródło danych do wpisu", "Sprzedający",
              "Kupujący", "Typ garażu / miejsca postojowego", "Powierzchnia zabudowy (m2)", "Kubatura",
              "Liczba kondygnacji", "Pozostałe obiekty", "Kod pocztowy", "Osiedle", "Strefa miasta",
              "Otoczenie", "Dostępność komunikacyjna", "Źródło ceny", "Cena (waluta)", "Waluta",
              "Kurs waluty z daty transakcji jeżeli watuta inna niż PLN", "Stan prawny budynek",
              "Dział III KW gruntu", "Wartość rynkowa", "Wartość odtworzeniowa", "Stawka VAT",
              "Data utworzenia", "Data modyfikacji", "Wpisana przez", "Modyfikowana przez", "Winda", "Street View"]


kolumny = [a_id, b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc, g_dzielnica, h_obreb_geodezyjny,
           i_arkusz, j_ulica, k_nr_budynku, l_nr_dzialki, m_oznaczenie, n_pole_powierzchni, o_powierzchnia_uzytkowa,
           p_cena, q_cena_mp2pu, r_opis, s_konstrukcja_budynku, t_rok_budowy, u_cena_brutto, v_cena_brutto_mp2,
           w_stan_prawny_gruntu, x_nr_kw, y_sad, z_nr_aktu, aa_zrodlo_informacji, ab_zrodlo_danych, ac_sprzedajacy,
           ad_kupujacy, ae_typ_garazu, af_powierzchnia_zabudowy, ag_kubatura, ah_liczba_kondygnacji,
           ai_pozostale_obiekty, aj_kod_pocztowy, ak_osiedle, al_strefa_miasta, am_otoczenie, an_dostepnosc,
           ao_zrodlo_ceny, ap_cena_waluta, aq_waluta, ar_kurs_waluty, as_stan_prawny, at_dzial_kw,
           au_wartosc_rynkowa, av_wartosc_odtworzeniowa, aw_stawka_VAT, ax_data_utworzenia, ay_data_modyfikacji,
           az_wpisana_przez, ba_modyfikowana_przez, bb_winda, xxx_ulica_geo]
kolumny1 = ["a_id", "b_data_transakcji", "c_wojewodztwo", "d_powiat", "e_gmina", "f_miejscowosc",
            "g_dzielnica", "h_obreb_geodezyjny", "i_arkusz", "h_obreb_geodezyjny", "j_ulica",
            "k_nr_domu", "l_nr_lokalu", "m_powierzchnia_uzytkowa", "n_cena_laczna", "o_cena_mp2",
            "p_cena_mp", "q_cena_mp2mp", "r_kondygnacja", "s_liczba_kondygnacji", "t_liczba_izb",
            "u_rok_budowy", "v_rodzaj_budynku", "w_stan_prawny_lokalu", "x_stan_prawny_gruntu",
            "y_typ_wlasciciela", "z_opis", "aa_konstrukcja_budynku", "ab_cena_brutto", "ac_cena_brutto_mp2",
            "ad_cena_brutto_mp", "ae_cena_brutto_mp2mp", "af_nr_kw", "ag_sad_wieczysty", "ah_nr_aktu",
            "ai_zrodlo_danych", "aj_sprzedajacy", "ak_kupujacy", "al_pom_przynalezne_ilosc",
            "am_pom_przynalezne_opis", "an_cena_pom_przyn", "ao_cena_pom_przyn_sztuka",
            "ap_liczba_miejsc_post", "aq_rodzaj_miejsca_post", "ar_cena_miejsca_post", "as_miejsce_post_cena",
            "at_pom_inne_przyn", "au_pozostale_obiekty", "av_funkcjonalnosc_lokalu", "aw_standard_lokalu",
            "ax_powierzchnia_uzytkowa_budynky", "ay_stand_tech", "az_mod_last_5_y", "ba_ekspozycja_lokalu",
            "bb_winda", "bc_kod_pocztowy", "bd_osiedle", "be_strefa_miasta", "bf_otoczenie",
            "bg_dostepnosc_kom", "bh_zrodlo_ceny", "bi_cena_waluta", "bj_waluta", "bk_kurs_waluty",
            "bl_stan_prawny_budynku", "bm_dzial_3", "bn_dzial_3_grunt", "bo_wartosc_rynkowa",
            "bp_wartosc_odtworzeniowa", "bq_stawka_vat", "br_mp_stawka_vat", "bs_data_utworzenia",
            "bt_data_modyfikacji", "bu_wpisana_przez", "bv_modyfikowana_przez", "bw_sw_ch_energ",
            "bx_nr_sw_ch_energ", "by_wsk_zapot", "bz_wsk_zapot_EK", "ca_nr_dzialki", "cb_pole_powierzchni_gruntu"]
