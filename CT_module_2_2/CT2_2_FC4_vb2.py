from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Verval en verhang berekenen

#sw_Python("
#versie 26-6-2025
#$adgo_lib
#$adgo_water_lib

significant = 3
print(significant) # [0]

lengte = kies_getal_stap(1000, 2000, 100, 0)
print(lengte) # [1]

hoogte_beneden = kies_getal_stap(-2.5, -0.5, 0.1, 2)
print(hoogte_beneden) # [2]

hoogte_boven = kies_getal_stap(500, 2000, 5, 0)
print(hoogte_boven) # [3]

verval = hoogte_boven - hoogte_beneden
print(verval) # [4]

verhang_1 = verval / (lengte * 1000)

verhang = float(f'{verhang_1:.{significant}g}')
print(verhang) # [5]

#")