from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Een watergang in een polder heeft een maximum debiet Q van 238 l/s
# De watergang kruist en dam door middel van een duiker.  De duiker bestaat uit betonnen buizen met
# een totale lengte van 5 m, de wrijvingsfactor λ is 0,02. De maximale toegestane stroomsnelheid in de duiker is 1 m/s. De duiker is geheel gevuld met water.
# Bereken de diameter van de duiker.

#sw_Python("
#versie 10-01-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 3
print(decimalen) # [0]

debiet = kies_integer_getal_stap(200,300,1)
print(debiet) # [1] (l/s)

lengte = kies_integer_getal_stap(5,10,1)
print(lengte) # [2] (m)

wrijvingsfactor = 0.02

max_snelheid = kies_getal_stap(0.5,1,0.01)  # [3] (m/s)
print(max_snelheid) # [3] (m/s)

# vraag 5 bereken de diameter van de duiker
oppervlakte = (debiet / 1000) / max_snelheid
diameter = math.sqrt(4 * oppervlakte / math.pi)
print(round(diameter, decimalen)) # [4] (m)

# vraag 6 energieverlies wrijving
hydraulsche_straal = diameter / 4
snelheids_hoogte = (max_snelheid ** 2) / (2 * water.g)
energieverlies_m = wrijvingsfactor * (lengte / (4 * hydraulsche_straal)) * snelheids_hoogte
print(round(energieverlies_m, 5)) # [5] (m)

# vraag 7 laminair of turbulent
# geen python

#")
