from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Debiet over stuw of overlaat
# Bereken de energiehoogte H bovenstrooms van de stuw
# Gebruik 2 decimalen en de eenheid is m

#sw_Python("
#versie 4-7-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

afvoercoeff = kies_getal_stap(1.1, 1.9, 0.1, 1)
print(afvoercoeff) # [1]

breedte_m = kies_getal_stap(1.5, 5.0, 0.5, 1)
print(breedte_m) # [2]

debiet_m3s = kies_getal_stap(0.3, 1.0, 0.1, 1)
print(debiet_m3s) # [3]

H_specifiek = (debiet_m3s / (afvoercoeff * breedte_m))**(2/3)
print(round(H_specifiek, decimalen)) # [4]

#")
