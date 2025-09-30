from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Getal van Reynolds
# Bereken het getal van Reynolds Re voor een hydraulisch ruwe situatie. Gebruik 0 decimalen en de eenheid is dimensieloos

#sw_Python("
#versie 4-7-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 0
print(decimalen) # [0]

R = kies_getal_stap(0.5, 2.5, 0.1, 1)
print(R) # [1]

v = kies_getal_stap(0.2,4.0, 0.1, 1)
print(v) # [2]

kinv = 10**(-6)
print(kinv) # [3]

Re = v * R / kinv
print(round(Re,decimalen)) # [4]

#")