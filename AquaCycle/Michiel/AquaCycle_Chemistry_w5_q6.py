import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# A WWTP in London in Canada (Canada also has a city London) is treating the waste water of 1 million inhabitants.
# The waste water flows after the grid and the primary sedimentation tanks to the aeration tanks, from which it flows to the secondary sedimentation tanks. The sludge is being recycled to the aeration tanks.
# The WWTP has the following data:
# Q	= 1.75 m3/sec			Xi	≈ 0
# Qr	= 1.00 m3/sec			X	= 4.0 kg/m3
# VS	= 100,000 m3			Xe	= 0.03 kg/m3
# BODinf	= 250 mg/L			Xr	= 10.0 kg/m3
# BOD loading = 1.2 kg/m3·day 	Purification efficiency = 98%

#sw_Python("
#versie 08-02-2024
#$AquaCycle_lib

decimalen = 2
print(decimalen) # [0]

inhabitants = 1000000
print(inhabitants) # [1]

Q = kies_getal_stap(1.5, 2.0, 0.1, 2)
print(round(Q, decimalen)) # [2]

Qr = 0.6 * Q
print(round(Qr, decimalen)) # [3]

VS = kies_integer_getal_stap(80000, 120000, 10000)
print(VS) # [4]

BODinf = kies_integer_getal_stap(200, 300, 10)
print(BODinf) # [5]

BOD_loading = kies_getal_stap(1.0, 1.5, 0.1, 1)
print(BOD_loading) # [6]

Xi = 0
print(Xi) # [7]

X = 4
print(X) # [8]

Xe = 0.03
print(Xe) # [9]

Xr = 10
print(Xr) # [10]

Purification_efficiency = kies_getal_stap(0.95, 0.99, 0.01, 2)
print(Purification_efficiency) # [11]


# a.	Calculate the volume of the aeration tank with the help of the incoming volumetric flow rate, the BODinf and the BOD loading.
BODinf_kg = BODinf / 1000
Q = Q * 86400
VA = BODinf_kg * Q / BOD_loading
print(round(VA, 0)) # [12]

# b.	Set up the mass balance for the sludge around the aeration tank and calculate the sludge growth (i.e.: rX) in kg/m3·day.
Qr = Qr * 86400
rX = -(Q * Xi + Qr * Xr - (Q + Qr ) * X) / VA
print(round(rX, 2)) # [13]

# c.	Set up the mass balance for the sludge around the sedimentation tanks and calculate the volumetric flow rate of the waste sludge(i.e.: Qw).
# 	(Q + Qr) * X - (Q - Qw ) * Xe - Qw * Xr -Qr * Xr = 0
Qw = (Q * X + Qr * X - Q * Xe -Qr * Xr) / (Xr - Xe)
print(round(Qw, 0)) # [14]

# d.	Calculate the load of the waste sludge (in kg/day) that is being produced and find out if this is more or less equal
# to the sludge production in the aeration tanks (rX · VA). What is causing the minor difference?
load_waste_sludge = Qw * Xr
print(round(load_waste_sludge, 0)) # [15]
sludge_production = rX * VA
print(round(sludge_production, 0)) # [16]

# e.	Calculate the water retention time (θ) in hours and the sludge age (θX) in days.
retention_time = (VA + VS) / Q
print(round(retention_time, 2)) # [17]
sludge_age = (VA + VS) * X /(Qw * Xr + (Q - Qw) * Xe)
print(round(sludge_age, 2)) # [18]

#")