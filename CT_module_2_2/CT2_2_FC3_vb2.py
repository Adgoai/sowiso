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

hoogte = kies_getal_stap(2.50, 4.0, 0.1, decimalen)
print(hoogte) # [1]

diepte = hoogte - kies_getal_stap(0.2, 0.5, 0.1, decimalen)
print(round(diepte, decimalen)) # [2]

dichtheid = water.sgzoet
print(dichtheid) # [3]

breedte = 1.00
print(round(breedte, decimalen)) # [4]

klep = kies_getal_stap(0.6, 1.1, 0.1, decimalen)
print(klep) # [5]

plaats = kies_getal_stap(0.5, 0.8, 0.1, decimalen)
print(plaats) # [6]

# Vraag bereken de totale kracht tegen de klep

p_boven = (diepte - klep - plaats) * dichtheid * water.g
p_onder = (diepte - plaats) * dichtheid * water.g
p_gem = (p_boven + p_onder) / 2
kracht = p_gem * klep * klep
print(round(kracht, decimalen)) # [7]

#")