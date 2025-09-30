from adgo_lib import kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Sloot: waterdiepte d = 3,98 m, bodembreedte w = 4,35 m, talud is 1 : 4. Talud gelijk aan beide zijdes
# Bereken de hydraulische straal R
# Gebruik 2 decimalen en eenheid is m

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

talud = kies_integer_getal_stap(1 , 5, 1)
print(talud)  # [3]

oppervlakte = bodembreedte * waterdiepte + talud * waterdiepte * waterdiepte
# print(oppervlakte)
natteomtrek = bodembreedte + 2 * (waterdiepte ** 2 + (waterdiepte * talud) ** 2 ) ** 0.5
#print(natteomtrek)

# Vraag 13 Bereken de hydraulische straal in m
hydraulische_straal = oppervlakte / natteomtrek
print(round(hydraulische_straal, decimalen))  # [4]

#")