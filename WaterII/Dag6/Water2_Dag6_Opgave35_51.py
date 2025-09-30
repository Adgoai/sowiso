from adgo_lib import kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#De watergang heeft benedenstrooms een stuw (korte overlaat). De waterstand benedenstrooms van de stuw staat lager dan de kruin.
#De watergang heeft een bodemverhang, de doorsnede van de watergang is trapeziumvormig en is gelijk over de gehele lengte van de watergang. Ook het debiet blijft gelijk over de gehele lengte van de watergang.
#Halverwege is een duiker aanwezig, deze duiker ligt horizontaal en heeft een rechthoekige doorsnede.

#sw_Python("
#versie 6-10-2023
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

decimalen_4 = 4
print(decimalen_4)  # [1]

decimalen_8 = 8
print(decimalen_8)  # [2]

debiet = kies_getal_stap(5, 8, 0.1, 1)
print(debiet)  # [3]

lengte_stuw_duiker = kies_integer_getal_stap(300, 400, 10)
print(lengte_stuw_duiker)  # [4]

bodemverhang = kies_integer_getal_stap(1000, 5500, 500)
print(bodemverhang)  # [5]

bodemhoogte_beneden = kies_getal_stap(0.2, 0.4, 0.05,2)
print(bodemhoogte_beneden)  # [6]

bodembreedte = kies_getal_stap(2, 4, 0.2,1)
print(bodembreedte)  # [7]

taludhelling = kies_integer_getal_stap(1, 5, 1)
print(taludhelling)  # [8]

coeff_manning = kies_getal_stap(0.02, 0.05, 0.01,2)
print(coeff_manning)  # [9]

kruinhoogte_stuw = kies_getal_stap(1.0, 2.0, 0.1)
print(kruinhoogte_stuw)  # [10]

kruinbreedte_stuw = kies_getal_stap(1, 5, 0.2,1)
print(kruinbreedte_stuw)  # [11]

afvoercoeff_stuw = kies_getal_stap(2, 3, 0.1,1)
print(afvoercoeff_stuw)  # [12]

# Vraag 35 Bepaal de evenwichtsdiepte (m) bovenstrooms van de stuw (afgerond op 2 decimalen)
# oppervlak = ((bodembreedte + hevenwicht * taludhelling) * hevenwicht)
# natt_omtrek = (bodembreedte + 2 * hevenwicht * (1 + taludhelling ** 2) ** 0.5)
# hydraulische_straal = oppervlak / natt_omtrek
# gemiddelde_stroomsnelheid = (debiet / ((bodembreedte + hevenwicht * taludhelling) * hevenwicht))
# energieverhang = (gemiddelde_stroomsnelheid * coeff_manning / hydraulische_straal**(2/3))**(2)
# hydraulische_straal = (((bodembreedte + hevenwicht * taludhelling) * hevenwicht) / (bodembreedte + 2 * hevenwicht * (1 + taludhelling ** 2) ** 0.5))
# energieverhang = ((debiet / ((bodembreedte + hevenwicht * taludhelling) * hevenwicht)) * coeff_manning / (((bodembreedte + hevenwicht * taludhelling) * hevenwicht) / (bodembreedte + 2 * hevenwicht * (1 + taludhelling ** 2) ** 0.5))**(2/3))**(2)

from scipy.optimize import fsolve
energieverhang = 1 / bodemverhang
# Definiëren van de vergelijking
def equation(hevenwicht):
    left_side = (debiet / ((bodembreedte + hevenwicht * taludhelling) * hevenwicht))
    right_side = coeff_manning / (((bodembreedte + hevenwicht * taludhelling) * hevenwicht) / (bodembreedte + 2 * hevenwicht * (1 + taludhelling ** 2) ** 0.5))**(2/3)
    return (left_side * right_side)**2 - energieverhang

# Proberen met meerdere startwaarden
start_values = [0.1, 0.5]
solutions = []

for guess in start_values:
    try:
        solution, = fsolve(equation, guess)
        if solution > 0:  # Omdat hevenwicht positief moet zijn
            solutions.append(solution)
    except:
        continue

# Verwijderen van dubbele oplossingen (als die er zijn) en sorteren
unique_solutions = sorted(set(solutions))

# De oplossing afdrukken
hevenwicht = unique_solutions[0]
print(round(unique_solutions[0], decimalen_2))  # [13]

# Vraag 36 Bepaal vervolgens de kritische diepte (m) bovenstrooms van de stuw (afgerond op 2 decimalen)
# H = (3/2) * hkritisch
# H = hkritisch + v**2 / (2 * water.g)
# oppervlak = ((bodembreedte + hkritisch * taludhelling) * hkritisch)
# v = (debiet / ((bodembreedte + hkritisch * taludhelling) * hkritisch))
# (3/2) * hkritisch = hkritisch + (debiet / ((bodembreedte + hkritisch * taludhelling) * hkritisch))**2 / 20

# from scipy.optimize import fsolve
# Definiëren van de vergelijking voor hkritisch
def hkritisch_equation(hkritisch):
    return (3/2) * hkritisch - hkritisch - (debiet / ((bodembreedte + hkritisch * taludhelling) * hkritisch))**2 / 20

# Proberen met meerdere startwaarden
start_values = [0.1, 0.5]
hkritisch_solutions = []

for guess in start_values:
    try:
        solution, = fsolve(hkritisch_equation, guess)
        if solution > 0:  # Omdat hkritisch positief moet zijn
            hkritisch_solutions.append(solution)
    except:
        continue

# Verwijderen van dubbele oplossingen (als die er zijn) en sorteren
unique_hkritisch_solutions = sorted(set(hkritisch_solutions))

# De oplossing afdrukken
hkritisch = unique_hkritisch_solutions[0]
print(round(unique_hkritisch_solutions[0], decimalen_2))  # [14]

# Vraag 37 Is de stroming : stromend of schietend of kritisch?

if (hevenwicht > hkritisch):
    print('stromend')  # [15]
elif (hevenwicht < hkritisch):
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

#print (stijging_waterstand_sectie1)
#print (stijging_waterstand_sectie2)
#print (snelheid_watergang_stuw)
#print (snelheid_watergang_halverwege)


#")