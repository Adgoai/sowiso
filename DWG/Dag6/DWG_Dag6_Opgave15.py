from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Opgave 4.18.4 Nortier, blz 168.
# Niet alle tussenstappen worden gevraagd,
# Als je drie  maal een fout antwoord geeft, dan komt er een video met uitleg.
#
# Bereken het drukverschil in een horizontale leiding bij een plotselinge verwijding van de
# leiding diameter van 0,15 m naar 0,30 m, als de leiding 140 l/s afvoert. Het is zoetwater.


#sw_Python("
#versie 28-2-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 4
print(decimalen) # [0]

diameter_links = kies_integer_getal_stap(150,300,10)
print(diameter_links) # [1] (mm)

diameter_rechts = diameter_links * kies_getal_stap(1.3,1.8,0.1,1)
print(diameter_rechts) # [2] (mm)

oppervlakte_links = 0.25 * math.pi * (diameter_links / 1000) ** 2

stroomsnelheid_links = kies_getal_stap(0.9,2,0.1,1)

debiet = stroomsnelheid_links * oppervlakte_links * 1000
print(round(debiet,0)) # [3] (l/s)

oppervlakte_rechts = 0.25 * math.pi * (diameter_rechts / 1000) ** 2

snelheidshoogte_links = (stroomsnelheid_links ** 2) / (2 * water.g)

stroomsnelheid_rechts = (debiet / 1000) / oppervlakte_rechts

energieverlies = (stroomsnelheid_links - stroomsnelheid_rechts) ** 2 / (2 * water.g)

snelheidshoogte_rechts = (stroomsnelheid_rechts ** 2) / (2 * water.g)

# vraag 15a Bereken de snelheidshoogte bovenstrooms (m).
print(round(snelheidshoogte_links, decimalen)) # [4] (m)

# vraag 15b Bereken de snelheidshoogte benedenstrooms (m).
print(round(snelheidshoogte_rechts, decimalen)) # [5] (m)

# vraag 15c Bereken het energieverlies (m).
print(round(energieverlies, decimalen)) # [6] (m)

# vraag 15d Bereken het drukverschil (kPa).
drukverschil_m = snelheidshoogte_links - energieverlies - snelheidshoogte_rechts
drukververschil_kPa = (1000 * drukverschil_m * water.g) / 1000
print(round(drukververschil_kPa, decimalen)) # [7] (kPa)

#")
