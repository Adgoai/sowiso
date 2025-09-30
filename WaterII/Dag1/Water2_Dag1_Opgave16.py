from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Formule van manning
# Bereken de het energieverhang Gebruik 5 decimalen

#sw_Python("
#versie 4-7-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 5
print(decimalen) # [0]

n = kies_getal_stap(0.01, 0.05, 0.01, 2)
print(n) # [1]

R = kies_getal_stap(0.5, 2.5, 0.5, 1)
print(R) # [2]

v = kies_getal_stap(0.5, 2.1, 0.1, 2)
print(v) # [3]

S = (v * n / R**(2/3))**(2)
print(round(S, decimalen)) # [4]

#")