import random

from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 04-09-2024
#$adgo_lib
#$adgo_bouwfysica_lib

#Van een woning zijn de volgende posten van de warmtebalans bekend.

balans_lijst = [
    [5810, 11340, 3200, 15800, 4550],
    [6820, 5100, 2230, 11300, 2850],
    [8180, 6120, 2680, 13560, 3420]
]

keuze = random.choice(balans_lijst)

random_number = random.randint(0, 4)

if random_number == 0:
    Q_installatie = ''
    Q_zon = keuze[1]
    Q_intern = keuze[2]
    Q_transmissie = keuze[3]
    Q_ventilatie = keuze[4]
    Q_antwoord = keuze[0]
    Q_missing = 'installatie'
elif random_number == 1:
    Q_installatie = keuze[0]
    Q_zon = ''
    Q_intern = keuze[2]
    Q_transmissie = keuze[3]
    Q_ventilatie = keuze[4]
    Q_antwoord = keuze[1]
    Q_missing = 'zon'
elif random_number == 2:
    Q_installatie = keuze[0]
    Q_zon = keuze[1]
    Q_intern = ''
    Q_transmissie = keuze[3]
    Q_ventilatie = keuze[4]
    Q_antwoord = keuze[2]
    Q_missing = 'interne warmteproductie'
elif random_number == 3:
    Q_installatie = keuze[0]
    Q_zon = keuze[1]
    Q_intern = keuze[2]
    Q_transmissie = ''
    Q_ventilatie = keuze[4]
    Q_antwoord = keuze[3]
    Q_missing = 'transmissie'
else:
    Q_installatie = keuze[0]
    Q_zon = keuze[1]
    Q_intern = keuze[2]
    Q_transmissie = keuze[3]
    Q_ventilatie = ''
    Q_antwoord = keuze[4]
    Q_missing = 'ventilatie'

print(Q_installatie) # [0]
print(Q_zon) # [1]
print(Q_intern) # [2]
print(Q_transmissie) # [3]
print(Q_ventilatie) # [4]
print(Q_antwoord) # [5]
print(Q_missing) # [6]

#")