from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import oppervlakte_cirkel

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#Bereken het oppervlakte Gebruik 4 significante cijfers en de eenheid is m2

#sw_Python("
#versie 31-5-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 3
print(decimalen) # [0]

diameter_m = kies_getal_stap(1.25, 5.00, 0.25, 2)
print(diameter_m) # [1]

oppervlak_m2 = oppervlakte_cirkel(diameter_m)
print (round(oppervlak_m2, decimalen)) # [2]

#")
