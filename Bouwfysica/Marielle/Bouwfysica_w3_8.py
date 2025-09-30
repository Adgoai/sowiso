import random

from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 03-09-2024
#$adgo_lib
#$adgo_bouwfysica_lib

# Van een bepaalde vloer is de Rc waarde 3,7 m2K/W (variatie in Rc: 4,7/8,0/10,0).
# Wat is de U-waarde voor deze vloer als deze rechtstreeks op de grond ligt/boven een kruipruimte ligt?


Rc_lijst = [
    {'Rc': 3.7},
    {'Rc': 4.7},
    {'Rc': 8.0},
    {'Rc': 10.0}
]

keuze = random.choice(Rc_lijst)
Rc = keuze['Rc']

Rsi = 0.17 # m²K/W

Rse_grond = 0 # m²K/W
Rse_kruipruimte = 0.17 # m²K/W

# U-waarde voor vloer op de grond
Rt_g = Rc + Rsi + Rse_grond
U_grond = 1 / Rt_g

# U-waarde voor vloer boven een kruipruimte
Rt_k = Rc + Rsi + Rse_kruipruimte
U_kruipruimte = 1 / Rt_k

print(Rc) # [0]
print(Rsi) # [1]
print(Rse_grond) # [2]
print(Rse_kruipruimte) # [3]
print(round(U_grond, 2)) # [4]
print(round(U_kruipruimte, 2)) # [5]

#")
