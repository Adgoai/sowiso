from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Formule van Darcy Weisbach
# Bereken de stroomsnelheid
# Gebruik 3 decimalen en de eenheid is m/s

#sw_Python("
#versie 4-7-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 3
print(decimalen) # [0]

#formule van darcy weisbach
Lambda = kies_getal_stap(0.02, 0.08, 0.01, 2)
print(Lambda) # [1]

L = kies_getal_stap(100, 1000, 100, 0)
print(L) # [2]

R = kies_getal_stap(0.5, 2.5, 0.5, 1)
print(R) # [3]

Wrijvingsverlies = kies_getal_stap(0.001, 0.01, 0.001, 3)
print(Wrijvingsverlies) # [4]

g = 10
print(g) # [5]

V = (2 * g * Wrijvingsverlies) / (Lambda * (L / (4 * R)))**0.5
print(round(V, decimalen)) # [6]

#")
