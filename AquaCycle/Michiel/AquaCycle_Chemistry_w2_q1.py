import numpy as np

from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Given the following water analysis data of a specific groundwater, determine the unknown value of
# the chloride concentration. Use an anion-cation balance to find the missing concentration of chloride.
# Molar mass of calcium, magnesium, sodium, hydrogencarbonate, sulfate and chloride are respectively:
# 40.08, 24.31, 22.99, 61, 96 and 35.45 g/mol.

#sw_Python("
#versie 24-04-2024
#$AquaCycle_lib

Ca2 = kies_integer_getal_stap(110, 150, 2) # mg/L
print(Ca2) # [0]

Mg2 = kies_integer_getal_stap(10, 20, 1) # mg/L
print(Mg2) # [1]

Na = 8 # mg/L
print(Na) # [2]

HCO3 = kies_integer_getal_stap(280,320,2) # mg/L
print(HCO3) # [3]

SO4 = 25 # mg/L
print(SO4) # [4]

# question a. Calculate Cl- concentration in mg/L.
CL = ((Ca2 / 40.08 * 2 + Mg2 / 24.31 * 2 + Na / 22.99) - (HCO3 / 61 + SO4 / 96 * 2)) * 35.45
print(round(CL, 0)) # [5]

# question b. Calculate Hardness in mmol/L.
Hardness = Ca2 / 40.08 + Mg2 / 24.31
print(round(Hardness, 2)) # [6]

# question c. c.	How many mg/L Ca(OH)2
softening = kies_getal_stap(1.30,1.70,0.05, 2) # mmol/L
softening = round(softening, 2)
print(softening) # [7]

CAOH2_added = ((Ca2 / 40.08 + Mg2 / 24.31) - softening) * 74
print(round(CAOH2_added, 0)) # [8]

#")