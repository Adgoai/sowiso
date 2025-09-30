from adgo_lib import kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Sloot: waterdiepte d = 3,98 m, bodembreedte w = 4,35 m, talud rechts is 1 : 4. Talud links 1 : 3
# Bereken de hydraulische straal R
# Gebruik 2 decimalen en eenheid is m

#sw_Python("
#versie 28-11-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen)  # [0]

bodembreedte = kies_getal_stap(1, 3, 0.1, 2)
print(bodembreedte)  # [1]

waterdiepte = kies_getal_stap(1, 3, 0.1, 2)
print(waterdiepte)  # [2]

talud_links = kies_integer_getal_stap(1 , 6, 1)  # taludhelling is 1 : talud
print(talud_links)  # [3]

talud_rechts = kies_integer_getal_stap(1 , 6, 1)  # taludhelling is 1 : talud

# talud links en rechts moeten verschillend in waarde zijn
while talud_rechts == talud_links:
    talud_rechts = kies_integer_getal_stap(1 , 6, 1)  # taludhelling is 1 : talud

print(talud_rechts)  # [4]

oppervlakte = bodembreedte * waterdiepte + 0.5 * talud_links * waterdiepte * waterdiepte + 0.5 * talud_rechts * waterdiepte * waterdiepte
# print(oppervlakte)
natteomtrek = bodembreedte + (waterdiepte ** 2 + (waterdiepte * talud_links) ** 2 ) ** 0.5 + (waterdiepte ** 2 + (waterdiepte * talud_rechts) ** 2 ) ** 0.5
# print(natteomtrek)

# Vraag 15 Bereken de hydraulische straal in m
hydraulische_straal = oppervlakte / natteomtrek
print(round(hydraulische_straal, decimalen))  # [5]

#")