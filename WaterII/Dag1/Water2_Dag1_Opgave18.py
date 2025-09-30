from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Getal van Reynolds
# Bereken op basis van het getal van Reynolds de stroomsnelheid. Gebruik 3 decimalen en de eenheid is m/s

#sw_Python("
#versie 4-7-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 3
print(decimalen) # [0]

R = kies_getal_stap(0.5, 2.5, 0.1, 1)
print(R) # [1]

Re = kies_getal_stap(20000,50000, 500, 0)
print(Re) # [2]

kinv = 10**(-6)
print(kinv) # [3]

v = Re * kinv / R
print(round(v,decimalen)) # [4]

#")