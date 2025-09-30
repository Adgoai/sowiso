import numpy as np

from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# A drinking water treatment plant softens 20∙106 m3 (range between 15∙106  and 30∙106, steps of 1∙106)
# per year by dosing 1.20 mmol/L Ca(OH)2. (range between 1.10 and 1.50, steps of 0.02) Molar mass of Ca(OH)2 is 74 g/mol.

#sw_Python("
#versie 24-04-2024
#$AquaCycle_lib

volume = kies_integer_getal_stap(15,30,1) * 10**6 # m3
print(volume) # [0]

softening = kies_getal_stap(1.10,1.50,0.02, 2) # mmol/L
print(softening) # [1]

# question a. Calculate the amount of Ca(OH)2 needed in kton/year.
CaOH2_added = volume * softening * 74 / 10**9
print(round(CaOH2_added, 2)) # [2]

# question b. How many kton of CaCO3 is produced per year by the softening process. The molar mass of CaCO3 is 100 g/mol.
CaCO3 = volume * softening * 2 * 100 / 10**9 # kton/year
print(round(CaCO3, 2)) # [3]

#")