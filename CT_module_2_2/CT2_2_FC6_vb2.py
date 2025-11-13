from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water
import random
import numpy as np

# In de zomer staat het water in deze sloot een meter diep na een forse bui. De sloot is 2,5 kilometer lang en heeft een verval van 2 meter onder een geleidelijk verhang. De sloot is goed onderhouden, heeft geen bochten, en een natuurlijke begroeiing (met name grassoorten)
# a Bereken de hydraulische straal ‘R’
# b Bereken de helling van de energielijn ‘I’
# c Bepaal de ruwheidsfactor ‘n’ volgens Manning
# d Bereken de gemiddelde snelheid ‘v’ volgens Manning


#sw_Python("
#versie 11-11-2025
#$adgo_lib
#$adgo_water_lib

manning_n = {
    'metselwerk': 0.015,
    'goed afgewerkt beton': 0.011,
    'betonnen goot': 0.014,
    'waterloop uitgegraven in aarde die glad en uniform is afgewerkt': 0.023,
    'rotsinsnijding die glad en uniform is afgewerkt': 0.033,
    'waterloop gebaggerd in aarde': 0.028,
    'waterloop met aarden bodem voorzien van steenbestorting langs het talud': 0.032
}
decimalen = 2
print(decimalen) # [0]

lengte = kies_getal_stap(2, 5, 0.5, 1)
print(lengte) # [1]

helling = kies_getal_stap(500, 4000, 500, 0)

verval = (lengte * 1000) / helling
print(round(verval, decimalen)) # [2]

diepte = kies_getal_stap(0.8, 1.2, 0.1, decimalen)
print(diepte) # [3]

bodem = kies_getal_stap(0.4, 0.8, 0.1, decimalen)
print(bodem) # [4]

talud = kies_integer_getal_stap(1, 5, 1)
print(talud) # [5]

beschrijving = random.choice(list(manning_n.keys()))
n_waarde = manning_n[beschrijving]
print(beschrijving) # [6]

# vraag a Bereken de hydraulische straal R
A = (bodem + diepte) * diepte
O = bodem + 2 * diepte * (1 + talud**2)**0.5
R = A / O
print(round(R, decimalen)) # [7]

# vraag b Bereken de helling van de energielijn I
I = verval / (lengte * 1000)
print(round(I, 5)) # [8]

# vraag c Bepaal de ruwheidsfactor n volgens Manning
print(round(n_waarde, 3)) # [9]

# vraag d Bereken de gemiddelde snelheid v volgens Manning
v = (1 / n_waarde) * R**(2/3) * I**0.5
print(round(v, decimalen)) # [10]

#")