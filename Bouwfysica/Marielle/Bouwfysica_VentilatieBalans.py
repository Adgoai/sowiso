from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 28-11-2024
#$adgo_lib

# oppervlaktes
O_hal_b = 6
O_woonkamer_b = 60
O_badkamer_1 = 9
O_kamer1_1 = 10
O_kamer2_1 = 16
O_kamer3_1 = 16
O_kamer4_1 = 8
O_ruimte1_2 = 12
O_ruimte2_2 = 8
O_kamer_2 = 35

# luchtvolumes
Q_slaapkamer_2 = 31.5 # l/s
Q_badkamer_2 = 14 # l/s
Q_toilet_2 = 7 # l/s
Q_naar_beneden_2 = 10.5 # l/s
Q_van_boven_1 = Q_naar_beneden_2 # l/s
Q_slaapkamer1_1  = 9 # l/s
Q_slaapkamer2_1 = 14.4 # l/s
Q_slaapkamer3_1 = 7.2 # l/s
Q_slaapkamer4_1 = 10.8 # l/s
Q_badkamer_1 = 14 # l/s
Q_toilet_1 = 7 # l/s
Q_naar_beneden_1 = 30.9 # l/s
Q_van_boven_b = Q_naar_beneden_1 # l/s
Q_toilet_b = 7 # l/s
Q_overstroom_b = 23.9 # l/s
Q_woonkamer_b = 30.1 # l/s
Q_keuken_b = 54 # l/s

eindbalans_plus = Q_woonkamer_b + Q_slaapkamer1_1 + Q_slaapkamer2_1 + Q_slaapkamer3_1 + Q_slaapkamer4_1 + Q_slaapkamer_2
eindbalans_min = Q_keuken_b + Q_toilet_b + Q_badkamer_1 + Q_toilet_1 + Q_badkamer_2 + Q_toilet_2

#formule Qventilatie
dichtheid_lucht = 1.25
soortelijke_warmte = 1000
Debiet = 0
Tbinnen =18
Tbuiten = 5
uren = 4000

Qventilatie= dichtheid_lucht * soortelijke_warmte * Debiet * (Tbinnen - Tbuiten) * uren / 1000000

#formuleQventilatie2
ventilatievoud = 0.5
netto_volume = 100
Qventilatie2 = 0.35 * ventilatievoud * netto_volume * (Tbinnen - Tbuiten) * uren / 1000

print([O_hal_b, O_woonkamer_b, O_badkamer_1, O_kamer1_1, O_kamer2_1, O_kamer3_1, O_kamer4_1, O_ruimte1_2, O_ruimte2_2,
       O_kamer_2, Q_slaapkamer_2, Q_badkamer_2, Q_toilet_2, Q_naar_beneden_2, Q_van_boven_1, Q_slaapkamer1_1,
       Q_slaapkamer2_1, Q_slaapkamer3_1, Q_slaapkamer4_1, Q_badkamer_1, Q_toilet_1, Q_naar_beneden_1, Q_van_boven_b,
       Q_toilet_b, Q_overstroom_b, Q_woonkamer_b, Q_keuken_b, eindbalans_plus, eindbalans_min, Qventilatie, Qventilatie2
])

#")
