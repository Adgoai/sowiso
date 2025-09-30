from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Afmetingen goot : Hoogt h is 8,2 m, Breedte (w) is 9,6 m. Stroomsnelheid is {u} m/s
# # Bereken de hydraulische straal (R) Gebruik 2 decimalen en vergeet niet de eenheid m2 te vermelden

#sw_Python("
#versie 13-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen)  # [0]

breedte = kies_getal_stap(4, 10, 0.2, 1)
print(breedte)  # [1]

hoogte = kies_getal_stap(1, 5, 0.2, 1)
print(hoogte)  # [2]

kin_visco = water.kin_visco
print(kin_visco)  # [3]

stroomsnelheid = kies_getal_stap(0.5, 4, 0.1, 1)
print(stroomsnelheid)  # [4]

oppervlakte = breedte * hoogte

omtrek = breedte + 2 * hoogte

# Vraag 11 Bereken de hydraulische straal in m
hydraulische_straal = oppervlakte / omtrek
print(round(hydraulische_straal, decimalen))  # [5]

# Vraag 12 Bereken de Reynoldsgetal
Reynoldsgetal = stroomsnelheid * hydraulische_straal / kin_visco
print(round(Reynoldsgetal, 0))  # [6]

#")