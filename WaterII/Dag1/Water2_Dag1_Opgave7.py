from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Formule van manning
# Bereken de stroomsnelheid. Gebruik 2 decimalen en de eenheid is m/s

#sw_Python("
#versie 6-6-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

n = kies_getal_stap(0.01, 0.05, 0.01, 2)
print(n) # [1]

R = kies_getal_stap(0.5, 2.5, 0.5, 1)
print(R) # [2]

S = kies_getal_stap(0.0001, 0.001, 0.0001, 4)
print(S) # [3]

V = (1 / n) * R**(2/3) * S**(1/2)
print(round(V, decimalen)) # [4]

#")