from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Ter plaatse van een dijk bedraagt het het verschil in drukhoogte (verval grondwater) 2,7 m. Als creepfactor volgens Bligh mag aangehouden worden 6.
# Bereken de kritieke kwelweglengte.
# Gebruik 1 decimaal en vergeet de eenheid niet.


#sw_Python("
#versie 15-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

verval = kies_getal_stap(2, 4, 0.1, 1)
print(verval)
creepfactor = kies_integer_getal_stap(4,18,1)
print(creepfactor) # [1]

Lkritiek = creepfactor * verval
print(round(Lkritiek, 2)) # [2]

#")
