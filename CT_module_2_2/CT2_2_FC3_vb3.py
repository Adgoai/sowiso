from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#Een keerwand heeft de volgende afmetingen

#sw_Python("
#versie 26-6-2025
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

dichtheid_water = water.sgzoet
print(dichtheid_water) # [1]

dichtheid_beton = 2500
print(dichtheid_beton) # [2]

wanddikte = kies_getal_stap(1.0, 1.6, 0.10, decimalen)

breedte_uitw = kies_getal_stap(8.0, 15.5, 0.5, decimalen)
print(breedte_uitw) # [3]

breedte_inw = breedte_uitw - 2 * wanddikte
print(round(breedte_inw, decimalen)) # [4]

hoogte_uitw = kies_getal_stap(5, 8.5, 0.5, decimalen)
print(hoogte_uitw) # [5]

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

diepte = druk_onderzijde / (dichtheid_beton * water.g)  # in m
print(round(diepte, decimalen)) # [10]

rand = hoogte_uitw - diepte
print(round(rand, decimalen)) # [11]

volume_boven_water = rand * breedte_uitw * lengte  # in m3
ballast = volume_boven_water * 1000  # l
print(round(ballast, 0)) # [12]

#")