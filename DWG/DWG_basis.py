from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
#

#sw_Python("
#versie 22-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

natte_oppervlak = kies_getal_tussen(1.4, 5.5, decimalen)
print(round(natte_oppervlak, decimalen)) # [1]

stroomsnelheid = kies_getal_stap(0.1, 1.4, 0.1, decimalen)
print(round(stroomsnelheid, decimalen)) # [2]

debiet = natte_oppervlak * stroomsnelheid
print(round(debiet, decimalen)) # [3]

#")
