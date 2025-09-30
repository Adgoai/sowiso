from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Energieverlies bij een plotselinge vernauwing van een horizontale buis
# Opgave 4.18.5 Nortier, blz 168.
# Niet alle tussenstappen worden gevraagd,
# Als je drie  maal een fout antwoord geeft, dan komt er een video met uitleg. In dit geval bij vraag 2
# Een horizontale buis met een inwendige diameter van 610 mm wordt achtereenvolgens vernauwd tot een diameter van 305 mm en 152,5 mm.
# Vernauwingen zijn abrupt, afvoer is 56,67 l/s. Het is zoetwater.


#sw_Python("
#versie 10-01-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 3
print(decimalen) # [0]

xi_lijst = [
   # {'D1D2': 4.0, 'xi': 0.45},
   # {'D1D2': 3.5, 'xi': 0.43},
   # {'D1D2': 3.0, 'xi': 0.42},
    {'D1D2': 2.5, 'xi': 0.40},
    {'D1D2': 2.0, 'xi': 0.37},
    {'D1D2': 1.5, 'xi': 0.28},
    {'D1D2': 1.3, 'xi': 0.20},
    {'D1D2': 1.1, 'xi': 0.01}
]

keuze = random.choice(xi_lijst)

D1D2 = keuze['D1D2']

xi = keuze['xi']

diameter2 = kies_integer_getal_stap(300,450,10)
print(diameter2) # [1] (mm)

diameter1 = diameter2 * D1D2
print(round(diameter1,0)) # [2] (mm)

diameter3 = diameter2 / D1D2
print(round(diameter3, 0)) # [3] (mm)

oppervlak2 = 0.25 * math.pi * (diameter2 / 1000) ** 2

stroomsnelheid2 = kies_getal_stap(0.8,1.5, 0.1, 3)

debiet = oppervlak2 * stroomsnelheid2 * 1000
print(round(debiet, 0)) # [4] (l/s)

oppervlak1 = 0.25 * math.pi * (diameter1 / 1000) ** 2
print(round(oppervlak1, decimalen)) # [5] (m2)

print(round(oppervlak2, decimalen)) # [6] (m2)

oppervlak3 = 0.25 * math.pi * (diameter3 / 1000) ** 2
print(round(oppervlak3, decimalen)) # [7] (m2)

stroomsnelheid1 = (debiet / 1000) / oppervlak1
print(round(stroomsnelheid1, decimalen)) # [8] (m/s)

snelheidshoogte1 = (stroomsnelheid1 ** 2) / (2 * water.g)
print(round(snelheidshoogte1, decimalen)) # [9] (m)

print(round(stroomsnelheid2, decimalen)) # [10] (m/s)

snelheidshoogte2 = (stroomsnelheid2 ** 2) / (2 * water.g)
print(round(snelheidshoogte2, decimalen)) # [11] (m)

stroomsnelheid3 = (debiet / 1000) / oppervlak3
print(round(stroomsnelheid3, decimalen)) # [12] (m/s)

snelheidshoogte3 = (stroomsnelheid3 ** 2) / (2 * water.g)
print(round(snelheidshoogte3, decimalen)) # [13] (m)

# vraag 16 Hoe groot is het energieverlies tussen 610 mm en 305 mm (m)?
energieverlies12 = xi * snelheidshoogte2
print(round(energieverlies12, decimalen)) # [14] (m)

# vraag 17 Hoe groot is het energieverlies tussen 305 mm en 152,5 mm (m)?
energieverlies23 = xi * snelheidshoogte3
print(round(energieverlies23, decimalen)) # [15] (m)

# vraag 18 Hoe groot is het drukverschil tussen de buis van 610 en 152,5 mm, als het energieverlies tgv wrijving in de buis van 305 mm, 0,61 m bedraagt? (kPa)
drukverschil_m = snelheidshoogte3 + (0.61 + energieverlies12 + energieverlies23) - snelheidshoogte1
drukverschil_kPa = (1000 * drukverschil_m * water.g) / 1000
print(round(drukverschil_kPa, decimalen)) # [16] (kPa)

#")
