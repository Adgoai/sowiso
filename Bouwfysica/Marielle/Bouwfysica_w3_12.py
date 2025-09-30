import random

from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 15-01-2025
#$adgo_lib
#$adgo_bouwfysica_lib

# Bereken Qtransmissie door een deel van de uitwendige scheidingconstructie waarvan is gegeven:

a_factor = 1

A_opp = kies_getal_stap(1, 10.5,0.5,1)

U_coeff = kies_getal_stap(0.25, 2.25, 0.25, 2)

dt_temp = kies_integer_getal_stap(13,17,1)

uren = kies_integer_getal_stap(3000, 4500, 500)

Q_transmissie = round(a_factor * A_opp * U_coeff * dt_temp * (uren / 1000),0)

print([a_factor, A_opp, U_coeff, dt_temp, uren, Q_transmissie])

#")
