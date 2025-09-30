import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $Aquacycle_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Questions for water treatment (lesson water quality, wastewater and effluent disposal)

#sw_Python("
#versie 08-02-2024
#$AquaCycle_lib

decimalen = 2
print(decimalen) # [0]


concentration = kies_integer_getal_stap(200,300, 10)
print(concentration) # [1]

# a.	Balance the reaction equation of the biodegradation of C6H14O2N2 without nitrification.
# Multiple choice?

# b.	Calculate the BODu of a water sample containing 250 mg/L C6H14O2N2, without any decimals. Assume that C6H14O2N2 is fully biodegradable, so BODu = ThOD without nitrification. (Range between 200 and 300 mg/L).
BODu = (concentration / 146) * 7 * 32
print (round(BODu, 0)) # [2]

# c. 	Calculate BOD5 with .
BOD5 = BODu * (1 - math.exp(-0.23 * 5))
print(round(BOD5, 0)) # [3]

# d.	Calculate the amount of NH3 formed in mmol/L and answer with two decimals.
NH3 = (concentration / 146) * 2
print(round(NH3, decimalen)) # [4]

# e.	Calculate the amount of oxygen needed for nitrification.
O2_nitrification = NH3 * 2 * 32
print(round(O2_nitrification, 0)) # [5]

#")