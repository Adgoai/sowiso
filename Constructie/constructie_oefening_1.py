from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 17-1-2023
#$adgo_lib
#$adgo_constructie_lib

decimalen = 2
print(decimalen) # [0]

lengte = kies_getal_stap(3, 8, 0.1,1)
print(round(lengte, decimalen)) # [1]

q_last = kies_getal_stap(1, 10, 0.1, 1)
print(round(q_last, decimalen)) # [2]

moment = (1/8) * q_last * lengte ** 2
print(round(moment, decimalen)) # [3]

#")
