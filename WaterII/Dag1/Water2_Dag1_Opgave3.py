from adgo_lib import kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#Als er een neerslag van 8 mm valt op een oppervlakte van 27 ha. Hoeveel m3 water valt er dan?
#Gebruik 0 decimalen en de eenheid is m3

#sw_Python("
#versie 31-5-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 0
print(decimalen) # [0]

neerslag_mm = kies_integer_getal_stap(10, 100, 1)
print(neerslag_mm) # [1]

oppervlak_ha = kies_integer_getal_stap(10, 500, 10)
print(oppervlak_ha) # [2]

volume_m3 = neerslag_mm * oppervlak_ha * 10
print(round(volume_m3, decimalen)) # [3]

#")