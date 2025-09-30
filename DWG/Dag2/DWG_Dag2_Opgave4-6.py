from adgo_lib import kies_getal_tussen, kies_getal_stap
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Een oefening in het invullen van tanh, sinh, cosh.
# Wat wordt de waarde voor tanh 3,2?
# Gebruik 2 decimalen en je hoeft geen eenheid in te vullen!!
# Hieronder nogmaals het filmpje over de tanh, sinh, cosh

#sw_Python("
#versie 7-12-2023
#$adgo_lib
#$adgo_DWG_lib



decimalen = 2
print(decimalen) # [0]

tanh = kies_getal_tussen(0.1, 5, decimalen)
print(round(tanh, decimalen))  # [1]
print(round(math.tanh(tanh), decimalen))  # [2]

sinh = kies_getal_tussen(0.1, 2, decimalen)
print(round(sinh, decimalen))  # [3]
print(round(math.sinh(sinh), decimalen))  # [4]

cosh = kies_getal_tussen(0.1, 2, decimalen)
print(round(cosh, decimalen))   # [5]
print(round(math.cosh(cosh), decimalen))  # [6]


#")
