from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water
import random
import numpy as np

# Ga uit van een verhang van 1:750 in een betonnen goot (gemiddeld onafgewerkt beton)
# Ga uit van zoet water met een temperatuur van rond het vriespunt
# a. Bepaal de kinematische viscositeit
# b. Bereken de hydraulische straal ‘R’
# c. Bereken de dikte van het laminaire grenslaagje
# d. Bepaal of de goot hydraulisch ruw of glad is, of eventueel in het overgangsgebied zit
# e. Bepaal de Chézy waarde in de situatie van voorbeeld 1a
# f. Bepaal de gemiddelde stroomsnelheid volgens Chézy




#sw_Python("
#versie 11-11-2025
#$adgo_lib
#$adgo_water_lib

kin_visco = {
    '0 graden': 1.79e-6,
    '20 graden': 1e-6
}

k_waarde = {
    'onafgewerkt beton': 4,
    'waterlopen met begroeiing': 150,
    'zeer glad beton': 0.2,
    'PVC': 0.1,
    'oud, slecht beton': 15,
}

decimalen = 2
print(decimalen) # [0]

# a. Bepaal de kinematische viscositeit
temp_beschrijving = random.choice(list(kin_visco.keys()))
kin_visc = kin_visco[temp_beschrijving]
print(temp_beschrijving) # [1]
print(kin_visc) # [2]

k_waarde_beschrijving = random.choice(list(k_waarde.keys()))
kwaarde = k_waarde[k_waarde_beschrijving]
print(k_waarde_beschrijving) # [3]
print(kwaarde) # [4] (mm)

verhang = kies_integer_getal_stap(500, 2000, 250)
print(verhang) # [5]

afstand_a = kies_getal_stap(1, 2,    0.1, decimalen)
print(afstand_a) # [6]

afstand_b = kies_getal_stap(1, 2,    0.1, decimalen)
print(round(afstand_b, decimalen)) # [7]

# b. Bereken de hydraulische straal ‘R’

A_z = afstand_a * afstand_b

O_z = afstand_a + 2 * afstand_b

R_zomer = A_z / O_z
print(round(R_zomer, decimalen)) # [8]

# c. Bereken de dikte van het laminaire grenslaagje

laagje = (12 * kin_visc) / ((10 * R_zomer * (1 / verhang))**0.5) * 1000
print(round(laagje, decimalen)) # [9] (mm)

# e. Bepaal de Chézy waarde in de situatie van voorbeeld 1a

if kwaarde > 6 * laagje:
    print(1) # [10] hydraulisch ruw
    C_waarde = 18 * np.log10((12 * R_zomer) / (kwaarde / 1000))
    print(round(C_waarde, decimalen))  # [11]
elif laagje > 4 * kwaarde:
    print(2) # [10] hydraulisch glad
    C_waarde = 18 * np.log10((48 * R_zomer) / (laagje / 1000))
    print(round(C_waarde, decimalen))  # [11]
else:
    print(3)  #[10] overgangsgebied
    C_waarde = 18 * np.log10((12 * R_zomer) / ((kwaarde / 1000) + (0.25 * (laagje / 1000))))
    print(round(C_waarde, decimalen))  # [11]

# f. Bepaal de gemiddelde stroomsnelheid volgens Chézy
v_gem = C_waarde * (R_zomer * (1 / verhang))**0.5
print(round(v_gem, decimalen)) # [12]

#")