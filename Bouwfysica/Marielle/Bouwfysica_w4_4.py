import math
import random

from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 15-01-2025
#$adgo_lib
#$adgo_bouwfysica_lib

lijst = [
    {'Set': 1, 'c': 23.05, 't': 25},
    {'Set': 2, 'c': 21.78, 't': 24},
    {'Set': 3, 'c': 20.55, 't': 23},
    {'Set': 4, 'c': 19.43, 't': 22},
    {'Set': 5, 'c': 18.35, 't': 21},
    {'Set': 6, 'c': 17.28, 't': 20},
    {'Set': 7, 'c': 16.30, 't': 19},
    {'Set': 8, 'c': 15.37, 't': 18},
    {'Set': 9, 'c': 14.47, 't': 17},
    {'Set': 10, 'c': 13.65, 't': 16},
    {'Set': 11, 'c': 12.85, 't': 15},
]

# a. Wat is de R.V. van lucht met een temperatuur van 18°C en een absolute luchtvochtigheid c van 12 g/m3?
gekozen_set1 = random.choice(lijst)
c_max1 = gekozen_set1['c']
temp1 =gekozen_set1['t']
RV1 = kies_integer_getal_stap(50,90,10)
c_lucht1 = round(c_max1 * RV1 / 100, 2)


# b. Wat is de absolute luchtvochtigheid van lucht met een temperatuur van 18°C en een R.V. van 60%?
gekozen_set2 = random.choice(lijst)
while gekozen_set1 == gekozen_set2:
    gekozen_set2 = random.choice(lijst)

c_max2 = gekozen_set2['c']
temp2 =gekozen_set2['t']
RV2 = kies_integer_getal_stap(50,90,10)
c_lucht2 = round(c_max2 * RV2 / 100, 2)

print([c_max1,temp1,RV1,c_lucht1,c_max2,temp2,RV2,c_lucht2])

#")
