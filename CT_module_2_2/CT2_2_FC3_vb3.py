from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water
import numpy as np

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Wat is het gewicht (in kN) van het tunnelelement?
# Hoe hoog drijft het tunnelelement boven de waterlijn, voordat de ballasttanks met water worden gevuld?

#sw_Python("
#versie 19-11-2025
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

dichtheid_water = 1000
print(dichtheid_water) # [1]

dichtheid_beton = 2500
print(dichtheid_beton) # [2]

breedte_uitw = kies_getal_stap(8.0, 15.5, 0.5, decimalen)
print(breedte_uitw) # [3]

hoogte_uitw = kies_getal_stap(5, 8.5, 0.5, decimalen)
print(hoogte_uitw) # [4]

randje = kies_getal_stap(0.2, 0.9, 0.1, decimalen)

h = hoogte_uitw - randje
O = breedte_uitw * h / 2.5
a = 4
b =(2 * breedte_uitw + 2 * hoogte_uitw)
c = O

# bereken x met numpy ax^x - bx + c = 0
x = np.roots([-a, b, -c])
x = min(x[x > 0])
x = round(x, 1)

wanddikte = x
while True:
    breedte_uitw = kies_getal_stap(8.0, 15.5, 0.5, decimalen)

    hoogte_uitw = kies_getal_stap(5, 8.5, 0.5, decimalen)

    randje = kies_getal_stap(0.2, 0.9, 0.1, decimalen)

    h = hoogte_uitw - randje
    O = breedte_uitw * h / 2.5
    a = 4
    b =(2 * breedte_uitw + 2 * hoogte_uitw)
    c = O

    x = np.roots([-a, b, -c])
    x = min(x[x > 0])
    x = round(x, 1)

    wanddikte = x

    breedte_inw = breedte_uitw - 2 * wanddikte

    hoogte_inw = hoogte_uitw - 2 * wanddikte

    lengte = kies_getal_stap(40, 90, 10, decimalen)

    opp_m =breedte_uitw * hoogte_uitw - breedte_inw * hoogte_inw
    gewicht_beton = opp_m * lengte * water.g * dichtheid_beton / 1000

    druk_onderzijde = (gewicht_beton * 1000) / (lengte * breedte_uitw)

    diepte = druk_onderzijde / (water.sgzoet * water.g)
    rand = hoogte_uitw - diepte
    if rand > 0.05:
        break

print(breedte_uitw) # [3]
print(hoogte_uitw) # [4]
print(round(breedte_inw, decimalen)) # [5]
print(round(hoogte_inw, decimalen)) # [6]
print(lengte) # [7]
print(round(gewicht_beton, 0)) # [8]
print(round(druk_onderzijde, decimalen)) # [9]
print(round(diepte, decimalen)) # [10]
print(round(rand, decimalen)) # [11]

volume_boven_water = rand * breedte_uitw * lengte
ballast = volume_boven_water * 1000
print(round(ballast, 0)) # [12]

#")

def test_berekening():
    successen = 0
    mislukkingen = 0

    for i in range(500):
        max_pogingen = 500
        for poging in range(max_pogingen):
            breedte_uitw = kies_getal_stap(8.0, 15.5, 0.5, decimalen)
            hoogte_uitw = kies_getal_stap(5, 8.5, 0.5, decimalen)
            randje = kies_getal_stap(0.2, 0.9, 0.1, decimalen)

            h = hoogte_uitw - randje
            O = breedte_uitw * h / 2.5
            a = 4
            b = (2 * breedte_uitw + 2 * hoogte_uitw)
            c = O

            x = np.roots([-a, b, -c])
            x = min(x[x > 0])
            x = round(x, 1)
            wanddikte = x

            breedte_inw = breedte_uitw - 2 * wanddikte
            hoogte_inw = hoogte_uitw - 2 * wanddikte
            lengte = kies_getal_stap(40, 90, 10, decimalen)

            opp_m = breedte_uitw * hoogte_uitw - breedte_inw * hoogte_inw
            gewicht_beton = opp_m * lengte * water.g * dichtheid_beton / 1000
            druk_onderzijde = (gewicht_beton * 1000) / (lengte * breedte_uitw)
            diepte = druk_onderzijde / (water.sgzoet * water.g)
            rand = hoogte_uitw - diepte

            if rand > 0.05:
                if rand > 0:
                    successen += 1
                else:
                    mislukkingen += 1
                    print(f"Test {i + 1}: rand = {rand:.3f} (niet positief!)")
                break

    print(f"\nResultaten:")
    print(f"Successen (rand > 0): {successen}")
    print(f"Mislukkingen (rand <= 0): {mislukkingen}")
    print(f"Totaal: {successen + mislukkingen}")


# Voer de test uit
test_berekening()

