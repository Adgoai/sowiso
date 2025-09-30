import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie
#   You are the specialist in water treatment. You are hired by a development organization and you have to design a
#   waste water treatment plant (WWTP) for a refugee camp in Sudan. This WWTP must be built with local materials and
#   should be easy to maintain. A better sanitation will result in fewer diarrhea deaths of children and elderly.
#   Therefore, you will present three designs, of which the calculations (answers on the questions below) will be the
#   arguments for your final choice of one these designs.
#   Design 1 is a CMFR with a volume of 6000 m3, which purifies the waste water with a volumetric flow rate of
#   500 m3/day and an average BOD concentration of 169.2 mg/l. You may assume that the biodegradation constant is 0.23 day-1.


#sw_Python("
#versie 08-02-2024
#$AquaCycle_lib

decimalen = 2
print(decimalen) # [0]

volume_CMFR = kies_integer_getal_stap(5000, 7000, 100)
print (volume_CMFR) # [1]

volumetric_flow_rate = kies_integer_getal_stap(400, 600, 10)
print (volumetric_flow_rate) # [2]

average_BOD_concentration = kies_getal_stap(150, 200, 1, 1)
print (average_BOD_concentration) # [3]

biodegradation_constant = kies_getal_stap(0.2, 0.3, 0.01, 2)
print (biodegradation_constant) # [4]

#question a 1. Calculate the BOD concentration of the effluent. mg/l

retention_days = volume_CMFR / volumetric_flow_rate
print(round(retention_days,0)) # [5]

BOD_concentration = average_BOD_concentration / (1 + biodegradation_constant * retention_days)
print (round(BOD_concentration, 0)) # [6]

#question a 2. Calculate also the purification efficiency.
purification_efficiency = ((average_BOD_concentration - BOD_concentration) / average_BOD_concentration) * 100
print (round(purification_efficiency, 1)) # [7]

#question b 1. Calculate the BOD concentration of the final effluent.
volume_CMFR = volume_CMFR / 3
retention_reactor_days = volume_CMFR / volumetric_flow_rate
print(round(retention_reactor_days, 0)) # [8]

C1 = average_BOD_concentration / (1 + biodegradation_constant * retention_reactor_days)
print (round(C1, 1)) # [9]

C2 = C1 / (1 + biodegradation_constant * retention_reactor_days)
print (round(C2, 1)) # [10]

C3 = C2 / (1 + biodegradation_constant * retention_reactor_days)
print (round(C3, 1)) # [11]

#question b 2. Calculate also the purification efficiency.
purification_efficiency = ((average_BOD_concentration - C3) / average_BOD_concentration) * 100
print (round(purification_efficiency, 1)) # [12]

#question c 1. Calculate the BOD concentration of the effluent
retention_days = volume_CMFR / volumetric_flow_rate
print(round(retention_days, 1)) # [13]

# C = C_0 * math.exp(-k_1 * t)
C = average_BOD_concentration * math.exp(-biodegradation_constant * retention_days)
print((round(C, 1))) # [14]

#question c 2. Calculate also the purification efficiency
purification_efficiency = ((average_BOD_concentration - C) / average_BOD_concentration) * 100
print (round(purification_efficiency, 1)) # [15]

#")