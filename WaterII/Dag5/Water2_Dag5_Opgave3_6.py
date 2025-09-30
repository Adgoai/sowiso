from adgo_lib import kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# We hebben de volgende informatie:
# Maaiveldhoogte  0 m NAP,
# Drainagebuizen liggen op 1,1 m beneden maaiveld,
# Afstand tussen de drainagebuizen is 16 m,
# Aangenomen wordt dat  er op  -8 m NAP een waterondoorlatende laag aanwezig is,
# De neerslagintensiteit is 17 mm per dag,
# De doorlaatbaarheidscoëfficient van de bodem bedraagt 4 * 10-6  m/s
# Wat wordt de verticale stroomsnelheid (neerslag) in m/s.

#sw_Python("
#versie 20-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

decimalen_10 = 10
print(decimalen_10)  # [1]

maaiveldhoogte = kies_getal_stap(-0.5, 0.5, 0.1, 1)
print(maaiveldhoogte)  # [2]

diepte_drainage = kies_getal_stap(0.8, 1.4, 0.1, 1)
print(diepte_drainage)  # [3]

afstand_drainage = kies_integer_getal_stap(15, 25, 1)
print(afstand_drainage)  # [4]

diepte_waterondoorlatende_laag = kies_getal_stap(-10.0, -7.0, 0.1, 1)
print(diepte_waterondoorlatende_laag)  # [5]

neerslagintensiteit = kies_integer_getal_stap(15, 25, 1)
print(neerslagintensiteit)  # [6]

doorlaatbaarheidscoefficient = kies_integer_getal_stap(2, 10, 1)
doorlaatbaarheidscoefficient = doorlaatbaarheidscoefficient * 10 ** -6
print(doorlaatbaarheidscoefficient)  # [7]

# Vraag 3 Wat wordt de verticale stroomsnelheid (neerslag) in m/s. Gebruik 10 decimalen.
vert_stroomsnelheid = (neerslagintensiteit / 1000 ) / (24 * 3600)
print(round(vert_stroomsnelheid, decimalen_10))  # [8]

# Vraag 4 Wat is de afstand tussen de ondoorlatende laag en de drainagebuizen in m. (H1) Gebruik 2 decimalen.
H1 = maaiveldhoogte - diepte_waterondoorlatende_laag - diepte_drainage
print(round(H1, decimalen_2))  # [9]

# Vraag 5 Bereken Hmidden of H0. Gebruik 2 decimalen.
l = afstand_drainage /2
Hmidden = (vert_stroomsnelheid * l ** 2 / doorlaatbaarheidscoefficient + H1 ** 2) ** (1/2)
print(round(Hmidden, decimalen_2))  # [10]

# Vraag 6 Maximale stijging van het grondwater in m. Gebruik 2 decimalen.
stijging = Hmidden - H1
print(round(stijging, decimalen_2))  # [11]

#")