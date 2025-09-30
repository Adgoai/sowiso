import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# A WWTP in Oconomowoc, a city in Wisconsin in the USA, is treating the waste water of 30,000 inhabitants.
# The waste water flows after the grid and the primary sedimentation tanks to the aeration tanks, from which it flows to the secondary sedimentation tanks. The sludge is being recycled to the aeration tanks.
# The WWTP has the following data:
# Q	= 15·10^3 m3/dag		    Xi	≈ 0
# Qr	= 17·10^3 m3/dag		X	= 5.0 kg/m3
# VA	= 7500 m3			    Xe	= 0.02 kg/m3
# VS	= 5000 m3			    Xr	= 9.0 kg/m3
# BODinf	= 250 mg/l			Purification efficiency = 98%
# As you can see on the picture, there are two secondary sedimentation tanks, which have a total volume of 5000 m3. The average depth is 4.06 m.


#sw_Python("
#versie 09-02-2024
#$AquaCycle_lib

decimalen = 2
print(decimalen) # [0]

inhabitants = 30000
print(inhabitants) # [1]

Q = kies_integer_getal_stap(12000,18000,1000)
print(Q)# [2]

Qr =0.8 * Q
print(round(Qr,0))# [3]

VA = kies_integer_getal_stap(5000, 10000, 1000)
print(VA) # [4]

VS = kies_integer_getal_stap(3000, 7000, 1000)
print(VS) # [5]

BODinf = kies_integer_getal_stap(200, 300, 10)
print(BODinf) # [6]

Xi = 0
print(Xi) # [7]

X = 5
print(X) # [8]

Xe = 0.02
print(Xe) # [9]

Xr = 9
print(Xr) # [10]

Purification_efficiency = kies_getal_stap(0.95, 0.99, 0.01,2)
print(Purification_efficiency) # [11]

volume_sedimentation_tanks = VS
print(volume_sedimentation_tanks) # [12]

average_depth = kies_getal_stap(3.5, 4.5, 0.1,1)
print(average_depth) # [13]

# question a Set up the mass balance for the sludge around the sedimentation tanks and calculate the volumetric flow rate of the sludge waste (i.e.: Qw).
# 	(Q + Qr) * X - (Q - Qw ) * Xe - Qw * Xr -Qr * Xr = 0
Qw = (Q * X + Qr * X - Q * Xe -Qr * Xr) / (Xr - Xe)
print(round(Qw,0)) # [14]

# question b. Set up the mass balance for the sludge around the aeration tanks and calculate the rate of sludge growth (i.e.: rX) in kg/m3·day.
# 	Q * Xi + Qr * Xr - (Q + Qr ) * X + rx * VA = 0
rX = -(Q * Xi + Qr * Xr - (Q + Qr ) * X) / VA
print(round(rX,2)) # [15]

#question c.	Calculate the load of sludge waste and find out if this is more or less equal to the sludge production
# in the aeration tanks (rX · VA). What is causing the minor difference?
# Load of sludge waste =Q_w X_r
Load_of_sludge_waste = Qw * Xr
print(round(Load_of_sludge_waste,0)) # [16]
# Sludge production =r_X V_A
Sludge_production = rX * VA
print(round(Sludge_production,0)) # [17]

# question d Calculate the diameter of one sedimentation tank.
volume1_tank = volume_sedimentation_tanks / 2

A = volume1_tank / average_depth

diameter = math.sqrt(A / math.pi) * 2
print(round(diameter,0)) # [18]

# question e. Calculate the water retention time (θ) in hours and the sludge age (θX) in days.
retention_time = (VA + VS) / Q
print(round(retention_time,2)) # [19]

sludge_age = (VA + VS) * X /(Qw * Xr + (Q - Qw) * Xe)
print(round(sludge_age,2)) # [20]

# question f.	Calculate with the help of the mass balance for organic matter the substrate removal rate (i.e.: rS) in kg/m3∙day.
# The mass balance for organic matter can be written as follows, if steady state is assumed: QC0 - QC + rSVA = 0

BODinf_kg = BODinf / 1000
BODeff = Xe * BODinf_kg
rS = -(Q * BODinf_kg - Q * BODeff) / VA
print(round(rS,2)) # [21]

#")