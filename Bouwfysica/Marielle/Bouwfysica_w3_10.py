import random

from Bouwfysica.Marielle.Bouwfysica_w3_7 import materiaal
from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 04-09-2024
#$adgo_lib
#$adgo_bouwfysica_lib

# In een bestaande woning wordt het schuin dak nageïsoleerd.
# De bewoners willen graag een Rc van 4,7/6,0/8,0 m2K/W realiseren.
# We gaan er van uit dat de nieuwe isolatie voor deze Rc waarde moet zorgen.
# Hoe dik moet de isolatielaag zijn als deze bestaat uit cellulose/glaswol/PIR (in mm)?

Rc_lijst = [
    {'Rc': 4.7},
    {'Rc': 6.0},
    {'Rc': 8.0}
]

keuze = random.choice(Rc_lijst)
Rc = keuze['Rc']

materialen = [
    {'materiaal': 'cellulose','lambda': 0.038},
    {'materiaal': 'glaswol','lambda': 0.037},
    {'materiaal': 'PIR','lambda': 0.024}
]

keuze = random.choice(materialen)
materiaal = keuze['materiaal']
Lambda = keuze['lambda']

dikte_m = Rc * Lambda
dikte_mm = round(dikte_m * 1000, 0)

print(Rc) # [0]
print(materiaal) # [1]
print(Lambda) # [2]
print(dikte_mm) # [3]



#")
