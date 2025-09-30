from adgo_lib import kies_getal_tussen, kies_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 7-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

golflengte = kies_getal_tussen(39, 60, 0)
print(round(golflengte, 0))  # [1]

waterdiepte = kies_getal_tussen(5, 10, decimalen)
print(round(waterdiepte, decimalen))  # [2]

# vraag 13 bereken de voortplantingssnelheid in m/s
voorplantingssnelheid = math.sqrt(water.g * golflengte / (2 * math.pi) * math.tanh(2 * math.pi * waterdiepte / golflengte))
print(round(voorplantingssnelheid, decimalen))  # [3]

# vraag 14 bereken de golfperiode in s
golfperiode = golflengte / voorplantingssnelheid
print(round(golfperiode, decimalen))  # [4]

#")
