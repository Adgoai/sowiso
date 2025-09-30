import math
from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $AquaCycle_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.

#sw_Python("
#versie 24-04-2024
#$AquaCycle_lib

F = kies_getal_stap(8.0, 12.1, 0.1)  # ton/h (F)
W_F_KNO3 = kies_getal_stap(0.15, 0.55, 0.01)  # -
W_F_water = round(1 - W_F_KNO3, 2)  # -

# Vapor (V)
W_V_wat = 1  # -
W_V_KNO3 = 0.0  # -

P = kies_getal_stap(0.5, 1.1, 0.1)  # ton/h (P)
W_P_KNO3 = kies_getal_stap(0.4, 1.2, 0.01)  # -
W_P_wat = round(1 - W_P_KNO3, 2)  # -

# Rest (R)
W_R_KNO3 = kies_getal_stap(0.1, 0.3, 0.01)  # -
W_R_wat = round(1 - W_R_KNO3, 2)  # -

# question 1 total balance sheet and partial balance sheet  step 2b
# F = V + P + R
# Partial balance: W_F_KNO3 * F = W_V_KNO3 * V + W_P_KNO3 * P + W_R_KNO3 * R

# onbekenden
Vo = 0
Ro = 0

# F = Vo + P + Ro
# W_F_KNO3 * F = W_V_KNO3 * Vo + W_P_KNO3 * P + W_R_KNO3 * Ro
R = (W_F_KNO3 * F - W_P_KNO3 * P) / W_R_KNO3  # ton/h
V = F - P - R  # ton/h


# C = P + R
KNO3_conc = W_P_KNO3 * P + W_R_KNO3 * R  # ton/h
Water_conc = W_P_wat * P + W_R_wat * R  # ton/h

efficiency = ((W_P_KNO3 * P) / (W_F_KNO3 * F)) * 100  # %

print(round(F, 1)) # [0]
print(round(W_F_KNO3, 2)) # [1]
print(round(W_F_water, 1)) # [2]

print(round(W_V_wat, 1)) # [3]
print(round(W_V_KNO3, 1)) # [4]

print(round(P, 1)) # [5]
print(round(W_P_KNO3, 2)) # [6]
print(round(W_P_wat, 2)) # [7]

print(round(W_R_KNO3, 2)) # [8]
print(round(W_R_wat, 1)) # [9]

#answers
print(round(R, 1)) # [10]
print(round(V, 1)) # [11]
print(round(KNO3_conc, 1)) # [12]
print(round(Water_conc, 1)) # [13]
print(round(efficiency, 0)) # [14]

#precentages
print(round(W_F_KNO3 * 100, 1)) # [15]
print(round(W_F_water * 100, 1)) # [16]
print(round(100,0)) # [17]
print(round(W_P_KNO3 * 100, 1)) # [18]
print(round(W_P_wat * 100, 1)) # [19]
print(round(W_R_KNO3 * 100, 1)) # [20]
print(round(W_R_wat * 100, 1)) # [21]

#")