from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Een horizontale buis heeft een lengte van 5061 m en een diameter van 1,07 m. Wrijvingsfactor λ= 0,02[-].
# De buis is voor 100% gevuld met zoetwater. De reservoirs bovenstrooms en benedenstrooms zijn groot.
# Bereken het drukverschil welk nodig is voor een debiet van 1,84 m3/s.  Je mag aannemen dat intree en uitree verlies verwaarloosbaar zijn.

#sw_Python("
#versie 28-02-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

lengte = kies_integer_getal_stap(5000,6000,10)
print(lengte) # [1] (m)

diameter = kies_getal_stap(1,1.5,0.01)
print(diameter) # [2] (m)

snelheid = kies_getal_stap(0.8,2.5, 0.1, 2)
oppervlakte = 0.25 * math.pi * (diameter) ** 2
hydraulsche_straal = diameter / 4
snelheidshoogte = (snelheid ** 2) / (2 * water.g)

debiet = snelheid * oppervlakte
print(round(debiet,decimalen)) # [3] (m3/s)

wrijvingsfactor = 0.02

# vraag 2a Bereken het wrijvingsverlies (in m) Darcy-Weisbach
wrijvingsverlies_m = wrijvingsfactor * (lengte / (4 * hydraulsche_straal)) * snelheidshoogte
print(round(wrijvingsverlies_m, decimalen)) # [4] (m)

# vraag 2b bereken het drukverschil (in kPa) Darcy-Weisbach

drukverschil_kPa = 1000 * water.g * wrijvingsverlies_m / 1000
print(round(drukverschil_kPa, decimalen)) # [5] (kPa)

# vraag 3 bereken het getal van Reynolds  visc = 10^-6
viscositeit = 10 ** -6
reynolds = (hydraulsche_straal * snelheid) / viscositeit
print(round(reynolds, decimalen)) # [6] (Reynolds)

# vraag 4 Is de stroming turbulent of laminair?
# geen python

#")
