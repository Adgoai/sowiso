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
#versie 10-01-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

lengte = kies_integer_getal_stap(40,60,1)
print(lengte) # [1] (m)

breedte = kies_getal_stap(3,5,0.1,1)
print(breedte) # [2] (m)

hoogte = kies_getal_stap(0.6,1.1,0.1, 1) * breedte
print(round(hoogte, decimalen)) # [3] (m)

contractiecoefficient = kies_getal_stap(0.4,0.6,0.01, 2)
print(contractiecoefficient) # [4] (-)

wrijvingsfactor = kies_getal_stap(0.03,0.06,0.01, 2)
print(wrijvingsfactor) # [5] (-)

bodemhoogte = kies_getal_stap(0.4,0.6,0.01, 2)
print(bodemhoogte) # [6] (m)

waterstand_benedenstrooms = bodemhoogte + hoogte + kies_getal_stap(0.4,0.8,0.1, 2)
print(round(waterstand_benedenstrooms, decimalen)) # [7] (m)

stroomsnelheid_bovenstrooms = 0
print(round(stroomsnelheid_bovenstrooms, decimalen)) # [8] (m/s)

stroomsnelheid_benedenstrooms = 0
print(round(stroomsnelheid_benedenstrooms, decimalen)) # [9] (m/s)

ksie_in = (1/contractiecoefficient - 1)**2
print(round(ksie_in, decimalen)) # [10] (-)

oppervlakte = breedte * hoogte

natte_omtrek = 2 * breedte + 2 * hoogte

hydraulische_straal = oppervlakte / natte_omtrek

ksie_wrijving = wrijvingsfactor * lengte / (4 * hydraulische_straal)
print(round(ksie_wrijving, decimalen)) # [11] (-)

ksie_uit = 1
print(round(ksie_uit, decimalen)) # [12] (-)

ksie_tot = ksie_in + ksie_wrijving + ksie_uit

snelheid = kies_getal_stap(1.2,2.1,0.1,1)

verval = ksie_tot * snelheid**2 / (2 * water.g)
print(round(verval, decimalen)) # [13] (m)

# vraag 1 Bereken ksie_totaal
print(round(ksie_tot, decimalen)) # [14] (-)

# vraag 2 bereken de stroomsnelheid door de duiker
print(round(snelheid, decimalen)) # [15] (m/s)

# vraag 3 bereken het debiet door de duiker
debiet = snelheid * oppervlakte
print(round(debiet, decimalen)) # [16] (m3/s)


#")
