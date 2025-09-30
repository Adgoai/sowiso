import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie
# The Eastern Treatment Plant, which is a WWTP, in Melbourne in Australia treats 40% of Melbourne’s sewage, servicing
# approximately 1.2 million people living in the southern and eastern suburbs. The WWTP consists of primary, secondary
# and tertiary treatment steps (Figure 1). The effluent is treated with ozone, UV and chlorine in order to re-use a
# part of the water for irrigation of gardens and in agriculture.
# The waste water flows after the grid and the primary sedimentation tanks to the aeration tanks,
# from which it flows to the secondary sedimentation tanks (clarifiers). The sludge is being recycled to the aeration tanks.
# The WWTP has the following data:
# Q	= 332·10^3 m3/day			Xi	≈ 0
# Qr	= 92·10^3 m3/day		X	= 2.0 kg/m3
# VA	= 122400 m3 			Xr	= 8.0 kg/m3
# VS	= 161200 m3				Xe	= 0.02 kg/m3
# BODinf	= 250 mg/L
# BODeff	= 5.00 mg/L


#sw_Python("
#versie 08-02-2024
#$AquaCycle_lib

decimalen = 2
print(decimalen) # [0]

Q = kies_integer_getal_stap(300000, 400000, 10000)
print(Q) # [1]

Qr = kies_integer_getal_stap(80000, 100000, 10000)
print(Qr) # [2]

VA = kies_integer_getal_stap(100000, 150000, 10000)
print(VA) # [3]

VS = kies_integer_getal_stap(150000, 170000, 10000)
print(VS) # [4]

BODinf = kies_integer_getal_stap(200, 300, 10)
print(BODinf) # [5]

BODeff = kies_getal_stap(3, 8, 0.1, 1)
print(BODeff) # [6]

Xi = 0
print(Xi) # [7]

X = 2
print(X) # [8]

Xr = 8
print(Xr) # [9]

Xe = 0.02
print(Xe) # [10]

# question a 1.	Calculate the BOD loading (in kg/m3·day) in the aeration tank.
# Explain if a low F/M ratio leads to a low or a high purification efficiency.
BODinf_kg = BODinf / 1000
print(round(BODinf_kg,3)) # [11]

BOD_loading = BODinf_kg * Q / VA
print(round(BOD_loading,3)) # [12]

# question a 2.the F/M ratio (sludge loading) (in kg BOD/kg sludge·day) in the aeration tank.

F_M_ratio = BOD_loading / (VA * X)
print(round(F_M_ratio,2)) # [13]

# question b Set up the mass balance for the BOD around the secondary treatment step and calculate the BOD removal rate (i.e.: rS) in kg/m3·day.
# 	Q* C_0-Q* C+r_s * V_A=0
BODeff_kg = BODeff / 1000
r_s = -(Q * (BODinf_kg - BODeff_kg))/VA
print(round(r_s,2)) # [14]

# question c. Set up the mass balance for the sludge around the sedimentation tanks and calculate the volumetric flow rate of the waste sludge (i.e.: Qw).
# 	(Q + Qr) * X - (Q - Qw ) * Xe - Qw * Xr -Qr * Xr = 0
Qw = (Q * X + Qr * X - Q * Xe -Qr * Xr) / (Xr - Xe)
print(round(Qw,0)) # [15]

# question d. 1	Calculate the water retention time (θ) in hours and the sludge age (θX) in days.
retention_time = (VA + VS) / Q
print(round(retention_time,2)) # [16]

# question d. 2	and the sludge age (θX) in days.
sludge_age = (VA + VS) * X /(Qw * Xr + (Q - Qw) * Xe)
print(round(sludge_age,2)) # [17]

#")