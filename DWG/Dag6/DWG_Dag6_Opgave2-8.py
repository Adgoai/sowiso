from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Energieverlies bij plotselinge verwijding van een horizontale buis
# De volgende gegevens zijn gegeven:
# Diameter links = 220 mm
# Diameter rechts = 470 mm
# Debiet is 71 l/s
# Druk links tov midden buis is 46 kPa
# Als referentielijn wordt de as van de leidingen gekozen. Punten P1 en P2 liggen op de referentielijn. Door de leiding stroomt zoetwater.
# Verder nemen we aan dat er vanwege de korte afstand geen wrijvingsverlies zal optreden.
# Bereken de stroomsnelheid in de linkerbuis.


#sw_Python("
#versie 22-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

diameter_links = kies_integer_getal_stap(150,300,10)
print(diameter_links) # [1] (mm)

diameter_rechts = diameter_links + kies_integer_getal_stap(200,300,10)
print(diameter_rechts) # [2] (mm)

debiet = kies_integer_getal_stap(100,200,1)
print(debiet) # [3] (l/s)

druk_links = kies_integer_getal_stap(40,50,1)
print(druk_links) # [4] (kPa)

oppervlakte_links = 0.25 * math.pi * (diameter_links / 1000) ** 2

oppervlakte_rechts = 0.25 * math.pi * (diameter_rechts / 1000) ** 2

# vraag 2 Bereken de stroomsnelheid in de linkerbuis.
stroomsnelheid_links = (debiet / 1000) / oppervlakte_links
print(round(stroomsnelheid_links, decimalen)) # [5] (m/s)

# vraag 3 Wat wordt de drukhoogte h1 links / bovenstrooms?
drukhoogte_links = (druk_links * 1000) / (water.g * 1000)
print(round(drukhoogte_links, decimalen)) # [6] (m)

# vraag 4 Wat wordt de totale energiehoogte aan de linker (bovenstrooms) kant?
snelheidshoogte_links = (stroomsnelheid_links ** 2) / (2 * water.g)

energiehoogte_links = drukhoogte_links + snelheidshoogte_links
print(round(energiehoogte_links, decimalen)) # [7] (m)

# vraag 5 Wat wordt de stroomsnelheid in de rechterbuis?
stroomsnelheid_rechts = (debiet / 1000) / oppervlakte_rechts
print(round(stroomsnelheid_rechts, decimalen)) # [8] (m/s)

# vraag 6 Bereken het energieverlies ten gevolge van de plotseling verwijding.
energieverlies = (stroomsnelheid_links - stroomsnelheid_rechts) ** 2 / (2 * water.g)
print(round(energieverlies, decimalen)) # [9] (m)

# vraag 7 Wat wordt de drukhoogte h2 rechts / benedenstrooms?
snelheidshoogte_rechts = (stroomsnelheid_rechts ** 2) / (2 * water.g)
drukhoogte_rechts = energiehoogte_links - energieverlies - snelheidshoogte_rechts
print(round(drukhoogte_rechts, decimalen)) # [10] (m)

# vraag 8 Wat wordt de druk in de rechterbuis? (kPa)
druk_rechts = (1000 * drukhoogte_rechts * water.g) / 1000
print(round(druk_rechts, decimalen)) # [11] (kPa)

#")
