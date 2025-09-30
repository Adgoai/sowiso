from adgo_lib import kies_getal_tussen, kies_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Op basis van figuur 9.12 uit Nortier ga je golfhoogte en golflengte bij afnemende diepte bepalen.
# De gegevens van de diepwatergolf zijn H0= m, L0=  m en T= s.
# De waterdiepte neemt af naar  m
#
# Gebruik 2 decimalen , een eenheid is niet nodig. Gebruik het "juiste antwoord" voor de vervolgvragen

#sw_Python("
#versie 24-1-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

antwoorden_lijst = [
    {'Set': 1, 'H0': 0.4, 'T': 2.2, 'L0': 8, 'h': 1, 'p1': 0.92, 'p2': 0.75, 'helling': 20, 'p4': 1.41, 'p5': 1.15},
    {'Set': 2, 'H0': 0.7, 'T': 2.8, 'L0': 12, 'h': 1.2, 'p1': 0.93, 'p2': 0.71, 'helling': 50, 'p4': 1.49, 'p5': 1.14},
    {'Set': 3, 'H0': 1.4, 'T': 3.9, 'L0': 24, 'h': 2, 'p1': 0.96, 'p2': 0.65, 'helling': 10, 'p4': 1.32, 'p5': 1.15},
    {'Set': 4, 'H0': 2.2, 'T': 5, 'L0': 39, 'h': 3.6, 'p1': 0.94, 'p2': 0.68, 'helling': 50, 'p4': 1.49, 'p5': 1.14},
    {'Set': 5, 'H0': 2.1, 'T': 5.2, 'L0': 42, 'h': 3.7, 'p1': 0.94, 'p2': 0.68, 'helling': 20, 'p4': 1.41, 'p5': 1.15},
    {'Set': 6, 'H0': 2.8, 'T': 5.8, 'L0': 52, 'h': 4, 'p1': 0.96, 'p2': 0.65, 'helling': 10, 'p4': 1.30, 'p5': 1.20},
    {'Set': 7, 'H0': 4.5, 'T': 7.4, 'L0': 85, 'h': 6.2, 'p1': 0.97, 'p2': 0.61, 'helling': 10, 'p4': 1.30, 'p5': 1.20},
    {'Set': 8, 'H0': 6, 'T': 9, 'L0': 126, 'h': 9.2, 'p1': 0.97, 'p2': 0.61, 'helling': 20, 'p4': 1.41, 'p5': 1.15},
    {'Set': 9, 'H0': 9.9, 'T': 12, 'L0': 225, 'h': 13.5, 'p1': 0.99, 'p2': 0.57, 'helling': 10, 'p4': 1.29, 'p5': 1.29},
    {'Set': 10, 'H0': 7.3, 'T': 11, 'L0': 189, 'h': 13.21, 'p1': 0.97, 'p2': 0.61, 'helling': 50, 'p4': 1.52, 'p5': 1.10},
]

gekozen_antwoord = random.choice(antwoorden_lijst)

H0 = gekozen_antwoord['H0']
print(H0) # [1]

L0 = gekozen_antwoord['L0']
print(L0) # [2]

T = gekozen_antwoord['T']
print(T) # [3]

waterdiepte = gekozen_antwoord['h']
print(waterdiepte) # [4]

# vraag 8 Wat is volgens de grafiek de waarde voor H/H0?
factor_H = gekozen_antwoord['p1']
print(factor_H) # [5]

# vraag9 Wat wordt vervolgens de waarde voor H bij de afgenomen waterdiepte? (m)
H = H0 * factor_H
print(round(H, decimalen)) # [6]

# vraag 10 Wat is de waarde voor L/L0?
factor_L = gekozen_antwoord['p2']
print(factor_L) # [7]

# vraag 11 Wat wordt vervolgens de waarde voor L bij de afgenomen waterdiepte? (m)
L = L0 * factor_L
print(round(L, decimalen)) # [8]

# VRAAG 12 IS GEEN PYTHON

hellingBodem = gekozen_antwoord['helling']
print(hellingBodem) # [9] 1:...

# vraag 13 De bodem heeft een helling 1 : 50. Bepaal op basis van figuur 9.14b de waterdiepte hb waarbij de golf zal breken.(m)
hb = H0 * gekozen_antwoord['p4']
print(round(hb, decimalen)) # [10]

# vraag 14 Bepaal de golfhoogte Hb bij waarbij de golf breekt. (m)
Hb = H0 * gekozen_antwoord['p5']
print(round(Hb, decimalen)) # [11]

# vraag 15 Bereken de golfbrekingsparameter
golfbrekingsparameter = (1 / hellingBodem) / math.sqrt(Hb / L0)
print(round(golfbrekingsparameter, decimalen)) # [12]

#")
