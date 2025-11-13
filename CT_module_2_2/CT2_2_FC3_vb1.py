from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Bereken de totale kracht (de resultante) tegen de wand
# (Waarbij kracht ‘F’= (gemiddelde) spanning x oppervlakte)


#sw_Python("
#versie 26-6-2025
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

hoogte = kies_getal_stap(2.0, 3.6, 0.1, decimalen)
print(hoogte) # [1]

diepte = hoogte - kies_getal_stap(0.2, 0.5, 0.1, decimalen)
print(round(diepte, decimalen)) # [2]

dichtheid = water.sgzoet
print(dichtheid) # [3]

breedte = 1.00
print(round(breedte, decimalen)) # [4]

# Vraag bereken de totale kracht tegen de wand

kracht = 0.5 * (diepte**2) * breedte * dichtheid * water.g
print(round(kracht, decimalen)) # [5]


#")