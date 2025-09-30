import random
from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 15-01-2025
#$adgo_lib
#$adgo_bouwfysica_lib

# We bekijken een isolatielaag van 150 mm met λ = 0,035 W/mK.

dikte_isolatie = 150 # mm
dikte_isolatie_m = dikte_isolatie / 1000 # m
lambda_isolatie = 0.035 # W/mK

# a. Bereken de warmteweerstand R van de isolatielaag in m²K/W
R_isolatie = round(dikte_isolatie_m / lambda_isolatie, 2)

# b Wat is het transmissieverlies door een scheidingsconstructie van 10m2 (variëren van 5 t/m 20 m2 met stappen van 0,5) met die R-waarde?

A_opp = kies_getal_stap(5, 20.5, 0.5, 10)

U_coeff = round(1/R_isolatie, 2)   # W/m2K

a_weeg = 1

dt_temp = 14 # °C

uren = 4000

Q_transmissie = round(a_weeg * A_opp * U_coeff * dt_temp * (uren / 1000), 0)

# c Als de isolatielaag 40 mm dikker is (varianten: 20 t/m 60, met stappen van 10mm),
# hoeveel minder warmte gaat er dan verloren als de andere uitgangspunten gelijkt blijven. Geef het antwoord als percentage.

dikte_extra = kies_integer_getal_stap(20, 70, 10)
dikte_mm = dikte_isolatie + dikte_extra
dikte_m = dikte_mm / 1000

R_isolatie_extra = round(dikte_m / lambda_isolatie, 2)

U_coeff_extra = round(1/R_isolatie_extra, 2)   # W/m2K

Q_transmissie_extra = round(a_weeg * A_opp * U_coeff_extra * dt_temp * (uren / 1000), 0)

percentage_minder = round((Q_transmissie - Q_transmissie_extra) / Q_transmissie * 100, 1)

print([R_isolatie, A_opp, U_coeff, Q_transmissie, dikte_extra, Q_transmissie_extra, percentage_minder])


#")
