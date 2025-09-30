from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random
import numpy as np


# formule van Bligh
verval = kies_getal_stap(2, 4, 0.1, 1)
print(verval)
creepfactor = kies_integer_getal_stap(4,18,1)
print(creepfactor)

Lkritiek = creepfactor * verval
print(round(Lkritiek, 2))