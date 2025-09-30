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
#versie 05-03-2024
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

waterstand_benedenstrooms = bodemhoogte + hoogte + kies_getal_stap(0.4,0.8,0.1, 1)
print(round(waterstand_benedenstrooms,2)) # [7] (m)

snelheid_bovenstrooms = kies_getal_stap(0.1,0.4,0.1,1)
print(snelheid_bovenstrooms) # [8] (m/s)

snelheid_benedenstrooms = kies_getal_stap(0.1,0.5,0.1,1)
if snelheid_benedenstrooms == snelheid_bovenstrooms:
    snelheid_benedenstrooms += 0.1
print(snelheid_benedenstrooms) # [9] (m/s)

ksie_in = (1/contractiecoefficient - 1)**2
print(round(ksie_in, decimalen)) # [10] (-)

oppervlakte = breedte * hoogte

natte_omtrek = 2 * breedte + 2 * hoogte

hydraulische_straal = oppervlakte / natte_omtrek

ksie_wrijving = wrijvingsfactor * lengte / (4 * hydraulische_straal)
print(round(ksie_wrijving, decimalen)) # [11] (-)

ksie_uit = 0.8
print(round(ksie_uit, 2)) # [12] (-)

ksie_tot = ksie_in + ksie_wrijving + ksie_uit

snelheid = kies_getal_stap(1.2,2.1,0.1,1)

verval = ksie_tot * snelheid**2 / (2 * water.g)
print(round(verval, decimalen)) # [13] (m)

#12a toegevoegde vraag : Bereken de hydraulische straal
# zie onderaan print(round(hydraulische_straal, 2)) # [25] (m)

#vraag 12 Bereken skie totaal
print(round(ksie_tot, 2)) # [14] (-)

# vraag 13 snelheidshoogte bovenstrooms
snelheidshoogte_bovenstrooms = snelheid_bovenstrooms**2 / (2 * water.g)
print(round(snelheidshoogte_bovenstrooms, 5)) # [15] (m)

# vraag 14 snelheidshoogte benedenstrooms
snelheidshoogte_benedenstrooms = snelheid_benedenstrooms**2 / (2 * water.g)
print(round(snelheidshoogte_benedenstrooms, 5)) # [16] (m)

# vraag 15 Bereken de stroomsnelheid in de duiker.
print(round(snelheid, decimalen)) # [17] (m/s)

# vraag 16 Bereken het debiet in de duiker.
debiet = snelheid * oppervlakte
print(round(debiet, decimalen)) # [18] (m3/s)

# vraag 17 Bereken de snelheidshoogte in de duiker.
snelheidshoogte = snelheid**2 / (2 * water.g)
print(round(snelheidshoogte, decimalen)) # [19] (m)

# vraag 18 bereken het energieverlies tgv instroom
energieverlies_instroom = ksie_in * snelheidshoogte
print(round(energieverlies_instroom, decimalen)) # [20] (m)

# vraag 19 bereken het energieverlies tgv wrijving
energieverlies_wrijving = ksie_wrijving * snelheidshoogte
print(round(energieverlies_wrijving, decimalen)) # [21] (m)

# vraag 20 bereken het energieverlies tgv uitstroom
energieverlies_uitstroom = ksie_uit * snelheidshoogte
print(round(energieverlies_uitstroom, decimalen)) # [22] (m)

# vraag 21 bereken ksie_uit opnieuw
# Waarschijnlijk is deze niet gelijk aan de aanname en zou je eigenlijk de opgave opnieuw moeten doen. Dit totdat de aanname en de berekening gelijk zijn. :-)
# Voor nu accepteren we het verschil.
oppervlakte_benedenstrooms = debiet / snelheid_benedenstrooms
ksie_nieuw = (1 - oppervlakte / oppervlakte_benedenstrooms)**2
print(round(ksie_nieuw, decimalen)) # [23] (-)

# vraag 22 Snelheidshoogte bij contractie
snelheid_contractie = snelheid / contractiecoefficient
snelheidshoogte_contractie = snelheid_contractie**2 / (2 * water.g)
print(round(snelheidshoogte_contractie, decimalen)) # [24] (m)

print(round(hydraulische_straal, 2)) # [25] (m)

#")
