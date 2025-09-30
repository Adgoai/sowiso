from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 27-3-2024
#$adgo_lib
#$adgo_constructie_lib

decimalen = 2
print(decimalen) # [0]

breedte_onder = kies_getal_stap(3000, 7000, 100,0)
print(round(breedte_onder, decimalen)) # [1]

hoogte_talud = kies_getal_stap(1000, 2000, 100,0)
print(round(hoogte_talud, decimalen)) # [2]

lengte_oplegging = kies_getal_stap(800,1200, 50, 0)
print(round(lengte_oplegging, decimalen)) # [3]

lengte_brug = breedte_onder + 2*hoogte_talud + 2*lengte_oplegging
print(round(lengte_brug,decimalen)) # [4]

breedte_brug = kies_getal_stap(2000,3500,100,0)
print(round(breedte_brug, decimalen)) # [5]

dikte_brug = kies_getal_stap(250, 450, 10, 0)
print(round(dikte_brug, decimalen)) # [6]

volume_watergang = (breedte_onder/1000) * (hoogte_talud/1000) + (hoogte_talud/1000 * hoogte_talud/1000)
volume_watergang = round(volume_watergang, decimalen)
print(volume_watergang) # [7]

volume_brug = (lengte_brug/1000) * (breedte_brug/1000) * (dikte_brug/1000)
volume_brug = round(volume_brug, decimalen)
print(volume_brug) # [8]

#")