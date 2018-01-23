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
k_nr_domu = ['']
l_nr_lokalu = ['']
m_powierzchnia_uzytkowa = ['']
n_cena_laczna = ['']
o_cena_mp2 = ['']
p_kondygnacja = ['']
q_liczba_kondygnacji = ['']
r_liczba_izb = ['']
s_rok_budowy = ['']
t_rodzaj_budynku = ['']
u_stan_prawny_lokalu = ['']
v_stan_prawny_gruntu = ['']
w_zrodlo_informacji = ['']
x_funkcja = ['']
y_stopa = ['']
z_opis = ['']
aa_konstrukcja = ['']
ab_nr_kw = ['']
ac_sad_wieczysty = ['']
ad_nr_aktu = ['']
ae_zrodlo_danych = ['']
af_sprzedajacy = ['']
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
ay_kod_pocztowy = ['']
az_osiedle = ['']
ba_strefa_miasta = ['']
bb_otoczenie = ['']
bc_dostepnosc_kom = ['']
bd_zrodlo_ceny = ['']
be_cena_waluta = ['']
bf_waluta = ['']
bg_kurs_waluty = ['']
bh_stan_prawny_budynku = ['']
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
bu_nr_dzialki = ['']
bv_pole_powierzchni_gruntu = ['']
bw_cena_brutto = ['']
ulica_geo = ['']
y_typ_wlasciciela = ['']
xxx_ulica_geo = ['']


header_csv = ["Id", "Data transakcji / wyceny", "Województwo", "Powiat", "Gmina", "Miejscowość", "Dzielnica",
              "Obręb geodezyjny", "Arkusz mapy", "Ulica", "Nr domu", "Nr lokalu", "Powierzchnia użytkowa (m2)",
              "Cena", "Cena m2 p.u.", "Kondygnacja lokalu", "Liczba kondygnacji", "Liczba izb", "Rok budowy",
              "Rodzaj budynku", "Stan prawny lokalu", "Stan prawny gruntu", "Źródło informacji",
              "Funkcja użytkowa lokalu", "Stopa kapitalizacji (%)", "Opis", "Konstrukcja budynku", "Nr KW",
              "Sąd wieczystoksięgowy", "Nr aktu notarialnego", "Źródło danych do wpisu", "Sprzedający", "Kupujący",
              "Pomieszczenia przynależne - ilość", "Pomieszczenie przynależne - opis",
              "Cena p. przynależnego zawarta w cenie transakcyjnej", "Pomieszczenia przynależne - Cena za sztukę",
              "Liczba miejsc postojowych", "Rodzaj miejsca postojowego",
              "Cena m. postojowego zawarta w cenie transakcyjnej", "M. postojowe - Cena za sztukę",
              "Pomieszczenia inne przynależne", "Pozostałe obiekty", "Funkcjonalność lokalu",
              "Standard lokalu użytkowego", "Powierzchnia użytkowa budynku", "Standard techniczny budynku",
              "Modernizowany w ostatnich 5 latach", "Ekspozycja lokalu", "Winda", "Kod pocztowy", "Osiedle",
              "Strefa miasta", "Otoczenie", "Dostępność komunikacyjna", "Źródło ceny", "Cena (waluta)", "Waluta",
              "Kurs waluty z dn. transakcji", "Stan prawny budynku", "Dział III KW lokalu", "Dział III KW gruntu",
              "Wartość rynkowa", "Wartość odtworzeniowa", "Data utworzenia", "Data modyfikacji", "Wpisana przez",
              "Modyfikowana przez", "Świadectwo charakterystyki energetycznej", "Nr św. ch. energetycznej",
              "Wskaźnik zapotrzebowania na energię pierwotną (EP)",
              "Wskaźnik zapotrzebowania na energię pierwotną (EK)", "Numer działki", "Pow. działki", "Cena brutto",
              "Street View"]

kolumny = [a_id, b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc, g_dzielnica, h_obreb_geodezyjny,
           i_arkusz, j_ulica, k_nr_domu, l_nr_lokalu, m_powierzchnia_uzytkowa, n_cena_laczna, o_cena_mp2,
           p_kondygnacja, q_liczba_kondygnacji, r_liczba_izb, s_rok_budowy, t_rodzaj_budynku, u_stan_prawny_lokalu,
           v_stan_prawny_gruntu, w_zrodlo_informacji, x_funkcja, y_stopa, z_opis, aa_konstrukcja, ab_nr_kw,
           ac_sad_wieczysty, ad_nr_aktu, ae_zrodlo_danych, af_sprzedajacy, ag_kupujacy, ah_pom_przynalezne_ilosc,
           ai_pom_przynalezne_opis, aj_cena_pom_przyn, ak_cena_pom_przyn_sztuka, al_liczba_miejsc_post,
           am_rodzaj_miejsca_post, an_cena_miejsca_post, ao_miejsce_post_cena, ap_pom_inne_przyn, aq_pozostale_obiekty,
           ar_funkcjonalnosc_lokalu, as_standard_lokalu, at_powierzchnia_uzytkowa_budynky, au_stand_tech,
           av_mod_last_5_y, aw_ekspozycja_lokalu, ax_winda, ay_kod_pocztowy, az_osiedle, ba_strefa_miasta,
           bb_otoczenie, bc_dostepnosc_kom, bd_zrodlo_ceny, be_cena_waluta, bf_waluta, bg_kurs_waluty,
           bh_stan_prawny_budynku, bi_dzial_3, bj_dzial_3_grunt, bk_wartosc_rynkowa, bl_wartosc_odtworzeniowa,
           bm_data_utworzenia, bn_data_modyfikacji, bo_wpisana_przez, bp_modyfikowana_przez, bq_sw_ch_energ,
           br_nr_sw_ch_energ, bs_wsk_zapot, bt_wsk_zapot_EK, bu_nr_dzialki, bv_pole_powierzchni_gruntu,
           bw_cena_brutto, y_typ_wlasciciela, xxx_ulica_geo]
