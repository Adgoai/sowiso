from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# In de polderwatergang van fig. 7.19 wordt een stuwtje geplaatst dat bestaat uit hardhouten damplanken. De watergang voert 1,7 m3/s af. De afvoercoëfficiënt van de stuw is 1,8 m1/2/s.
# Bereken de gemiddelde stroomsnelheid bovenstrooms van het stuwtje, in de watergang uit.
# Gebruik 2 decimalen en vergeet de eenheid niet.
# NB Deze opgave is gebaseerd op Nortier 7.9 opgave 3.

#sw_Python("
#versie 20-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

bodembreedte = 3.0
print(bodembreedte)  # [1]

waterdiepte = 1.0
print(waterdiepte)  # [2]

talud = 2  # taludhelling is 1 : talud
print(talud)  # [3]

debiet = kies_getal_stap(1.0,1.5,0.1,1)
print(debiet)  # [4]

drempelbreedte = 3.0
print(drempelbreedte)  # [5]

afvoercoefficient = kies_getal_stap(1.6,2.0,0.1,1)
print(afvoercoefficient)  # [6]

# Vraag 11 Bereken de gemiddelde stroomsnelheid bovenstrooms van het stuwtje, in de watergang uit.
oppervlakte = bodembreedte * waterdiepte + talud * waterdiepte * waterdiepte
stroomsnelheid = debiet / oppervlakte
print(round(stroomsnelheid, decimalen_2))  # [7]

# Vraag 12 is een multiple choice vraag, is altijd volkomend overlaat

# Vraag 13 Bereken de energiehoogte H ter plaatse van de stuw (m)
energiehoogte = (debiet / (afvoercoefficient * drempelbreedte)) ** (2 / 3)
print(round(energiehoogte, decimalen_2))  # [8]

# Vraag 14 Bereken de hoogte van de stuw (x) (m)
snelheidshoogte = stroomsnelheid ** 2 / (2 * water.g)
stuwhoogte = 1 + snelheidshoogte - energiehoogte
print(round(stuwhoogte, decimalen_2))  # [9]

#")