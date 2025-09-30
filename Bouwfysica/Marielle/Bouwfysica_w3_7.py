import random
from tkinter.constants import ROUND

from Bouwfysica.Marielle.Bouwfysica_w3_1 import dikte
from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 03-09-2024
#$adgo_lib
#$adgo_bouwfysica_lib


#Voor de warmteweerstand van een constructie is de isolatielaag bepalend; de bijdrage van andere lagen is
# relatief klein en verwaarlozen we in deze opgave. Volgens het Besluit bouwwerken leefomgeving (Bbl)
# moet de Rc van een vloer 3,7 m2K/W bedragen.


Rc = 3.7 # m²K/W

materiaal_lijst = [
    {'materiaal': 'PUR', 'Lambda': 0.025},
    {'materiaal': 'PIR', 'Lambda': 0.024},
    {'materiaal': 'EPS', 'Lambda': 0.038},
    {'materiaal': 'XPS', 'Lambda': 0.035},
    {'materiaal': 'Icynene', 'Lambda': 0.037},
    {'materiaal': 'Steenwol', 'Lambda': 0.036},
    {'materiaal': 'Vlas', 'Lambda': 0.038},
    {'materiaal': 'Katoen isolatie', 'Lambda': 0.038},
    {'materiaal': 'Schapenwol', 'Lambda': 0.038}

]

# Hoe dik (mm) moet een laag PUR/EPS/PIR/XPS/Steenwol/vlas/schapenwol/katoen/Icynene
# zijn om aan deze eis te voldoen?

keuze = random.choice(materiaal_lijst)

Lambda = keuze['Lambda']
materiaal = keuze['materiaal']

dikte_mm = Rc * Lambda * 1000

print(Rc) # [0]
print(materiaal) # [1]
print(Lambda) # [2]
print(round(dikte_mm, 0)) # [3]


#")
