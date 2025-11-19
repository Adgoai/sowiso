from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water
import numpy as np

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Wat is het gewicht (in kN) van het tunnelelement?
# Hoe hoog drijft het tunnelelement boven de waterlijn, voordat de ballasttanks met water worden gevuld?

#sw_Python("
#versie 19-11-2025
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

dichtheid_water = 1000
print(dichtheid_water) # [1]

dichtheid_beton = 2500
print(dichtheid_beton) # [2]

breedte_uitw = kies_getal_stap(8.0, 15.5, 0.5, decimalen)
print(breedte_uitw) # [3]

hoogte_uitw = kies_getal_stap(5, 8.5, 0.5, decimalen)
print(hoogte_uitw) # [4]

randje = kies_getal_stap(0.2, 0.9, 0.1, decimalen)

h = hoogte_uitw - randje
O = breedte_uitw * h / 2.5
a = 4
b =(2 * breedte_uitw + 2 * hoogte_uitw)
c = O

# bereken x met numpy ax^x - bx + c = 0
x = np.roots([-a, b, -c])
x = min(x[x > 0])
x = round(x, 1)

wanddikte = x

breedte_inw = breedte_uitw - 2 * wanddikte
print(round(breedte_inw, decimalen)) # [5]

hoogte_inw = hoogte_uitw - 2 * wanddikte
print(round(hoogte_inw, decimalen)) # [6]

lengte = kies_getal_stap(40, 90, 10, decimalen)
print(lengte) # [7]

# Wat is het gewicht in KN

opp_m =breedte_uitw * hoogte_uitw - breedte_inw * hoogte_inw
gewicht_beton = opp_m * lengte * water.g * dichtheid_beton / 1000  # in kN
print(round(gewicht_beton, 0)) # [8]

# Hoe hoog steekt de tunnel boven het water uit?

druk_onderzijde = (gewicht_beton * 1000) / (lengte * breedte_uitw)  # in Pa
print(round(druk_onderzijde, decimalen)) # [9]

diepte = druk_onderzijde / (water.sgzoet * water.g)  # in m
print(round(diepte, decimalen)) # [10]

rand = hoogte_uitw - diepte
print(round(rand, decimalen)) # [11]

volume_boven_water = rand * breedte_uitw * lengte  # in m3
ballast = volume_boven_water * 1000  # l
print(round(ballast, 0)) # [12]

#")