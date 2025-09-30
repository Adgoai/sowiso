import random

from Bouwfysica.Marielle.Bouwfysica_w7_2 import t_binnen, t_buiten
from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Voor een slaapkamer worden een aantal “maatregelen” overwogen. Welke is het meest effectief als het gaat om het beperken van het transmissieverlies?
# Ga voor de berekeningen uit van een gemiddelde binnen- en buitentemperatuur gedurende het stookseizoen is respectievelijk 18°C en 5°C en een stookseizoen van 4000uur. De totale uitwendige scheidingsconstructie van de slaapkamer is 9,5 m2. Er is geen dak of vloer die aan de buitenlucht grenst.
# Er is een raam van 1,5m2 bestaande uit een houten kozijn met enkel glas. Dit heeft een U-waarde van 4,7 W/m2K. Het glas kan worden vervangen door HR++ glas in het bestaande kozijn. De nieuwe U-waarde wordt dan 1,3 W/m2K.
# De slaapkamer heeft 8 m2 gesloten buitengevel bestaande uit een ongeïsoleerde spouwmuur. De Rc van deze constructie is 1,3 m2K/W. Door de spouw na te isoleren, kan de Rc-waarde van de gevel worden verhoogd naar 2,5 m2K/W.
# De slaapkamer wordt slechts beperkt verwarmd waardoor we uit mogen gaan van een gemiddelde binnentemperatuur van 15°C. Je mag het effect van (extra) warmteverlies dat hierdoor tussen ruimten binnen de woning optreedt negeren.
# Varianten niet random, omdat antwoorden vergeleken worden. Rc, U-waarden en binnentemperatuur blijven gelijk. Variëren in oppervlakken. Voor deze varianten blijven de conclusies gelijk (niet de getallen uiteraard).
# Variant 2: raam 1m2, gesloten 8,5m2
# Variant 3: raam 2m2, gesloten 12m2
# Variant 4: raam 2m2, gesloten 10m2

#sw_Python("
#versie 30-10-2024
#$adgo_lib
#$adgo_bouwfysica_lib

varianten_set = [
    {'raam': 1.5, 'gesloten': 8},
    {'raam': 1, 'gesloten': 8.5},
    {'raam': 2, 'gesloten': 12},
    {'raam': 2, 'gesloten': 10}
]

keuze = random.choice(varianten_set)

raam = keuze['raam']
gesloten = keuze['gesloten']
totaal = raam + gesloten

t_binnen = 18
t_buiten = 5
stookseizoen = 4000

U_bestaand =4.7
U_nieuw = 1.3

Rc_bestaand = 1.3
Rc_nieuw = 2.5
t_slaapkamer = 15

Rsi = 0.13 # m²K/W
Rse = 0.04 # m²K/W

#berekeningen

U_gevel = round(1 / (Rsi + Rse + Rc_bestaand), 3)
U_gevel_nieuw = round(1 / (Rsi + Rse + Rc_nieuw), 3)

Q_gevel = round(totaal * U_gevel * (stookseizoen / 1000) * (t_binnen - t_buiten), 0)
Q_raam = round(raam * U_bestaand * (stookseizoen / 1000) * (t_binnen - t_buiten), 0)
Q_totaal_bestaand = round(Q_gevel + Q_raam, 0)

Q_raam_nieuw = round(raam * U_nieuw * (stookseizoen / 1000) * (t_binnen - t_buiten), 0)
Q_raam_besparing = round(Q_raam - Q_raam_nieuw, 0)

Q_gevel_nieuw = round(totaal * U_gevel_nieuw * (stookseizoen / 1000) * (t_binnen - t_buiten), 0)
Q_gevel_besparing = round(Q_gevel - Q_gevel_nieuw, 0)

Q_raam_slaapkamer = round(raam * U_nieuw * (stookseizoen / 1000) * (t_slaapkamer - t_buiten), 0)
Q_gevel_slaapkamer = round(totaal * U_gevel_nieuw * (stookseizoen / 1000) * (t_slaapkamer - t_buiten), 0)
Q_totaal_slaapkamer = round(Q_raam_slaapkamer + Q_gevel_slaapkamer, 0)

Q_slaapkamer_besparing = round(Q_totaal_bestaand - Q_totaal_slaapkamer, 0)

print(raam) # 0
print(gesloten) # 1
print(totaal) # 2
print(t_binnen) # 3
print(t_buiten) # 4
print(stookseizoen) # 5
print(U_bestaand) # 6
print(U_nieuw) # 7
print(Rc_bestaand) # 8
print(Rc_nieuw) # 9
print(t_slaapkamer) # 10
print(Rsi) # 11
print(Rse) # 12
print(U_gevel) # 13
print(U_gevel_nieuw) # 14
print(Q_gevel) # 15
print(Q_raam) # 16
print(Q_totaal_bestaand) # 17
print(Q_raam_nieuw) # 18
print(Q_raam_besparing) # 19
print(Q_gevel_nieuw) # 20
print(Q_gevel_besparing) # 21
print(Q_raam_slaapkamer) # 22
print(Q_gevel_slaapkamer) # 23
print(Q_totaal_slaapkamer) # 24
print(Q_slaapkamer_besparing) # 25

#")
