import math

from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 30-3-2024
#$adgo_lib
#$adgo_bouwfysica_lib

# Q_{transmissie}=a\bullet A\bullet U\bullet (T_i-T_e)\bullet tijd/1000

opp_wand = kies_integer_getal_stap(15,25,1) # m²
print(opp_wand) # [0]

opp_raam = kies_getal_stap(1.5,3,0.1,1) # m²
print(opp_raam) # [1]

U_raam = 1.0 # W/m²K
print(U_raam) # [2]

R_gevel = 4.7 # m²K/W
print(R_gevel) # [3]

# Vraag 9Hoe verhouden het warmteverlies door het raam en het gesloten deel van de gevel zich ongeveer tot elkaar?

AU_raam = opp_raam * U_raam
AU_gevel = opp_wand / R_gevel

verhouding = AU_raam / AU_gevel

# Bereken de omgekeerde verhouding
omgekeerde_verhouding = 1 / verhouding

print(round(omgekeerde_verhouding, 2)) # [4]

#")
