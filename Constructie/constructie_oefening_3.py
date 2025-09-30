from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# sw_Python("
# versie 17-1-2023
# $adgo_lib
# $adgo_constructie_lib

decimalen = 2
print(decimalen)  # [0]

lengte_a = kies_getal_stap(1, 5, 0.1, 1)
print(round(lengte_a, decimalen))  # [1]

lengte_b = lengte_a + kies_getal_stap(1, 3, 0.1, 1)
print(round(lengte_b, decimalen))  # [1]

lengte = lengte_a + lengte_b
print(round(lengte, decimalen))  # [1]

q_last = kies_getal_stap(1, 10, 0.1, 1)
print(round(q_last, decimalen))  # [2]

F_last = kies_getal_stap(1, 10, 0.1, 1)
print(round(F_last, decimalen))  # [2]

reactie_a = (1 / 2) * q_last * lengte + F_last * lengte_b / lengte
print(round(reactie_a, decimalen))  # [3]

reactie_b = (1 / 2) * q_last * lengte + F_last * lengte_a / lengte
print(round(reactie_b, decimalen))  # [3]
# ")
