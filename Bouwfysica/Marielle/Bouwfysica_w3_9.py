import random

from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 19-09-2024
#$adgo_lib
#$adgo_bouwfysica_lib

# In een bestaande woning met een spouwmuur, wil men de isolatie verbeteren door de spouw te vullen met EPS parels.

# vraag a Wat is de warmtegeleidingscoëfficient van EPS-parels (opzoeken in tabellenboek of op internet)?

lambda_min = 0.033 # W/mK
lambda_max = 0.042  # W/mK
lambda_gem = round((lambda_min + lambda_max) / 2, 3)

# Wat is de Rc-waarde van de isolatie als de spouw 40/50/60/70 mm is?

dikte_spouw = [
    {'dikte': 40},
    {'dikte': 50},
    {'dikte': 60},
    {'dikte': 70}
]

keuze = random.choice(dikte_spouw)

dikte = keuze['dikte']
dikte_m = round(dikte / 1000, 3)

#Omdat antwoord afhankelijk is van a, berkening in sowiso zelf

print(lambda_min) # [0]
print(lambda_max) # [1]
print(lambda_gem) # [2]
print(dikte) # [3]
print(dikte_m) # [4]



#")
