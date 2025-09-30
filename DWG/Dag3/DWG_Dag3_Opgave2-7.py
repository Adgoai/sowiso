from adgo_lib import kies_getal_tussen, kies_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Opgave diepwaterwindgolven
# # Voor het beantwoorden van de volgende vragen moet gebruik gemaakt worden van de grafieken 9.9 (blz 341) 9.12, 9.14b en 9.14c uit Nortier. Wellicht is het verstandig een kopie van de grafieken te maken, zodat je lijntjes in de grafieken kan tekenen. Probleem bij het aflezen van getallen uit grafieken is de nauwkeurigheid. De range waarbinnen de aflezing moet vallen is daarom bij deze opgaven ruim aangehouden. Bij het verder verwerken van de aflezingen moet je uitgaan van het getal welk door moodle als "juist antwoord" wordt gegeven.
# De effectieve strijklengte bedraagt ... km.
# Als windsnelheid wordt .. m/s aangehouden.
# We nemen aan dat het om een diepwatergolf gaat. Achteraf ga je dit controleren.


#sw_Python("
#versie 21-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

antwoorden_lijst = [
    {'Set': 1, 'f': 2, 'w': 12.5, 'H0': 0.4, 'T': 2.2, 'L0': 8, 'duur': 0.45},
    {'Set': 2, 'f': 6, 'w': 12.5, 'H0': 0.7, 'T': 2.8, 'L0': 12, 'duur': 1.0},
    {'Set': 3, 'f': 6, 'w': 25, 'H0': 1.4, 'T': 3.9, 'L0': 24, 'duur': 0.8},
    {'Set': 4, 'f': 15, 'w': 25, 'H0': 2.2, 'T': 5.0, 'L0': 39, 'duur': 1.5},
    {'Set': 5, 'f': 60, 'w': 12.5, 'H0': 2.1, 'T': 5.2, 'L0': 42, 'duur': 5.8},
    {'Set': 6, 'f': 35, 'w': 20, 'H0': 2.8, 'T': 5.8, 'L0': 52, 'duur': 3.0},
    {'Set': 7, 'f': 60, 'w': 25, 'H0': 4.5, 'T': 7.4, 'L0': 85, 'duur': 4.0},
    {'Set': 8, 'f': 200, 'w': 20, 'H0': 6, 'T': 9.0, 'L0': 126, 'duur': 11.0},
    {'Set': 9, 'f': 400, 'w': 25, 'H0': 9.9, 'T': 12.0, 'L0': 225, 'duur': 17.0},
    {'Set': 10, 'f': 600, 'w': 20, 'H0': 7.3, 'T': 11.0, 'L0': 189, 'duur': 24.0},

]

gekozen_antwoord = random.choice(antwoorden_lijst)

effectieve_strijklengte = gekozen_antwoord['f']
print(round(effectieve_strijklengte, decimalen))  # [1]

windsnelheid = gekozen_antwoord['w']
print(windsnelheid)  # [2]

# Vraag 2 Wat wordt volgens figuur 9.9 uit Nortier de golfhoogte H0 in m.
golfhoogte = gekozen_antwoord['H0']
print(golfhoogte)  # [3]

# Vraag 3 Wat wordt volgens figuur 9.9 uit Nortier de golfperiode T in s.
golfperiode = gekozen_antwoord['T']
print(golfperiode)  # [4]

# Vraag 4 Wat wordt volgens figuur 9.9 uit Nortier de golflengte L0 in m.
golflengte = gekozen_antwoord['L0']
print(golflengte)  # [5]

# Vraag 5 Hoe lang met de stormwind gewaaid hebben om de golven te laten ontstaan (uur)
duur = gekozen_antwoord['duur']
print(duur)  # [6]

# Vraag 6 Wat wordt de snelheid van de windgolf in m/s.
snelheid = golflengte / golfperiode
print(round(snelheid, decimalen))  # [7]

# Vraag 7 Wat moet de minimale diepte zijn om te kunnen spreken van een diepwatergolf?
mindiepte = (golflengte * 0.5)
print(round(mindiepte, 1))  # [8]

#")
