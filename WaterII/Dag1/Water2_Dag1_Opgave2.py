from adgo_lib import kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#Een buis heeft een diameter van 612 mm. Wat is de diameter uitgedrukt in m? Gebruik 3 decimalen

#sw_Python("
#versie 31-5-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 3
print(decimalen) # [0]

diameter_mm = kies_integer_getal_stap(100, 5000, 1)
print(diameter_mm) # [1]

diameter_m = diameter_mm / 1000
print(round(diameter_m, decimalen)) # [2]

#")