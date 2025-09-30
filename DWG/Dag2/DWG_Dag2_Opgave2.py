import random

from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#Van een windveld zijn de volgende gegevens bekend:
#De lengte is 75 km.
#De breedte is 60 km.
#Bereken op basis van figuur 9.2 Nortier de Effectieve Strijklengte.
#Gebruik 1 decimaal en de eenheid is km

#sw_Python("
#versie 7-12-2023
#$adgo_lib
#$adgo_DWG_lib

decimalen = 1
print(decimalen) # [0]

ant_lijst = [
    {'lengte': 25, 'breedte': 5, 'afgelezenFaktor': 0.38},
    {'lengte': 25, 'breedte': 10, 'afgelezenFaktor': 0.58},
    {'lengte': 50, 'breedte': 30, 'afgelezenFaktor': 0.7},
    {'lengte': 75, 'breedte': 60, 'afgelezenFaktor': 0.80},
    {'lengte': 42, 'breedte': 50, 'afgelezenFaktor': 0.91},
    {'lengte': 50, 'breedte': 80, 'afgelezenFaktor': 0.98},
    {'lengte': 25, 'breedte': 10, 'afgelezenFaktor': 0.58}
]

gekozen_antwoord = random.choice(ant_lijst)

lengte = gekozen_antwoord['lengte']
print(lengte) # [1]

breedte = gekozen_antwoord['breedte']
print(breedte) # [2]

afgelezenFaktor = gekozen_antwoord['afgelezenFaktor']
effektieve_strijklengte = lengte * afgelezenFaktor
print(round(effektieve_strijklengte, decimalen)) # [3]

#")
