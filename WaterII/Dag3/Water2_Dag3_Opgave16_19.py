from adgo_lib import kies_getal_stap, kies_integer_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Bodembreedte w	=	9	m
# Taluds 1 : x	=	1
# Waterdiepte  d	=	2	m
# Coefficient van Manning n	=	0,04	s/m1/3
# Dimensies watergang
# Lengte	=	1000	m
# Bodemverhang 1 	:	1556
# We gaan uit van eenparige permanente stroming. Debiet , gemiddelde stroomsnelheid en waterdiepte zijn overal gelijk
# Bereken de hydraulische straal R
# Gebruik 2 decimalen en vergeet de eenheid niet.

#sw_Python("
#versie 13-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen)  # [0]

bodembreedte = kies_getal_stap(1, 3, 0.1, 2)
print(bodembreedte)  # [1]

waterdiepte = kies_getal_stap(1, 3, 0.1, 2)
print(waterdiepte)  # [2]

talud = kies_integer_getal_stap(1 , 5, 1)  # taludhelling is 1 : talud
print(talud)  # [3]

kin_visco = water.kin_visco
print(kin_visco)  # [4]

coef_manning = kies_getal_stap(0.02, 0.06, 0.01, 2)
print(coef_manning)  # [5]

lengte = kies_integer_getal_stap(500, 2000, 100)
print(lengte)  # [6]

bodemverhang = kies_integer_getal_stap(1000, 2000, 100) # bodemverhang is 1 : bodemverhang
print(bodemverhang)  # [7]

# vraag 16 Bereken de hydraulische straal R
oppervlakte = bodembreedte * waterdiepte + talud * waterdiepte * waterdiepte
# print(oppervlakte)
natteomtrek = bodembreedte + 2 * (waterdiepte ** 2 + (waterdiepte * talud) ** 2 ) ** 0.5
# print(natteomtrek)

hydraulische_straal = oppervlakte / natteomtrek
print(round(hydraulische_straal, decimalen))  # [8]

# vraag 17 bereken de stroomsnelheid op basis van de formule van Manning
stroomsnelheid = (1 / coef_manning) * hydraulische_straal**(2/3) * (1 / bodemverhang)**(1/2)
print(round(stroomsnelheid, decimalen))  # [9]

# vraag 18 bereken het debiet
debiet = oppervlakte * stroomsnelheid
print(round(debiet, decimalen))  # [10]

# vraag 19 berkenen reynoldsgetal
reynoldsgetal = stroomsnelheid * hydraulische_straal / kin_visco
print(round(reynoldsgetal, decimalen))  # [11]

#")