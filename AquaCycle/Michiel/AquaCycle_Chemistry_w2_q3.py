import numpy as np

from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# To minimize the risk of viruses, disinfection with UV light is done with a dose of 60 mJ/cm2.
# The UV light installed has an intensity of 8.0 mW/cm2 (range between 7.0 and 9.0, steps of 0.1),
# and the transmittance is only 75% (range between 60 and 80, steps of 1) due to absorption by a high concentration
# of other suspended solids

# Surface water has to be disinfected with a volumetric flow rate of 4.0 m3/s (range between 3.0 and 5.0, steps of 0.1)
# has to be disinfected. The irradiation depth (and diameter) of the reactor with many parallel cylindrical tubes is 5 cm.
# The velocity through the tubes is 0.20 m/s (range between 0.10 and 0.30, steps of 0.01) with exposure time of 20 seconds.

#sw_Python("
#versie 24-04-2024
#$AquaCycle_lib

UV_dose = 60 # mJ/cm2
print(UV_dose) # [0]

UV_intensity = kies_getal_stap(7.0,9.0,0.1) # mW/cm2
print(UV_intensity) # [1]

transmittance = kies_integer_getal_stap(60,80,1) # %
print(transmittance) # [2]

flow_rate = kies_getal_stap(3.0,5.0,0.1) # m3/s
print(flow_rate) # [3]

irradiation_depth = 5 # cm
print(irradiation_depth) # [4]

velocity = kies_getal_stap(0.10,0.30,0.01) # m/s
print(velocity) # [5]

exposure_time = 20 # s
print(exposure_time) # [6]

# a.	What must be the minimal contact time?
contact_time = UV_dose/ (UV_intensity * (transmittance/100))
print(round(contact_time, 0)) # [7]

# b.	How many tubes are needed in parallel?
tubes= (flow_rate / velocity) / (np.pi * (irradiation_depth * 0.5 / 100 )**2)
print(round(tubes, 0)) # [8]

# c.	What is the length of one UV tube to have a exposure time of 20 seconds?
length = velocity * exposure_time # m
print(round(length, 1)) # [9]

#d.	What is the total length of all the tubes of the disinfection unit together in km?
total_length = (velocity * exposure_time * (length / velocity) / (irradiation_depth * 0.5 / 100 )**2) / 1000 # km
print(round(total_length, 0)) # [10]



#")