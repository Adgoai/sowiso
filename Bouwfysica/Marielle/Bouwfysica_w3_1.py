import math

from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 30-3-2024
#$adgo_lib
#$adgo_bouwfysica_lib

decimalen = 2
print(decimalen) # [0]

dikte = kies_integer_getal_stap(70, 130, 10)
print(dikte) # [1]

# vraag 1 : Welke waarde voor Lambda moet je aanhouden? W/mK
lambda_kalkzandsteen = 0.90 # W/mK
print(lambda_kalkzandsteen) # [2]

# vraag 2 : Bereken de warmteweerstand R van de isolatie in m²K/W
R_kalkzand = (dikte / 1000) / lambda_kalkzandsteen
print(round(R_kalkzand, decimalen)) # [3]

# vraag 4; Wat ts de lambda van EPS
lambda_EPS = 0.035 # W/mK
print(lambda_EPS) # [4]

# vraag 5; Bereken de warmteweerstand R van de isolatie in m²K/W
R_EPS = (dikte / 1000) / lambda_EPS
print(round(R_EPS, decimalen)) # [5]


#")
