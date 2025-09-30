from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Energieverlies bij geleidelijke verwijding van een horizontale buis
# De volgende gegevens zijn gegeven (Diameter en debiet zijn hetzelfde als de vorige opgave
# Diameter links = 220 mm
# Diameter rechts = 470 mm
# Debiet is 71 l/s
# Druk links tov midden buis is 46 kPa
# Hoek a = 50 graden
# Als referentielijn wordt de as van de leidingen gekozen. Door de leiding stroomt zoetwater.
# Verder nemen we aan dat er vanwege de korte afstand geen wrijvingsverlies zal optreden.
# Bereken de totale energie H links (bovenstrooms) t.o.v de referentielijn.


#sw_Python("
#versie 28-02-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 3
print(decimalen) # [0]

diameter_links = kies_integer_getal_stap(150,300,10)
print(diameter_links) # [1] (mm)

diameter_rechts = diameter_links * kies_getal_stap(1.3,1.8,0.1,1)
print(round(diameter_rechts,0)) # [2] (mm)

oppervlakte_links = 0.25 * math.pi * (diameter_links / 1000) ** 2

oppervlakte_rechts = 0.25 * math.pi * (diameter_rechts / 1000) ** 2

snelheid = kies_getal_stap(2,4,0.1,1)
debiet = snelheid * oppervlakte_links * 1000
print(round(debiet,0)) # [3] (l/s)

druk_links = kies_integer_getal_stap(40,50,1)
print(druk_links) # [4] (kPa)

hoeka_lijst = [
    #{'hoek': 6, 'n': 0.14},
    #{'hoek': 10, 'n': 0.20},
    {'hoek': 15, 'n': 0.30},
    {'hoek': 20, 'n': 0.40},
    {'hoek': 30, 'n': 0.70},
    {'hoek': 40, 'n': 0.90},
    {'hoek': 50, 'n': 1.00},
    {'hoek': 60, 'n': 1.10},
    {'hoek': 70, 'n': 1.10}
]

keuze = random.choice(hoeka_lijst)

hoek = keuze['hoek']
print(hoek) # [5] (graden)

n = keuze['n']

stroomsnelheid_links = (debiet / 1000) / oppervlakte_links

drukhoogte_links = (druk_links * 1000) / (water.g * 1000)

snelheidshoogte_links = (stroomsnelheid_links ** 2) / (2 * water.g)

stroomsnelheid_rechts = (debiet / 1000) / oppervlakte_rechts

snelheidshoogte_rechts = (stroomsnelheid_rechts ** 2) / (2 * water.g)

# vraag 9 Bereken de totale energie H links (bovenstrooms) t.o.v de referentielijn.
energiehoogte_links = drukhoogte_links + snelheidshoogte_links
print(round(energiehoogte_links, decimalen)) # [6] (m)

# vraag 10 Bereken het energieverlies ten gevolge van de geleidelijke verwijding.
xi = n * (oppervlakte_links / oppervlakte_rechts - 1) ** 2
dh= xi * snelheidshoogte_rechts
print(round(dh, decimalen)) # [7] (m)

# vraag 11 Wat wordt de drukhoogte h2 rechts / benedenstrooms?
drukhoogte_rechts = drukhoogte_links - dh - snelheidshoogte_rechts
print(round(drukhoogte_rechts, decimalen)) # [8] (m)


#")
