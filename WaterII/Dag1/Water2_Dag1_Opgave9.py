import numpy as np
from adgo_lib import kies_getal_stap


# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Coefficient van chezy
# Bereken de coëfficiënt van Chezy  C voor een hydraulisch ruwe situatie. Gebruik 2 decimalen en de eenheid is m^(1/2)/s

#sw_Python("
#versie 6-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

R = kies_getal_stap(0.5, 2.5, 0.1, 1)
print(R) # [1]

k = kies_getal_stap(1.0,5.0, 0.1, 1) #k is in mm!
print(k) # [2]

C = 18 * np.log10(12 * R / (k / 1000))
print(round(C,decimalen)) # [3]

#")