import numpy as np
from adgo_lib import kies_getal_stap, kies_integer_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Waterdiepte bij B (y1) = 1,2 m. Waterdiepte bij A tov B (y2) = 3,5 m. Lengte van de klep (Tussen A en B)  = 7,8 m.  Breedte van de klep is 2,4 m.
# Bedoeling is om de kracht door het zoetwater op de klep te berekenen. Je gaat dit in aantal stappen doen
# Gebruik 0 decimalen, bij vraag  6 2 decimalen

#sw_Python("
#versie 12-11-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 0
print(decimalen)  # [0]

decimalen_vraag6 = 2
print(decimalen_vraag6)  # [1]

y1 = kies_getal_stap(0.5, 1, 0.1, 1)
print(y1)  # [2]

y2 = kies_getal_stap(1, 3, 0.1, 1)
print(y2)  # [3]

hoek = kies_integer_getal_stap(10, 40, 5)
# print(hoek)
lengte_klep = y2 / np.sin(np.deg2rad(hoek))
print(round(lengte_klep,2))  # [4]

breedte_klep = kies_getal_stap(1, 3, 0.1, 1)
print(breedte_klep)  # [5]

# Vraag 3 Bereken de waterdruk in B. Gebruik 0 decimalen, eenheid = Pa = N/m2
waterdrukB = y1 * water.sgzoet * water.g
print(round(waterdrukB, decimalen))  # [6]

# Vraag 4 Bereken de waterdruk in A. Gebruik 0 decimalen, eenheid = Pa = N/m2
waterdrukA = y2 * water.sgzoet * water.g  # Pa = N/m2
print(round(waterdrukA, decimalen))  # [7]

# Vraag 5 Bereken de gemiddelde waterdruk op de klep. Gebruik 2 decimalen, eenheid = Pa = N/m2
waterdruk_gemiddeld = (waterdrukB + waterdrukA) / 2 # Pa = N/m2
print(round(waterdruk_gemiddeld, decimalen))  # [8]

# Vraag 6 Bereken het oppervlakte van de klep. Gebruik 2 decimalen, eenheid = m2
oppervlak_klep = lengte_klep * breedte_klep # m2
print(round(oppervlak_klep, decimalen_vraag6))  # [9]

# Vraag 7 Bereken de kracht op de klep. Gebruik 0 decimalen, eenheid = N
kracht = waterdruk_gemiddeld * oppervlak_klep # N
print(round(kracht, decimalen))  # [10]

#")