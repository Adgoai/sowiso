import numpy as np

from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#A PFR (plug flow reactor) has to be designed for a water treatment plant with a minimal
# purification efficiency of 95.0%. The influent concentration (as BOD) is 250 mg/L.
# The volumetric flow rate is 15.0·103 m3/day.
# The biodegradation constant (k1) is 11.98 day-1.
# You may assume that it is a first order reaction.

#sw_Python("
#versie 08-02-2024
#$AquaCycle_lib

decimalen = 2
print(decimalen) # [0]

efficiency = kies_getal_stap(90, 97, 0.1, 1)
print (efficiency) # [1]

influent_concentration = kies_integer_getal_stap(200, 300, 5)
print (influent_concentration) # [2]

volumetric_flow_rate = kies_integer_getal_stap(10, 20, 1)
volumetric_flow_rate *= 1000
print (volumetric_flow_rate) # [3]

k1 = kies_getal_stap(10, 15, 0.1, 2)
print (k1) # [4]

reactor_width = kies_getal_stap(2,3,0.2,1)
print (reactor_width) # [5]

reactor_depth = kies_getal_stap(1,2,0.2,1)
print (reactor_depth) # [6]

tank_depth = kies_getal_stap(7,10,0.2,1)
print (tank_depth) # [7]

#question 1 a.	Calculate first the effluent concentration if the PFR reaches a purification efficiency of %.
Concentration_effluent = influent_concentration * (1 - efficiency / 100)
print (round(Concentration_effluent, 1)) # [8]

#question 1 b.	Calculate also the minimal retention time needed to obtain the desired purification efficiency.
first = np.log(Concentration_effluent / influent_concentration)
time_retention = first / -k1
print (round(time_retention, decimalen)) # [9]

#question 2	Calculate the volume of the PFR needed (m3).
volume_PFR = volumetric_flow_rate * time_retention
print (round(volume_PFR, 0)) # [10]

#question 3 Calculate the length of the PFR and the velocity in the PFR in m/sec, if the width and the depth of the reactor is 2.00 m and 1.50 m, respectively.
area_PFR = reactor_width * reactor_depth
velocity_PFR = volumetric_flow_rate / area_PFR
print(round(velocity_PFR, 0)) # [11] (m/day)
length_PFR = velocity_PFR * time_retention
print (round(length_PFR, 0)) # [12] (m)

#question 4 Calculate the volume of the CMFR which is needed to reach a purification efficiency of 95%.
# (Use the same values for BOD concentration, the volumetric flow rate and the biodegradation constant (k1), which are written above.)
#	Q * C_0 - Q * C - k * C * V=0
#   V = (Q * C_0 - Q * C) / (k * C)
volume_CMFR = (volumetric_flow_rate * influent_concentration - volumetric_flow_rate * Concentration_effluent) / (k1 * Concentration_effluent)
print (round(volume_CMFR, 0)) # [13]

#question 5 Calculate the diameter of the cylindrically shaped CMFR. (m)
# V = d * A
# A = V / d
A = volume_CMFR / tank_depth
# A = pi * r^2
r = (A / np.pi) ** 0.5
diameter_CMFR = r * 2
print (round(diameter_CMFR, 1)) # [14]

#")