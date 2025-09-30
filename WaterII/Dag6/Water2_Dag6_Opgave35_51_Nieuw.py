from adgo_lib import kies_getal_stap, kies_integer_getal_stap
import random

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#De watergang heeft benedenstrooms een stuw (korte overlaat). De waterstand benedenstrooms van de stuw staat lager dan de kruin.
#De watergang heeft een bodemverhang, de doorsnede van de watergang is trapeziumvormig en is gelijk over de gehele lengte van de watergang. Ook het debiet blijft gelijk over de gehele lengte van de watergang.
#Halverwege is een duiker aanwezig, deze duiker ligt horizontaal en heeft een rechthoekige doorsnede.

#sw_Python("
#versie 7-12-2023
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

decimalen_4 = 4
print(decimalen_4)  # [1]

decimalen_8 = 8
print(decimalen_8)  # [2]


antwoorden_lijst = [
    {'Set': 1, 'crest': 1.2, 'q': 3.0, 'bodembreedte': 2.5, 'x': 3, 'Ibodem': 1500, 'wcrest': 4.0, 'cbed': 1.2, 'yc': 0.44, 'ye': 0.77},
    {'Set': 2, 'crest': 1.2, 'q': 2.0, 'bodembreedte': 3.5, 'x': 1, 'Ibodem': 3500, 'wcrest': 3.0, 'cbed': 1.1, 'yc': 0.31, 'ye': 0.79},
    {'Set': 3, 'crest': 1.1, 'q': 2.0, 'bodembreedte': 1.4, 'x': 3, 'Ibodem': 4000, 'wcrest': 3.0, 'cbed': 1.0, 'yc': 0.43, 'ye': 0.93},
    {'Set': 4, 'crest': 2.0, 'q': 2.2, 'bodembreedte': 1.8, 'x': 3, 'Ibodem': 2000, 'wcrest': 3.0, 'cbed': 1.8, 'yc': 0.41, 'ye': 0.78},
    {'Set': 5, 'crest': 1.5, 'q': 3.4, 'bodembreedte': 1.8, 'x': 3, 'Ibodem': 1500, 'wcrest': 4.5, 'cbed': 1.3, 'yc': 0.53, 'ye': 0.89},
    {'Set': 6, 'crest': 1.4, 'q': 2.8, 'bodembreedte': 1.1, 'x': 4, 'Ibodem': 5000, 'wcrest': 4.0, 'cbed': 1.2, 'yc': 0.51, 'ye': 1.06},
    {'Set': 7, 'crest': 1.5, 'q': 2.5, 'bodembreedte': 3.6, 'x': 3, 'Ibodem': 3500, 'wcrest': 7.0, 'cbed': 1.0, 'yc': 0.33, 'ye': 0.76},
    {'Set': 8, 'crest': 1.7, 'q': 3.5, 'bodembreedte': 2.3, 'x': 3, 'Ibodem': 1000, 'wcrest': 6.0, 'cbed': 1.4, 'yc': 0.49, 'ye': 0.23},
    {'Set': 9, 'crest': 1.9, 'q': 3.0, 'bodembreedte': 1.6, 'x': 1, 'Ibodem': 1500, 'wcrest': 4.0, 'cbed': 1.7, 'yc': 0.62, 'ye': 1.14},
    {'Set': 10, 'crest': 1.2, 'q': 4.0, 'bodembreedte': 4.7, 'x': 3, 'Ibodem': 1500, 'wcrest': 4.0, 'cbed': 0.8, 'yc': 0.38, 'ye': 0.70},
    {'Set': 11, 'crest': 1.4, 'q': 3.0, 'bodembreedte': 4.6, 'x': 1, 'Ibodem': 5000, 'wcrest': 7.0, 'cbed': 1.0, 'yc': 0.34, 'ye': 0.95},
    {'Set': 12, 'crest': 1.3, 'q': 2.5, 'bodembreedte': 2.5, 'x': 3, 'Ibodem': 2500, 'wcrest': 5.0, 'cbed': 1.0, 'yc': 0.39, 'ye': 0.80},
    {'Set': 13, 'crest': 1.9, 'q': 3.0, 'bodembreedte': 2.3, 'x': 1, 'Ibodem': 3500, 'wcrest': 5.0, 'cbed': 1.6, 'yc': 0.51, 'ye': 1.22},
    {'Set': 14, 'crest': 1.6, 'q': 2.0, 'bodembreedte': 2.3, 'x': 1, 'Ibodem': 3000, 'wcrest': 6.0, 'cbed': 1.1, 'yc': 0.39, 'ye': 0.94},
    {'Set': 15, 'crest': 2.0, 'q': 2.0, 'bodembreedte': 2.1, 'x': 1, 'Ibodem': 2000, 'wcrest': 3.0, 'cbed': 1.7, 'yc': 0.42, 'ye': 0.87},
    {'Set': 16, 'crest': 1.4, 'q': 3.0, 'bodembreedte': 2.5, 'x': 1, 'Ibodem': 5000, 'wcrest': 5.0, 'cbed': 1.1, 'yc': 0.50, 'ye': 1.29},
    {'Set': 17, 'crest': 1.4, 'q': 3.0, 'bodembreedte': 1.6, 'x': 2, 'Ibodem': 4000, 'wcrest': 4.0, 'cbed': 1.6, 'yc': 0.56, 'ye': 1.21},
    {'Set': 18, 'crest': 1.1, 'q': 2.0, 'bodembreedte': 3.0, 'x': 2, 'Ibodem': 4500, 'wcrest': 4.0, 'cbed': 0.7, 'yc': 0.32, 'ye': 0.83},
    {'Set': 19, 'crest': 1.1, 'q': 2.0, 'bodembreedte': 3.6, 'x': 1, 'Ibodem': 2000, 'wcrest': 3.0, 'cbed': 0.8, 'yc': 0.30, 'ye': 0.66},
    {'Set': 20, 'crest': 1.8, 'q': 5.0, 'bodembreedte': 4.7, 'x': 4, 'Ibodem': 1000, 'wcrest': 5.0, 'cbed': 1.8, 'yc': 0.42, 'ye': 0.68}
]

