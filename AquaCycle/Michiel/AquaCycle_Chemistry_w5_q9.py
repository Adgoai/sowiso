import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $AquaCycle_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# The 1400 km long river Kura flows 185 km through Turkey, 425 km through Georgia and 790 km through Azerbaijan. The Kura flows out into the Caspian Sea.
# For Azerbaijan the River Kura is the main source for fresh water, while Georgia has enough groundwater for making drinking water.
# When the River Kura flows into Georgia from Turkey, the river is almost unpolluted, but it is heavily polluted when
# it reaches the border of Azerbaijan. This is mainly due to the waste water discharges from the Georgian capital Tblisi and the industrial city Rustavi.

# The Kura has a volumetric flow rate of 120 m3/sec in the summer months, just before the River flows into Tblisi.
# Furthermore, it has a velocity of 0.43 m/sec and a BODu concentration of 12.2 mg/l. The discharge of untreated sewage
# from Tblisi has a volumetric flow rate of 3.5 m3/sec (range between 3.0 and 4.0) and a BODu concentration of 358 mg/l. (Range between 300 and 400).



#sw_Python("
#versie 08-02-2024
#$AquaCycle_lib

decimalen = 2
print(decimalen) # [0]

flow_rate = kies_getal_stap(3,4, 0.1, 1)
print(flow_rate) # [1]

concentration = kies_integer_getal_stap(300,400, 10)
print(concentration) # [2]

# a.	How many people are living in Tblisi when the average water usage is 150 liter per inhabitant per day? Give the
# answer in million of inhabitants with one decimal.
inhabitants = flow_rate * 86400 * 1000 / (150 * 1000000)
print(round(inhabitants, 1)) # [3]


# b.	Calculate the BODu concentration just after the point of discharge (or: calculate L0) in Tblisi. Answer with one decimal.
BODu = (120 * 12.2 + flow_rate * concentration) / (120 + flow_rate)
print(round(BODu, 1)) # [4]


# c.	When will the critical oxygen deficit (tc) occur? Answer with one decimal.
# How many kilometers downstream from Tblisi will the critical oxygen deficit occur? Answer without decimals.
# (Given: k1 = 0.23 dag-1, k2 = 0.50 dag-1, (range between 0.45 and 0.55) D0 = 0.85 mg/l and the
# saturation concentration of oxygen is 9.20 mg/l at the existing temperature.

k2 = kies_getal_stap(0.45,0.55, 0.01, 2)
print(k2) # [5]

tc = (1 / (k2 - 0.23)) * math.log((k2/0.23)*(1 - 0.85 * (k2-0.23)/(0.23 * BODu)))
print(round(tc, 1)) # [6]

x = 0.43 * 86400 * tc / 1000
print(round(x, 0)) # [7]


# d.	What will the critical oxygen deficit (Dc) be?
# (Fill the tc in the oxygen deficit formula.) What will the oxygen concentration be at that point? Answers with one decimal.

Dc = (0.23 * BODu / (k2-0.23)) * (math.exp(-0.23 * tc) - math.exp(-k2 * tc))
print(round(Dc, 1)) #[8]

O2 = 9.20 - Dc
print(round(O2, 1)) #[9]

# e.	Calculate the BODu concentration in the river the Kura 130 km downstream of Tblisi just before the Kura flows
# into the city Rustavi. Answer with one decimal.

Ct = BODu * math.exp(-0.23 * tc)
print(round(Ct, 1)) #[10]

#")