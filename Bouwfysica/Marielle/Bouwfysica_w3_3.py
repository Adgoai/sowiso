import math

from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 30-3-2024
#$adgo_lib
#$adgo_bouwfysica_lib

Rc = 4.7 # m²K/W
print(Rc) # [0]

# Vraag wat is de lambda van vlas
lambda_vlas = 0.038 # W/mK
print(lambda_vlas) # [1]

# Vraag 6 Hoe dik moet een laag vlas zijn om aan deze eis te voldoen? Geef je antwoord in mm en rond af op een heel tiental.
dikte_vlas = Rc * lambda_vlas * 1000 # mm
dikte_vlas = math.ceil(dikte_vlas / 10.0) * 10
print(dikte_vlas) # [2]

#")
