import random

from adgo_lib import kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Bij de volgende oefening is het perceel omringd door sloten. In het perceel liggen drainagebuizen die afvoeren naar de sloten.
# Afstand tussen de drainagebuizen is 16 m,
# Afstand tussen de sloten is 378 m,
# Als neerslag wordt 17 mm/dag,
# Diameter van de drainagebuizen is 80 mm,
# Voor de coëfficiënt van Manning n mag 0.013 s/m1/3 worden aangenomen
# Het bodemverhang van de  drainagebuizen is 1:1000
# Uitgangspunt is dat de drainagebuizen maximaal 50% zijn gevuld.
# Wat is het maximale grondoppervlakte waarvan de neerslag door één drainagebuis zal afvoeren?

#sw_Python("
#versie 20-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen_7 = 7
print(decimalen_7)  # [0]

afstand_drainage = kies_integer_getal_stap(10, 20, 1)
print(afstand_drainage)  # [1]

afstand_watergangen = kies_integer_getal_stap(300, 400, 1)
print(afstand_watergangen)  # [2]

neerslagintensiteit = kies_integer_getal_stap(15, 25, 1)
print(neerslagintensiteit)  # [3]

diameter_drainage = random.choice([60, 80 , 100])
print(diameter_drainage)  # [4]

manning_n = kies_getal_stap(0.01, 0.03, 0.001, 3)
print(manning_n)  # [5]

bodemverhang = 1000 # 1:1000
print(bodemverhang)  # [6]

#  Vraag 9  Wat is het maximale grondoppervlakte waarvan de neerslag door één drainagebuis zal afvoeren? (m2) 0 decimalen
oppervlak = afstand_drainage * afstand_watergangen * 0.5
print(round(oppervlak, 0))  # [7]

# Vraag 10 Wat wordt nu het maximale debiet door één drainagebuis, bij een neerslag van ....mm/dag? (m3/s)
vert_stroomsnelheid = (neerslagintensiteit / 1000 ) / (24 * 3600)
debiet_max = vert_stroomsnelheid * oppervlak
print(round(debiet_max, decimalen_7))  # [8]

# Vraag 11 Hydraulische straal van de drainagebuis (m)
hydraulische_straal = (diameter_drainage / 1000) / 4
print(round(hydraulische_straal, decimalen_7))  # [9]

# Vraag 12 Wat is de gemiddelde stroomsnelheid in de drainagebuis (m/s)
stroomsnelheid = (hydraulische_straal ** (2/3) * (1 / bodemverhang) ** (1/2)) / manning_n
print(round(stroomsnelheid, decimalen_7))  # [10]

# Vraag 13 Maximala afvoercapaciteit van de drainagebuis (m3/s)
opp_drain_half_gevuld = ((1/4) * 3.1415 * (diameter_drainage / 1000) ** 2) / 2
debiet_afvoer = stroomsnelheid * opp_drain_half_gevuld
print(round(debiet_afvoer, decimalen_7))  # [11]

# Vraag 14 Heeft de drainage voldoende capaciteit om de neerslag af te voeren? (ja/nee)
if debiet_max < debiet_afvoer:
    print('nee') # [12]
else:
    print('ja') # [12]

#")