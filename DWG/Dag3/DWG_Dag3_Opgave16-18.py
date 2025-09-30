from adgo_lib import kies_getal_tussen, kies_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.


#sw_Python("
#versie 7-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

antwoorden_lijst = [
    {'Set': 1, 'h': 2, 'w': 0.3, 'H1': 0.3, 'L': 6},
    {'Set': 2, 'h': 4, 'w': 1, 'H1': 0.6, 'L': 9},
    {'Set': 3, 'h': 6, 'w': 3, 'H1': 0.8, 'L': 17},
    {'Set': 4, 'h': 8, 'w': 6, 'H1': 1.2, 'L': 22},
    {'Set': 5, 'h': 10, 'w': 12, 'H1': 1.5, 'L': 31},
    {'Set': 6, 'h': 2, 'w': 3, 'H1': 0.7, 'L': 18},
    {'Set': 7, 'h': 4, 'w': 12, 'H1': 0.9, 'L': 22},
    {'Set': 8, 'h': 6, 'w': 12, 'H1': 1.2, 'L': 26},
    {'Set': 9, 'h': 8, 'w': 30, 'H1': 1.6, 'L': 37},
    {'Set': 10, 'h': 10, 'w': 30, 'H1': 1.8, 'L': 40}
]

gekozen_antwoord = random.choice(antwoorden_lijst)

waterdiepte = gekozen_antwoord['h']
print(waterdiepte) # [1]

effectieveStrijklengte = gekozen_antwoord['w']
print(effectieveStrijklengte) # [2]

# vraag 16
# De waterdiepte bedraagt ..m, het stormt met een windsnelheid van 22 m/s. De effectieve strijklengte is .. km
# Bepaal op basis van grafiek 9.10 uit Nortier de golfhoogte H
golfhoogte = gekozen_antwoord['H1']
print(golfhoogte) # [3]

# vraag 17 Bepaal op basis van grafiek 9.10 uit Nortier de golflengte L (m)
golflengte = gekozen_antwoord['L']
print(golflengte) # [4]

# Vraag 18 Bereken de voortplantingssnelheid van de golf (m/s)
voorplantingssnelheid = math.sqrt(water.g * golflengte / (2 * math.pi) * math.tanh(2 * math.pi * waterdiepte / golflengte))
print(round(voorplantingssnelheid, decimalen)) # [5]

#")
