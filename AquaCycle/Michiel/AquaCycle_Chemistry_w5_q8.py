import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $AquaCycle_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# A food processing industry is discharging 500 m3 wastewater per day (range between 400 and 600) containing organic
# waste with an average formula of C5H10O4N2 and a concentration of 800 mg/L. (Range between 700 and 900).

#sw_Python("
#versie 08-02-2024
#$AquaCycle_lib

decimalen = 0
print(decimalen) # [0]

flow_rate = kies_integer_getal_stap(400,600, 10)
print(flow_rate) # [1]

concentration = kies_integer_getal_stap(700,900, 10)
print(concentration) # [2]

#a	Balance the reaction equation of the biodegradation of C5H10O4N2 without nitrification.

#b	Calculate the COD. Answer without decimals.
COD = (concentration / 162) * 4 * 32
print(round(COD, 0)) # [3]

#c	Calculate Nkj. Answer without decimals.
Nkj = (concentration / 162) * 2 * 14
print(round(Nkj, 0)) # [4]

#d	Calculate the amount of i.e. (inhabitant equivalents) with i.e.=Q/150 (COD+4.57N_Kj ).
ie = flow_rate / 150 * (COD + 4.57 * Nkj)
print(round(ie, 0)) # [5]

#")