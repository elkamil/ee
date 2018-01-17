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
m_powierzchnia_gruntu = ['']
n_powierzchnia_uzytkowa = ['']
o_podstawa_ustalenia = ['']
p_cena = ['']
q_cena_m2 = ['']
r_typ_domu = ['']
s_zrodlo_informacji = ['']
t_opis = ['']
u_konstrukcja_budynku = ['']
v_rok_budowy = ['']
w_cena_brutto = ['']
x_cena_brutto_m2 = ['']
y_stan_prawny_gruntu = ['']
z_typ_budynku = ['']
aa_nr_kw = ['']
ab_sad_wieczystoksiegowy = ['']
ac_nr_aktu_notarialnego = ['']
ad_zrodlo_danych = ['']
ae_sprzedajacy = ['']
af_kupujacy = ['']
ag_powierzchnia_zabudowy = ['']
ah_powierzchnia_calkowita = ['']
ai_cena_m2_pc = ['']
aj_kubatura = ['']
ak_liczba_kondygnacji = ['']
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
aw_kod_pocztowy = ['']
ax_osiedle = ['']
ay_strefa_miasta = ['']
az_otoczenie = ['']
ba_dostepnosc_komunikacyjna = ['']
bb_zrodlo_ceny = ['']
bc_cena_waluta = ['']
bd_waluta = ['']
be_kurs_waluty = ['']
bf_stan_prawny = ['']
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
bx_udzial = ['']
by_funkcja = ['']
bz_przeznaczenie_terenu = ['']

header_csv = ["Id", "Data transakcji / wyceny", "Województwo", "Powiat", "Gmina", "Miejscowość", "Dzielnica",
              "Obręb geodezyjny", "Arkusz mapy", "Ulica", "Nr budynku", "Numer działki",
              "Pole powierzchni gruntu (m2)", "Powierzchnia użytkowa (m2)",
              "Podstawa ustalenia Pu", "Cena", "Cena m2 p.u.", "Typ domu", "Źródło informacji", "Opis",
              "Konstrukcja budynku", "Rok budowy", "Cena brutto", "Cena brutto m2 p.u.",
              "Stan prawny grunt", "Typ budynku", "Nr KW", "Sąd wieczystoksięgowy",
              "Nr aktu notarialnego", "Źródło danych do wpisu", "Sprzedający", "Kupujący", "Powierzchnia zabudowy (m2)",
              "Powierzchnia całkowita (m2)", "Cena m2 p.c.", "Kubatura", "Liczba kondygnacji",
              "Standard techniczny budynku", "Modernizowany w ostatnich 5 latach",
              "Pozostałe obiekty", "Funkcjonalność budynku", "Ekspozycja budynku", "Powierzchnia wynajmu (m2)",
              "Stawka czynszu (PLN / m2 Pu)",
              "Kształt", "Długość frontu działki (m)", "Głębokość działki", "Uzbrojenie i dostęp do mediów",
              "Kod pocztowy", "Osiedle", "Strefa miasta",
              "Otoczenie", "Dostępność komunikacyjna", "Źródło ceny", "Cena (waluta)", "Waluta",
              "Kurs waluty z daty transakcji jeżeli watuta inna niż PLN",
              "Stan prawny budynek", "Numer KW budynku (dotyczy budynków stanowiących nieruchomość odrębną od działki)",
              "Prawo do wieczystego uzytkowania gruntu - do kiedy", "Dział III KW (budynku)", "Wartość rynkowa",
              "Wartość odtworzeniowa", "Stawka VAT", "Data utworzenia", "Data modyfikacji", "Wpisana przez",
              "Modyfikowana przez", "Winda", "Świadectwo charakterystyki energetycznej", "Nr św. ch. energetycznej",
              "Wskaźnik zapotrzebowania na energię pierwotną (EP)", "Wskaźnik zapotrzebowania na energię końcową (EK)",
              "Garaż", "Pomieszczenia inne przynależne - opis", "Udział", "Funkcja", "Przeznaczenie terenu"]

kolumny = [a_id, b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc, g_dzielnica, h_obreb_geodezyjny,
           i_arkusz, j_ulica, k_nr_budynku, l_nr_dzialki, m_powierzchnia_gruntu, n_powierzchnia_uzytkowa,
           o_podstawa_ustalenia,
           p_cena, q_cena_m2, r_typ_domu, s_zrodlo_informacji, t_opis, u_konstrukcja_budynku, v_rok_budowy,
           w_cena_brutto, x_cena_brutto_m2, y_stan_prawny_gruntu, z_typ_budynku, aa_nr_kw, ab_sad_wieczystoksiegowy,
           ac_nr_aktu_notarialnego, ad_zrodlo_danych, ae_sprzedajacy, af_kupujacy, ag_powierzchnia_zabudowy,
           ah_powierzchnia_calkowita, ai_cena_m2_pc, aj_kubatura, ak_liczba_kondygnacji, al_standard_techniczny,
           am_modernizowany, an_pozostale_obiekty, ao_funkcjonalnosc_budynku, ap_ekspozycja_budynku,
           aq_powierzchnia_wynajmu,
           ar_stawka_czynszu, as_ksztalkt, at_dlugosc_frontu_dzialki, au_glebokosc_dzialki, av_uzbrojenie,
           aw_kod_pocztowy, ax_osiedle, ay_strefa_miasta, az_otoczenie, ba_dostepnosc_komunikacyjna,
           bb_zrodlo_ceny, bc_cena_waluta, bd_waluta, be_kurs_waluty, bf_stan_prawny, bg_numer_kw_budynku,
           bh_prawo_do_wieczystego, bi_dzial_iii_kw, bj_wartosc_rynkowa, bk_wartosc_odtworzeniowa, bl_stawka_vat,
           bm_data_utworzenia, bn_data_modyfikacji, bo_wpisana_przez, bp_modyfikowana_przez, bq_winda, br_swiadectwo_ch,
           bs_nr_sw_ener, bt_wskaznik_ep, bu_wskaznik_ek, bv_garaz, bw_inne_pomieszczenia, bx_udzial, by_funkcja,
           bz_przeznaczenie_terenu]
