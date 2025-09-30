from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Ombouwen formules  Bereken Diameter

#sw_Python("
#versie 4-7-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 3
print(decimalen) # [0]

A = kies_getal_stap(1, 5, 0.2, 2)
print(A) # [1]

diameter_m = (A / (0.25 * 3.14159)) ** 0.5
print(round(diameter_m,decimalen)) # [2]

#")