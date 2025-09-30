import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie
# A CMFR (completely mixed flow reactor) is used in a water treatment plant, of which the volume is 1008 m3 .
# The influent concentration (as BOD) is 200 mg/L and the effluent concentration is 20 mg/L. The volumetric flow rate is 720 m3/day.

#sw_Python("
#versie 08-02-2024
#$AquaCycle_lib

decimalen = 2
print(decimalen) # [0]

CMFR_volume = kies_integer_getal_stap(1000, 2000, 10)
print(CMFR_volume) # [1]

CMFR_influent_concentration = kies_integer_getal_stap(150, 250, 10)
print(CMFR_influent_concentration) # [2]

CMFR_effluent_concentration = kies_integer_getal_stap(10, 30, 1)
print(CMFR_effluent_concentration) # [3]

flow_rate = kies_integer_getal_stap(500, 1000, 10)
print(flow_rate) # [4] (m3/day)

# question a.	Calculate the biodegradation constant (k1). You may assume that it is a first order reaction.
# Q*C_0-Q*C-k_1*CV=0

k1 = (flow_rate * CMFR_influent_concentration - flow_rate * CMFR_effluent_concentration) / (CMFR_volume * CMFR_effluent_concentration)
print(round(k1, decimalen)) # [5]

# question b.Calculate the volume which is needed to reach a purification efficiency of 95%.
C = 0.05 * CMFR_influent_concentration
# Q*C_0-Q*C-k_1*CV=0
Volume = (flow_rate * CMFR_influent_concentration - flow_rate * CMFR_effluent_concentration) / (C * CMFR_effluent_concentration)
print(round(Volume, 0)) # [6]

# question c.	Calculate the BOD concentration of the effluent. Show with a calculation if the purification efficiency
# will meet the standard of 95% when this design is chosen.
volume_reactor = CMFR_volume / 2
print(round(volume_reactor, 0)) # [7]

retention_reactor = volume_reactor / flow_rate
print(round(retention_reactor, 2)) # [8]

C1 = CMFR_influent_concentration / (1 + k1 * retention_reactor)
print(round(C1, 1)) # [9]

C2 = C1 / (1 + k1 * retention_reactor)
print(round(C2, 2)) # [10]

Efficency = ((CMFR_influent_concentration - C2) / CMFR_influent_concentration) * 100
print(round(Efficency, 1)) # [11]

# question d 1.Calculate the minimum retention time needed to achieve a purification efficiency of 95%.
# 	ln(C/C_0)=-k_1 * t
retention = math.log(C / CMFR_influent_concentration) / (-k1)
print(round(retention, 3)) # [12]

# question d 2.Calculate also the volume of the PFR.
# V=Q*t
volume = flow_rate * retention
print(round(volume, 0)) # [13]

#")