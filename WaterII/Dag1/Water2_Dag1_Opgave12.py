from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Ombouwen formules kwadraat naar formules tot de macht 2
# Y = X^0,5  Wat is de waarde voor X
# Gebruik 2 decimalen en geen eenheid

#sw_Python("
#versie 4-7-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

y = kies_getal_stap(0.5, 2.5, 0.1, 2)
print(y) # [1]

x = y ** 2
print(round(x,decimalen)) # [2]

#")