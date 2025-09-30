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
print(hoogte) # [3] (m)

contractiecoefficient = kies_getal_stap(0.4,0.6,0.01, 2)
print(contractiecoefficient) # [4] (-)

wrijvingsfactor = kies_getal_stap(0.03,0.06,0.01, 2)
print(wrijvingsfactor) # [5] (-)

bodemhoogte = kies_getal_stap(0.4,0.6,0.01, 2)
print(bodemhoogte) # [6] (m)

waterstand_benedenstrooms = bodemhoogte + hoogte + kies_getal_stap(0.4,0.8,0.1, 1)
print(round(waterstand_benedenstrooms, 1)) # [7] (m)

snelheid_bovenstrooms = kies_getal_stap(0.5,1,0.1,1)
print(snelheid_bovenstrooms) # [8] (m/s)

snelheid_benedenstrooms = kies_getal_stap(0.5,1,0.1,1)
if snelheid_benedenstrooms == snelheid_bovenstrooms:
    snelheid_benedenstrooms += 0.2

print(snelheid_benedenstrooms) # [9] (m/s)

oppervlakte = breedte * hoogte

natte_omtrek = 2 * breedte + 2 * hoogte

snelheid = kies_getal_stap(1.2,2.1,0.1,1)


ksie_in = (1/contractiecoefficient - 1)**2
print(round(ksie_in, decimalen)) # [10] (-)

hydraulische_straal = oppervlakte / natte_omtrek

ksie_wrijving = wrijvingsfactor * lengte / (4 * hydraulische_straal)
print(round(ksie_wrijving, decimalen)) # [11] (-)

# vraag 23 Bereken ksie_totaal
ksie_uit = (1 - snelheid_benedenstrooms/snelheid)**2
print(round(ksie_uit, 2)) # [12] (-)

ksie_tot = ksie_in + ksie_wrijving + ksie_uit
print(round(ksie_tot, decimalen)) # [13] (-)

debiet = oppervlakte * snelheid
print(round(debiet, decimalen)) # [14] (m3/s)

# vraag 24 wat wordt de waterstand bovenstrooms m NAP
Energieverlies = ksie_tot * snelheid**2 / (2 * water.g)

snelheidshoogte_benedenstrooms = snelheid_benedenstrooms**2 / (2 * water.g)

snelheidshoogte_bovenstrooms = snelheid_bovenstrooms**2 / (2 * water.g)

waterstand_bovenstrooms = waterstand_benedenstrooms + snelheidshoogte_benedenstrooms + Energieverlies - snelheidshoogte_bovenstrooms
print(round(waterstand_bovenstrooms, decimalen)) # [15] (m)


#")
