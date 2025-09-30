from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Energieverlies bij een plotselinge vernauwing van een horizontale buis
# De volgende gegevens zijn gegeven (Diameter en debiet zijn hetzelfde als de vorige opgave
# Diameter links = 470 mm
# Diameter rechts = 220 mm
# Debiet is 71 l/s
# Druk links tov midden buis is 46 kPa
# Als referentielijn wordt de as van de leidingen gekozen. Door de leiding stroomt zoetwater.
# Verder nemen we aan dat er vanwege de korte afstand geen wrijvingsverlies zal optreden.
# Bereken de totale energie H links (bovenstrooms) t.o.v de referentielijn.


#sw_Python("
#versie 28-02-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 4
print(decimalen) # [0]

xi_lijst = [
    {'D1D2': 4.0, 'xi': 0.45},
    {'D1D2': 3.0, 'xi': 0.43},
    {'D1D2': 3.5, 'xi': 0.42},
    {'D1D2': 2.5, 'xi': 0.40},
    {'D1D2': 2.0, 'xi': 0.37},
    {'D1D2': 1.5, 'xi': 0.28},
    {'D1D2': 1.3, 'xi': 0.20},
    #{'D1D2': 1.1, 'xi': 0.01}
]

keuze = random.choice(xi_lijst)

D1D2 = keuze['D1D2']

xi = keuze['xi']

diameter_rechts = kies_integer_getal_stap(150,300,10)
print(diameter_rechts) # [1] (mm)

diameter_links = diameter_rechts * D1D2
print(diameter_links) # [2] (mm)

stroomsnelheid_rechts = kies_getal_stap(0.9,2,0.1,1)

oppervlakte_rechts = 0.25 * math.pi * (diameter_rechts / 1000) ** 2

debiet = stroomsnelheid_rechts * oppervlakte_rechts * 1000
print(round(debiet,0)) # [3] (l/s)

druk_links = kies_integer_getal_stap(40,50,1)
print(druk_links) # [4] (kPa)

oppervlakte_links = 0.25 * math.pi * (diameter_links / 1000) ** 2

stroomsnelheid_links = (debiet / 1000) / oppervlakte_links

drukhoogte_links = (druk_links * 1000) / (water.g * 1000)

snelheidshoogte_links = (stroomsnelheid_links ** 2) / (2 * water.g)

energiehoogte_links = drukhoogte_links + snelheidshoogte_links

snelheidshoogte_rechts = (stroomsnelheid_rechts ** 2) / (2 * water.g)

# vraag 12 Bereken de totale energie H links (bovenstrooms) t.o.v de referentielijn.
print(round(energiehoogte_links, decimalen)) # [5] (m)

# vraag 13 Bereken het energieverlies ten gevolge van de plotselinge vernauwing. (m)
dH = xi * snelheidshoogte_rechts
print(round(dH, decimalen)) # [6] (m)

# vraag 14 Wat wordt de drukhoogte h2 rechts / benedenstrooms? (m)
dh = energiehoogte_links - dH - snelheidshoogte_rechts
print(round(dh, decimalen)) # [7] (m)

#")