gekozen_antwoord = random.choice(antwoorden_lijst)

debiet = gekozen_antwoord['q']
print(debiet)  # [3]

lengte_stuw_duiker = 350
print(lengte_stuw_duiker)  # [4]

bodemverhang = gekozen_antwoord['Ibodem']
print(bodemverhang)  # [5]

bodemhoogte_beneden = 0.20
print(bodemhoogte_beneden)  # [6]

bodembreedte = gekozen_antwoord['bodembreedte']
print(bodembreedte)  # [7]

taludhelling = gekozen_antwoord['x']
print(taludhelling)  # [8]

coeff_manning = 0.02
print(coeff_manning)  # [9]

kruinhoogte_stuw = gekozen_antwoord['crest']
print(kruinhoogte_stuw)  # [10]

kruinbreedte_stuw = gekozen_antwoord['wcrest']
print(kruinbreedte_stuw)  # [11]

afvoercoeff_stuw = 1.7
print(afvoercoeff_stuw)  # [12]

# Vraag 35 Bepaal de evenwichtsdiepte (m) bovenstrooms van de stuw (afgerond op 2 decimalen)
evenwichtsdiepte = gekozen_antwoord['ye']
print(round(evenwichtsdiepte, decimalen_2))  # [13]

# Vraag 36 Bepaal vervolgens de kritische diepte (m) bovenstrooms van de stuw (afgerond op 2 decimalen)

hkritisch = gekozen_antwoord['yc']
print(round(hkritisch, decimalen_2))  # [14]

# Vraag 37 Is de stroming : stromend of schietend of kritisch?
if (evenwichtsdiepte > hkritisch):
    print('stromend')  # [15]
elif (evenwichtsdiepte < hkritisch):
    print('schietend')  # [15]
else:
    print('kritisch') # [15]

# Vraag 38 Omdat de waterstand benedenstrooms van de stuw lager staat dan de kruin van de stuw kunnen we aannemen dat de stuw volkomen is
# Bereken de H (overstortende straal) ter plaatse van de stuw
# Gebruik 2 decimalen en vergeet de eenheid niet

energieHoogte_stuw = (debiet / (afvoercoeff_stuw * kruinbreedte_stuw))**(2/3)
print(round(energieHoogte_stuw, decimalen_2))  # [16]

# Vraag 39 We nemen aan dat de stroomsnelheid in de watergang net bovenstrooms van de stuw laag is. Snelheidshoogte is ongeveer 0. Energielijn en waterstand (p.n.)zijn ongeveer gelijk
## Bereken de waterstand ter plaats van de stuw.
## Gebruik 2 decimalen en mNAP

waterstand_stuw = kruinhoogte_stuw + energieHoogte_stuw
print(round(waterstand_stuw, decimalen_2))  # [17]

# Vraag 40 Om de waterstand ter plaatse van de duiker te berekenen gaan we de watergang in 2 secties opdelen. sectie 1 = vanaf stuw tot ...m.  sectie 2 = vanaf ... tot .... m (duiker)
# Voor Dieuwke sectie1 = lengte_stuw_duiker / 2
#  We beginnen dus met sectie 1 en dan met de doorsnede net bovenstrooms van de stuw
#  Wat is hier de waterdiepte? (m)
#
sectie1 = lengte_stuw_duiker / 2
print(round(sectie1, decimalen_2))  # [18]

