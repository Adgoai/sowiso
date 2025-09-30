import math

from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 30-3-2024
#$adgo_lib
#$adgo_bouwfysica_lib

Rc = kies_getal_stap(4.0,8.0,0.1,1) # m²K/W
print(Rc) # [0]

isolatie_dikte = kies_integer_getal_stap(130,180,10) # mm
print(isolatie_dikte) # [1]

# Vraag  Een architect wil een zo dun mogelijke pakket realiseren. Wat moet de λ van een materiaal maximaal zijn om met een isolatielaag van 120 mm een Rc van 4,7 m2K/W te realiseren?

lambda_max = (isolatie_dikte / 1000) / Rc
print(round(lambda_max, 3)) # [2]

#")
