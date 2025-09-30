from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# De breedte (w) van deze koker is 9,6 m, de hoogte (h) is 8,2 m.
# Bereken het oppervlakte in m2
# Gebruik 2 decimalen en vergeet niet de eenheid m2 te vermelden

#sw_Python("
#versie 6-9-2023
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

#Vraag 3 Berekenen het oppervlakte in m2
oppervlakte = breedte * hoogte
print(round(oppervlakte, decimalen))  # [5]

# Vraag 4 Bereken de natte omtrek in m
omtrek = 2 * (breedte + hoogte)
print(round(omtrek, decimalen))  # [6]

# Vraag 5 Bereken de hydraulische straal in m
hydraulische_straal = oppervlakte / omtrek
print(round(hydraulische_straal, decimalen))  # [7]

# Vraag 6 Bereken de Reynoldsgetal
Reynoldsgetal = stroomsnelheid * hydraulische_straal / kin_visco
print(round(Reynoldsgetal, 0))  # [8]

#")