waterdiepte_stuw = waterstand_stuw - bodemhoogte_beneden;
print(round(waterdiepte_stuw, decimalen_2))  # [19]

# Vraag 41 Bereken de hydraulische straal R van deze doorsnede
# Gebruik 2 decimalen en m

oppervlak_watergang_stuw = ((bodembreedte + waterdiepte_stuw * taludhelling) * waterdiepte_stuw)
natte_omtrek_watergang_stuw = (bodembreedte + 2 * waterdiepte_stuw * (1 + taludhelling ** 2) ** 0.5)
hydraulische_straal_stuw = oppervlak_watergang_stuw / natte_omtrek_watergang_stuw
print(round(hydraulische_straal_stuw, decimalen_2))  # [20]

# Vraag 42 Bereken de gemiddelde snelheid in deze doorsnede
# Gebruik 2 decimalen en m/s
snelheid_watergang_stuw = (debiet / oppervlak_watergang_stuw)
print(round(snelheid_watergang_stuw, decimalen_2))  # [21]

# Vraag 43 bereken met Manning de helling van de energielijn ter plaats van de doorsnede net bovenstrooms van de stuw
# Gebruik 8 decimalen
energieverhang_watergang_stuw = (snelheid_watergang_stuw * coeff_manning / hydraulische_straal_stuw**(2/3))**(2)
print(round(energieverhang_watergang_stuw, decimalen_8))  # [22]

# Vraag 44 We nemen aan dat voor sectie 1 het verhang van de waterlijn (p.n.) gelijk is aan het energieverhang I en dat het energieverhang over sectie1 gelijk blijft.
# Wat is dan de stijging van de waterstand over de 150 m
# Gebruik 4 decimalen en vergeet de eenheid niet.
# NB 4 decimalen lijkt overdreven, maar bij een aantal opgaven is de stijging echt minimaal. So don't worry

stijging_waterstand_sectie1 = energieverhang_watergang_stuw * sectie1
print(round(stijging_waterstand_sectie1, decimalen_4))  # [23]

# Vraag 45 Wat wordt de waterstand halverwege de stuw en de duiker? (einde sectie 1)
# Gebruik 2 decimalen en mNAP
waterstand_halverwege = waterstand_stuw + stijging_waterstand_sectie1
print(round(waterstand_halverwege, decimalen_2))  # [24]

# Vraag 46 Bereken de bodemhoogte van de watergang halverwege de stuw en de duiker
# Gebruik 2 decimalen en mNAP
bodemhoogte_halverwege = sectie1 / bodemverhang + bodemhoogte_beneden
print(round(bodemhoogte_halverwege, decimalen_2))  # [25]

# Vraag 47 Bereken de waterdiepte halverwege de stuw en de duiker
# Gebruik 2 decimalen en m
waterdiepte_halverwege = waterstand_halverwege - bodemhoogte_halverwege
print(round(waterdiepte_halverwege, decimalen_2))  # [26]

# Vraag 48 Bereken de hydraulische straal R halverwege de stuw en de duiker
# Gebruik 2 decimalen en m
oppervlak_watergang_halverwege = ((bodembreedte + waterdiepte_halverwege * taludhelling) * waterdiepte_halverwege)
natte_omtrek_watergang_halverwege = (bodembreedte + 2 * waterdiepte_halverwege * (1 + taludhelling ** 2) ** 0.5)
hydraulische_straal_halverwege = oppervlak_watergang_halverwege / natte_omtrek_watergang_halverwege
print(round(hydraulische_straal_halverwege, decimalen_2))  # [27]

# Vraag 49 Bereken de gemiddelde snelheid in deze doorsnede
# Gebruik 2 decimalen en m/s
snelheid_watergang_halverwege = (debiet / oppervlak_watergang_halverwege)
print(round(snelheid_watergang_halverwege, decimalen_2))  # [28]

# Vraag 50 bereken met Manning de helling van de energielijn ter plaats van de doorsnede halverwege de stuw en de duiker
# Gebruik 8 decimalen
energieverhang_watergang_halverwege = (snelheid_watergang_halverwege * coeff_manning / hydraulische_straal_halverwege**(2/3))**(2)
print(round(energieverhang_watergang_halverwege, decimalen_8))  # [29]

# Vraag 51 We nemen aan dat voor sectie 2 het verhang van de waterlijn (p.n.) gelijk is aan het energieverhang I en dat het energieverhang over sectie2 gelijk blijft.
# Wat wordt de waterstand ter plaatse van de duiker?
# Gebruik 2 decimalen en mNAP
stijging_waterstand_sectie2 = energieverhang_watergang_halverwege * sectie1
waterstand_duiker = waterstand_halverwege + stijging_waterstand_sectie2
print(round(waterstand_duiker, decimalen_2))  # [30]


#")