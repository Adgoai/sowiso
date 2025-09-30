from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Een grote tank met zoetwater heeft op een afstand van 4,93 m beneden de waterspiegel een gaatje.
# Bereken de stroomsnelheid waarmee het water door het gaatje stroomt
#
# Gebruik 2 decimalen en vergeet de eenheid niet.

#sw_Python("
#versie 6-96-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen)  # [0]

afstand_x = kies_getal_stap(1, 5, 0.2, 1)
print(afstand_x)  # [1]

#Bereken de stroomsnelheid waarmee het water door het gaatje stroomt. Gebruik 2 decimalen, eenheid = m/s. Gebruik Torricelli
v = (2 * water.g * afstand_x)**(1/2)
print(round(v, decimalen))  # [2]

#")