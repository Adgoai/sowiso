from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# In een wand tussen twee grote wateroppervlakten zit een klein gaatje. Het gaatje bevindt zich op 7,6 m (y) beneden het linker wateroppervlak.
# Het waterstandsverschil tussen beide wateroppervlakten bedraagt 1,1 m (h).
# Aan beide zijden betreft het zoetwater.
# Stap 1 : Wat is de plaatshoogte (z) voor P1 en P2.
# Gebruik 2 decimalen, eenheid = m

#sw_Python("
#versie 12-11-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen)  # [0]

y1 = kies_getal_stap(2, 10, 0.2, 1)
print(y1)  # [1]

h = kies_getal_stap(0.3, 1.0, 0.1, 1)
print(h)  # [2]

#12 Wat is de plaDag2_atshoogte (z) voor P1 en P2.
z = 0.0
print(round(z, decimalen))  # [3]

#13 Bereken de drukhoogte in P1. Gebruik 2 decimalen, eenheid = m
drukhoogte_P1 = y1
print(round(drukhoogte_P1, decimalen))  # [4]

#14 Bereken de drukhoogte in P2. Gebruik 2 decimalen, eenheid = m
drukhoogte_P2 = y1 - h
print(round(drukhoogte_P2, decimalen))  # [5]

#15 Bereken de snelheidshoogte in P1. Gebruik 2 decimalen, eenheid = m
snelheidshoogte_P1 = 0.0
print(round(snelheidshoogte_P1, decimalen))  # [6]

#16 Bereken het energieverlies tussen P1 en P2. Gebruik 2 decimalen, eenheid = m
energieverlies = 0.0
print(round(energieverlies, decimalen))  # [7]

#17 Bereken de snelheidshoogte tpv P2. Gebruik 2 decimalen, eenheid = m
snelheidshoogte_P2 = h
print(round(snelheidshoogte_P2, decimalen))  # [8]

#18 Bereken de snelheid in P2. Gebruik 2 decimalen, eenheid = m/s
v2 = (snelheidshoogte_P2 * 2 * water.g)**(1/2)
print(round(v2, decimalen))  # [9]

#")