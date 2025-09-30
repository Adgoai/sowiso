from adgo_lib import kies_getal_tussen, kies_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 7-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 1
print(decimalen) # [0]

antwoorden_lijst = [
    {'Set': 1, 'w': 22, 'f': 4000, 'd': 5, 'H': 0.9, 'T': 3.3},
    {'Set': 2, 'w': 30, 'f': 3000, 'd': 4, 'H': 1, 'T': 3.6},
    {'Set': 3, 'w': 22, 'f': 2000, 'd': 3, 'H': 0.6, 'T': 2.8},
    {'Set': 4, 'w': 30, 'f': 1000, 'd': 6, 'H': 0.8, 'T': 3.0},
    {'Set': 5, 'w': 22, 'f': 1500, 'd': 5, 'H': 0.6, 'T': 2.8},
    {'Set': 6, 'w': 30, 'f': 2500, 'd': 4, 'H': 1, 'T': 3.5},
    {'Set': 7, 'w': 22, 'f': 3500, 'd': 3, 'H': 0.7, 'T': 3.1},
    {'Set': 8, 'w': 30, 'f': 3000, 'd': 4, 'H': 1, 'T': 3.6},
    {'Set': 9, 'w': 22, 'f': 2000, 'd': 5, 'H': 0.7, 'T': 2.9},
    {'Set': 10, 'w': 30, 'f': 1500, 'd': 6, 'H': 0.9, 'T': 3.2}
]

gekozen_antwoord = random.choice(antwoorden_lijst)

diepte = gekozen_antwoord['d']
print(diepte) # [1]

strijklengte = gekozen_antwoord['f']
print(strijklengte) # [2]

windsnelheid = gekozen_antwoord['w']
print(windsnelheid) # [3]

# Vraag 19 In deze opgave ga je de golfhoogte H en periode T berekenen die optreden ter plaatse van een dijk aan een meer. Het meer heeft een gemiddelde diepte van 5 m. De effectieve strijklengte is 4000 m. De windsnelheid die aangehouden wordt bedraagt 22 m/s.
# Bereken de golfhoogte H met de formule van Bretschneider

H = gekozen_antwoord['H']
print(round(H, decimalen))  # [4]

# Vraag 20 Bereken de periode T met de formule van Bretschneider
periode = gekozen_antwoord['T']
print(round(periode, decimalen))  # [5]

#")
