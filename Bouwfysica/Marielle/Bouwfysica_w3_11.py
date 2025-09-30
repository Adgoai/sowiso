import random

from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 04-09-2024
#$adgo_lib
#$adgo_bouwfysica_lib

# Wat is de U-waarde van een dak als de Rc waarde 4,7/6/8/10 m2K/W bedraagt?

Rc_lijst = [
    {'Rc': 4.7},
    {'Rc': 6},
    {'Rc': 8},
    {'Rc': 10}
]

keuze = random.choice(Rc_lijst)

Rc = keuze['Rc']

Rsi = 0.10 # m²K/W
Rse = 0.04 # m²K/W
RT = Rsi + Rse + Rc
U = 1 / RT
U = round(U, 2)

print(Rc) # [0]
print(Rsi) # [1]
print(Rse) # [2]
print(U) # [3]

#")
