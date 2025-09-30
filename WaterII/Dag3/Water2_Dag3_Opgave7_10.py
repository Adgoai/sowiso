from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Diameter van de buis is.
# Bereken het oppervlakte in m2
# Gebruik 2 decimalen en vergeet niet de eenheid m2 te vermelden
# NB in moodle werkte we met significante cijfers. In sowiso werken we met decimalen

#sw_Python("
#versie 17-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen)  # [0]

diameter = kies_getal_stap(1, 4, 0.2, 1)
print(diameter)  # [1]

kin_viscositeit = water.kin_visco
print(kin_viscositeit)  # [2]

stroomsnelheid = kies_getal_stap(0.5, 2, 0.1, 1)
print(stroomsnelheid)  # [3]

#Vraag 7 Berekenen het oppervlakte in m2
oppervlakte = 0.25 * 3.14159 * diameter ** 2
print(round(oppervlakte, decimalen))  # [4]

# Vraag 8 Bereken de natte omtrek in m
omtrek = 3.14159 * diameter
print(round(omtrek, decimalen))  # [5]

# Vraag 9 Bereken de hydraulische straal in m
hydraulische_straal = oppervlakte / omtrek
print(round(hydraulische_straal, decimalen))  # [6]

# Vraag 10 Bereken R bij half gevulde buis
hydraulische_straal_helft = hydraulische_straal
print(round(hydraulische_straal_helft, decimalen))  # [7]

#")