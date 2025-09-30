from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#Een keerwand heeft de volgende afmetingen

#sw_Python("
#versie 26-6-2025
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

afstand_a = kies_getal_stap(1, 2,    0.1, decimalen)
print(afstand_a) # [1]

afstand_b = kies_getal_stap(1, 2,    0.1, decimalen)
print(round(afstand_b, decimalen)) # [2]

afstand_c = kies_getal_stap(0.2, 0.5,    0.1, decimalen)
print(round(afstand_c, decimalen)) # [3]

afstand_d = kies_getal_stap(20, 30,    1, decimalen)
print(round(afstand_d, decimalen)) # [4]

# R zomer

A_z = afstand_a * afstand_b
print(round(A_z, decimalen)) # [5]

O_z = afstand_a + 2 * afstand_b
print(round(O_z, decimalen)) # [6]

R_zomer = A_z / O_z
print(round(R_zomer, decimalen)) # [7]

# R winter

A_w = A_z + afstand_c * (afstand_d + afstand_a)
print(round(A_w, decimalen))  # [8]

O_w = O_z + 2 * afstand_c + afstand_d
print(round(O_w, decimalen)) # [9]

R_w = A_w / O_w
print(round(R_w, decimalen)) # [10]

#")