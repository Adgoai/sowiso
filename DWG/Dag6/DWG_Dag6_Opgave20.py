from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Opgave 4.18.6 Nortier, blz 169.
# Niet alle tussenstappen worden gevraagd,
# Als je drie  maal een fout antwoord geeft, dan komt er een video met uitleg.
# Bereken het drukverlies dat optreedt in een horizontaal gelegen buisleiding die 140 l/s afvoert, als de diameter plotseling van 0,3 m overgaat op 0,15 m. Het is zoetwater.

#sw_Python("
#versie 28-02-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 4
print(decimalen) # [0]

xi_lijst = [
   # {'D1D2': 4.0, 'xi': 0.45},
   # {'D1D2': 3.5, 'xi': 0.43},
    {'D1D2': 3.0, 'xi': 0.42},
    {'D1D2': 2.5, 'xi': 0.40},
    {'D1D2': 2.0, 'xi': 0.37},
    {'D1D2': 1.5, 'xi': 0.28},
    {'D1D2': 1.3, 'xi': 0.20},
    {'D1D2': 1.1, 'xi': 0.01}
]

keuze = random.choice(xi_lijst)

D1D2 = keuze['D1D2']

xi = keuze['xi']

diameter_rechts = kies_integer_getal_stap(150,300,10)

diameter_links = diameter_rechts * D1D2

oppervlakte_links = 0.25 * math.pi * (diameter_links / 1000) ** 2

oppervlakte_rechts = 0.25 * math.pi * (diameter_rechts / 1000) ** 2

snelheid_rechts = kies_getal_stap(1,2, 0.1, 3)

debiet = oppervlakte_rechts * snelheid_rechts * 1000

snelheid_links = (debiet / 1000) / oppervlakte_links

snelheidshoogte_links = (snelheid_links ** 2) / (2 * water.g)

snelheidshoogte_rechts = (snelheid_rechts ** 2) / (2 * water.g)

energieverlies = xi * snelheidshoogte_rechts

print(round(diameter_links, 0)) # [1] (mm)

print(round(diameter_rechts,0)) # [2] (mm)

print(round(debiet, 0)) # [3] (l/s)

# vraag 20 a Bereken de stroomsnelheden in beide buizen (m/s).
print(round(snelheid_links, decimalen)) # [4] (m/s)
print(round(snelheid_rechts, decimalen)) # [5] (m/s)

# vraag 20 b  Bereken het energieverlies (m).
print(round(energieverlies, decimalen)) # [6] (m)

# vraag 20 c Bereken het drukverschil (kPa).
drukverschil_m = snelheidshoogte_rechts + energieverlies - snelheidshoogte_links
drukververschil_kPa = (1000 * drukverschil_m * water.g) / 1000
print(round(drukververschil_kPa, decimalen)) # [7] (kPa)

#")
