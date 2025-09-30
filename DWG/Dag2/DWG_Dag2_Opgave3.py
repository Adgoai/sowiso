import random

from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie
# Bereken de dominerende of significante golfhoogte.
# Gebruik 1 decimaal en vergeet de eenheid niet.

#sw_Python("
#versie 7-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 1
print(decimalen) # [0]

# Genereren van een lijst met 12 getallen, elk getal random tussen 2.0 en 10.0
getallen_lijst = [random.uniform(2.0, 10.0) for _ in range(12)]
print(round(getallen_lijst[0], decimalen))  # [1]
print(round(getallen_lijst[1], decimalen))  # [2]
print(round(getallen_lijst[2], decimalen))  # [3]
print(round(getallen_lijst[3], decimalen))  # [4]
print(round(getallen_lijst[4], decimalen))  # [5]
print(round(getallen_lijst[5], decimalen))  # [6]
print(round(getallen_lijst[6], decimalen))  # [7]
print(round(getallen_lijst[7], decimalen))  # [8]
print(round(getallen_lijst[8], decimalen))  # [9]
print(round(getallen_lijst[9], decimalen))  # [10]
print(round(getallen_lijst[10], decimalen))  # [11]
print(round(getallen_lijst[11], decimalen))  # [12]

# Eerst sorteren we de lijst in aflopende volgorde
gesorteerde_lijst = sorted(getallen_lijst, reverse=True)

# Daarna selecteren we de hoogste 4 getallen
hoogste_vier_getallen = gesorteerde_lijst[:4]

# Vervolgens berekenen we het gemiddelde van deze 4 getallen
significanteGolfHoogte = sum(hoogste_vier_getallen) / 4
print(round(significanteGolfHoogte, decimalen))  # [13]

#")
