import random

from Bouwfysica.Marielle.Bouwfysica_w7_2 import stookseizoen, t_binnen
from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 31-10-2024
#$adgo_lib
#$adgo_bouwfysica_lib

# Een bewoner wil een aanpassing maken in zijn woning. Hiervoor gaat hij 3 m2 (varianten: van 2 t/m 4 m2 met stappen van 0,5) extra ramen in de uitwendige scheidingsconstructie aanbrengen. In verband met de zonne-energiebijdrage besluit de bewoner de ramen in de zuidgevel (varianten: zuidoost, in het platte dak) te plaatsen. De bewoner vraagt zich af of door de komst van deze extra ramen het energieverbruik omhoog of omlaag zal gaan? En ook hoeveel het omhoog op omlaag gaat.
# Gebruik hiervoor de formules van Qtransmissie en Qzon:

#Uitgangspunten (niet variëren):
# Voor de huidige  niet-transparante  gevel/dak wordt uitgegaan van 0,4 W/m2K voor de U-waarde.
# De U-waarde van het nieuwe glas+kozijn is 1,4 W/m2K.
# De ZTA-waarde van het glas bedraagt 0,6.
# Het stookseizoen duurt 4000 uren.
# De gemiddelde binnen- en buitentemperatuur zijn respectievelijk 18°C en 5°C.
# Factor a mag in deze  berekening  buiten  beschouwing worden gelaten.
# Gemiddelde zoninstraling over het stookseizoen:
# zuid = 65 W/m2
# zuidwest en zuidoost = 55 W/m2
# west en oost = 35 W/m2
# noordwest en noordoost = 25 W/m2
# noord = 20 W/m2
# horizontaal vlak = 60 W/m2

Opp_extra_raam = kies_getal_stap(2, 4, 0.5, 1)

locatie_set = [
    {'locatie': 'de zuidoostgevel', 'zoninstraling': 55},
    {'locatie': 'de zuidgevel', 'zoninstraling': 65},
    {'locatie': 'het platte dak', 'zoninstraling': 60}
]

keuze = random.choice(locatie_set)
locatie = keuze['locatie']
zoninstraling = keuze['zoninstraling']

U_huidig = 0.4
U_nieuw = 1.4
ZTA = 0.6
stookseizoen = 4000
t_binnen = 18
t_buiten = 5
a_factor = 1

#berekeningen
Qtransmissie_huidig = round(Opp_extra_raam * U_huidig * (stookseizoen / 1000) * (t_binnen - t_buiten), 1)
Qtransmissie_nieuw = round(Opp_extra_raam * U_nieuw * (stookseizoen / 1000) * (t_binnen - t_buiten), 1)
Qzon = round(Opp_extra_raam * ZTA * zoninstraling * (stookseizoen / 1000), 1)
Qwinst =round(Qzon - Qtransmissie_nieuw, 1)
Energie = round(Qtransmissie_huidig + Qwinst, 1)

print(Opp_extra_raam) # [0]
print(locatie) # [1]
print(zoninstraling) # [2]
print(U_huidig) # [3]
print(U_nieuw) # [4]
print(ZTA) # [5]
print(stookseizoen) # [6]
print(t_binnen) # [7]
print(t_buiten) # [8]
print(a_factor) # [9]
print(Qtransmissie_huidig) # [10]
print(Qtransmissie_nieuw) # [11]
print(Qzon) # [12]
print(Qwinst) # [13]
print(Energie) # [14]
#")
