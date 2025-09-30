from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Een rechthoekig kanaal heeft een breedte van 11 m.
# De energiehoogte H (gemeten vanaf de bodem) is 2,4 m.
# We nemen aan dat dit de minimale optredende energiehoogte is.
# Bereken de kritische diepte hc
# Gebruik 2 decimalen en vergeet de eenheid niet.

#sw_Python("
#versie 20-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

bodembreedte = kies_getal_stap(8.0, 12.5, 0.5, 1)
print(bodembreedte)  # [1]

energiehoogte_H = kies_getal_stap(2.0, 3.0, 0.1, 1)
print(energiehoogte_H)  # [2]

# vraag 21 Bereken de kritische diepte hc (m)
hc = (2/3) * energiehoogte_H
print(round(hc, decimalen_2))  # [3]

#vraag 22 Bereken het debiet Q (m3/s)
Debiet = (hc ** 3 * water.g * bodembreedte ** 2) ** (1/2)
print(round(Debiet, decimalen_2))  # [4]



#")