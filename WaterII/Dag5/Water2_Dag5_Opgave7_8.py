from adgo_lib import kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Maaiveld 0 m NAP,
# Drainagebuizen liggen 1,1 m beneden het maaiveld,
# Het grondwater mag maximaal 0,1 m boven de drainagebuizen stijgen.
# De ondoorlatende laag bevindt zich op -8 m NAP,
# We gaan uit van een neerslag van 17 mm per dag,
# De doorlaatbaarheidscoëfficient is 4 * 10-6  m/s
# Wat is de waarde van H0 ?
# Gebruik 2 decimalen en vergeet de eenheid niet.

#sw_Python("
#versie 20-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

maaiveldhoogte = kies_getal_stap(-0.5, 0.5, 0.1, 1)
print(maaiveldhoogte)  # [2]

diepte_drainage = kies_getal_stap(0.8, 1.4, 0.1, 1)
print(diepte_drainage)  # [3]

max_stijging_gw = kies_getal_stap(0.4, 0.9, 0.1,1)
print(max_stijging_gw)  # [4]

diepte_waterondoorlatende_laag = kies_getal_stap(-10.0, -7.0, 0.1, 1)
print(diepte_waterondoorlatende_laag)  # [5]

neerslagintensiteit = kies_integer_getal_stap(15, 25, 1)
print(neerslagintensiteit)  # [6]

doorlaatbaarheidscoefficient = kies_integer_getal_stap(2, 10, 1)
doorlaatbaarheidscoefficient = doorlaatbaarheidscoefficient * 10 ** -6
print(doorlaatbaarheidscoefficient)  # [7]

# Vraag 7 Wat is de waarde voor H0 (Hmidden) in m. Gebruik 2 decimalen.
Hmidden = maaiveldhoogte - diepte_waterondoorlatende_laag - diepte_drainage + max_stijging_gw
print(round(Hmidden, decimalen_2))  # [8]

# Vraag 8 Wat is de afstand tussen de drainagebuizen in m. Gebruik 2 decimalen.
H1 = maaiveldhoogte - diepte_waterondoorlatende_laag - diepte_drainage
vert_stroomsnelheid = (neerslagintensiteit / 1000 ) / (24 * 3600)

l = ((Hmidden ** 2 - H1 ** 2) * doorlaatbaarheidscoefficient / vert_stroomsnelheid ) ** (1/2)
l = 2 * l
print(round(l, decimalen_2))  # [9]

#")