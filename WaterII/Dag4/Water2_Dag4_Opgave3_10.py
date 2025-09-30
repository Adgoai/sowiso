from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Een kanaal met een volkomen lange overlaat heeft een afvoer van 62,2 m3/s. De drempelbreedte b = 15,2 m en de drempelhoogte (kruin) ligt 1,6 beneden het aangegeven nulniveau, Zie figuur 7.18.  De doorsnede is bovenstrooms van de overlaat.
# Deze opgave is gebaseerd op Nortier 7.9 vraagstuk 2.
# Bereken de het natte oppervlak bovenstrooms van de overlaat (fig 7.18)
# Gebruik 2 decimalen.

#sw_Python("
#versie 03-12-2024
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

decimalen_3 = 3
print(decimalen_3)  # [1]

bodembreedte = 21.0
print(bodembreedte)  # [2]

waterdiepte = 3.0
print(waterdiepte)  # [3]

talud = 3  # taludhelling is 1 : talud
print(talud)  # [4]

debiet = kies_getal_stap(50.0,80.0,0.5,2)
print(debiet)  # [5]

drempelbreedte = bodembreedte
print(drempelbreedte)  # [6]

# "Drempelhoogte" Is hier een verwarrende term, omdat dit de hoogte tov de waterstand is, normaal gesproken is de hoogte tov de bodem
drempelhoogte = kies_getal_stap(1.4,1.7,0.1,2)
print(drempelhoogte)  # [7]

# Vraag 3 Bereken de het natte oppervlak bovenstrooms van de overlaat (m2)
oppervlakte = round(bodembreedte * waterdiepte + talud * waterdiepte * waterdiepte, decimalen_2)
print(oppervlakte)  # [8]

# Vraag 4 Bereken de stroomsnelheid bovenstrooms van de overlaat (m/s)
stroomsnelheid = round(debiet / oppervlakte, decimalen_2)
print(stroomsnelheid)  # [9]

# Vraag 5 Bereken de snelheidshoogte bovenstrooms van de overlaat (m)
snelheidshoogte = round(stroomsnelheid ** 2 / (2 * water.g), decimalen_3)
print(snelheidshoogte)  # [10]

# Vraag 6 Bereken de de energiehoogte bovenstrooms van de overlaat (m)
energiehoogte_bovenstrooms = round(drempelhoogte + snelheidshoogte, decimalen_3)
print(energiehoogte_bovenstrooms)  # [11]

# Vraag 7 Bereken de afvoercoëfficiënt cvl van deze volkomen lange overlaat (m1/2/s)
afvoercoefficient = round(debiet / (drempelbreedte * energiehoogte_bovenstrooms ** 1.5), decimalen_2)
print(afvoercoefficient)  # [12]

# vraag 8 Bereken de waterhoogte boven de overlaat aan de benedenstroomse zijde (m)
kritische_waterhoogte =round((2 / 3)  * energiehoogte_bovenstrooms, decimalen_2)
print(kritische_waterhoogte)  # [13]

# Vraag 9 Wat was ook alweer de waterstand boven de kruin aan de bovenstroome zijde (m)
waterstand_bovenstrooms = drempelhoogte
print(round(waterstand_bovenstrooms, decimalen_2))  # [14]

# Vraag 10 Wat wordt nu de gemiddelde stroomsnelheid boven de overlaat (m/s)
gemiddelde_diepte = (waterstand_bovenstrooms + kritische_waterhoogte) / 2
gemiddelde_stroomsnelheid = debiet / (bodembreedte * gemiddelde_diepte)
print(round(gemiddelde_stroomsnelheid, decimalen_2))  # [15]

#")