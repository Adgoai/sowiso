from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
# Duiker
#Lengte	=	31	m
#Breedte duiker	=	2,2	m
#Hoogte duiker	=	3,4	m
#Contractiecoëfficiënt μ 	=	0,5	 -
#Wrijvingsfactor λ	=	0,04	 -
#Bodem hoogte	=	0,50	m NAP
#Waterstand benedenstrooms	=	5	m NAP
#Stroomsnelheid bovenstrooms	=	0	m/s
#Stroomsnelheid benedenstrooms	=	0 	m/s
#Verschil in waterstand (verval)	=	1,8	m

#sw_Python("
#versie 06-03-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

lengte = kies_integer_getal_stap(40,60,1)
print(lengte) # [1] (m)

breedte = kies_getal_stap(3,5,0.1,1)
print(breedte) # [2] (m)

hoogte = kies_getal_stap(0.6,1.1,0.1, 1) * breedte
print(round(hoogte, 2)) # [3] (m)

bodemhoogte = kies_getal_stap(0.4,0.6,0.01, 2)
print(bodemhoogte) # [4] (m)

waterstand_bovenstrooms = bodemhoogte + hoogte * kies_getal_stap(0.8,1.0,0.1, 1)
print(round(waterstand_bovenstrooms,2)) # [5] (m)

snelheid_bovenstrooms = kies_getal_stap(0.5,1.5,0.1, 1)

snelheid_benedenstrooms = kies_getal_stap(0.5,1.5,0.1, 1)
if snelheid_benedenstrooms == snelheid_bovenstrooms:
    snelheid_benedenstrooms += 0.2

snelheidshoogte_bovenstrooms =  snelheid_bovenstrooms**2 / (2 * water.g)

snelheidshoogte_benedenstrooms =  snelheid_benedenstrooms**2 / (2 * water.g)

Hspec = waterstand_bovenstrooms + snelheidshoogte_bovenstrooms - bodemhoogte
Hspec23 = (2/3) * Hspec

h3 = 1.1 * Hspec23

waterstand_benedenstrooms = bodemhoogte + h3
print(round(waterstand_benedenstrooms,2)) # [6] (m)

wrijvingsfactor = kies_getal_stap(0.02,0.05,0.01, 2)
print(wrijvingsfactor) # [7] (-)

contractiecoefficient = 0.8
print(contractiecoefficient) # [8] (-)

afvoercoeff_volkomen = 1.5
print(afvoercoeff_volkomen) # [9] (-)

# vraag 25 Bereken de H bovenstrooms tov de bodem van de duiker (Hspec) m
print(round(Hspec, decimalen)) # [10] (m)

# vraag 26 Bereken h3
print(round(h3, decimalen)) # [11] (m)

# vraag 27 h3 - 2/3 H
print(round(h3 - Hspec23, decimalen)) # [12] (m)

# vraag 28 Volkomen of onvolkomen

# vraag 29 bereken de hydraulische straal
waterdiepte = (waterstand_bovenstrooms + waterstand_benedenstrooms ) / 2 - bodemhoogte
oppervlake = breedte * waterdiepte
natteomtrek = breedte + 2 * waterdiepte
hydraulische_straal = oppervlake / natteomtrek
print(round(hydraulische_straal, decimalen)) # [13] (m)

# vraag 30 Bereken de afvoercoefficient bij een onvolkomen overlaat.
ksie_uitstroom = 0.8
ksie_instroom = (1 / contractiecoefficient -1)**2
ksie_wrijving = wrijvingsfactor * lengte / (4 * hydraulische_straal)
ksie_totaal = ksie_uitstroom + ksie_instroom + ksie_wrijving
afvoercoefficient = 1 / (ksie_totaal**0.5)
print(round(afvoercoefficient, decimalen)) # [14] (-)

# vraag 31 Bereken het debiet
debiet = afvoercoefficient * breedte * h3 * math.sqrt(2 * water.g * (Hspec - h3))
print(round(debiet, decimalen)) # [15] (m3/s)

# ik was lui :-(
print(snelheid_bovenstrooms) # [16] (m/s)
print(snelheid_benedenstrooms) # [17] (m/s)


#")
