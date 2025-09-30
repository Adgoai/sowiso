from adgo_lib import kies_getal_stap, kies_integer_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# In deze opgave ga je de formules voor watergangen (Manning) en overlaten combineren. Hierbij nemen we nog steeds aan dat bodemverhang en energieverhang gelijk zijn.
# De theorie nodig voor het oplossen van het vraagstuk zal je vooral vinden bij dag 2 Bernoulli, dag 3 dimensioneren van watergangen en dag 4 Overlaten en stuwen
# # De watergang is trapeziumvormig en heeft een bodembreedte van  4 m, het talud aan beide zijden is 1:2.
# Lengte van de watergang is 839 km. Benedenstrooms is er een korte overlaat aanwezig.
# Het debiet bedraagt 7,8  m3/s en is over de gehele lengte gelijk.
# Waterdiepte is 2,3 m en is over de gehele lengte tot aan de overlaat gelijk, achter de overlaat is de waterstand lager dan de kruinhoogte.
# De coëfficiënt van Manning n is 0,012 s/m1/3
# Breedte van de korte overlaat is  4 m, afvoercoëfficiënt c = 1,9 m1/2/s
# In deze opgave ga je uiteindelijk de bodemhelling bereken en de kruinhoogte van de stuw.

#sw_Python("
#versie 27-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

decimalen_8 = 8
print(decimalen_8)  # [1]

bodembreedte = kies_getal_stap(2,8, 0.5,1)
print(bodembreedte)  # [2]

talud = kies_integer_getal_stap(1, 5, 1) # 1 : ......
print(talud)  # [3]

waterdiepte = kies_getal_stap(2, 4, 0.1, 1)
print(waterdiepte)  # [4]

lengte = kies_integer_getal_stap(800,1500, 50)
print(lengte)  # [5]

debiet = kies_getal_stap(1, 3, 0.1, 1)
print(debiet)  # [6]

coefficient_Manning = kies_getal_stap(0.01, 0.03, 0.005, 3)
print(coefficient_Manning)  # [7]

breedte_stuw = kies_getal_stap(2, 6, 0.5, 1)
print(breedte_stuw)  # [8]

afvoercoefficient = kies_getal_stap(1, 2, 0.1, 1)
print(afvoercoefficient)  # [9]

# Vraag 21 Bereken de hydraulische straal R in de watergang bovenstrooms van de overlaat. (m) (2 decimalen)
opp = (bodembreedte + waterdiepte * talud) * waterdiepte
natt_omtrek = bodembreedte + 2 * waterdiepte * (1 + talud ** 2) ** 0.5
hydraulische_straal = opp / natt_omtrek
print(round(hydraulische_straal, decimalen_2 ))  # [10]

# Vraag 22 Bereken de gemiddelde stroomsnelheid in de watergang bovenstrooms van de overlaat. (m/s) (2 decimalen)
gemiddelde_stroomsnelheid = debiet / opp
print(round(gemiddelde_stroomsnelheid, decimalen_2 ))  # [11]

# Vraag 23 Bereken het energieverhang met de formule van Manning. (m/m) (8 decimalen)
energieverhang = (gemiddelde_stroomsnelheid * coefficient_Manning / hydraulische_straal**(2/3))**(2)
print(round(energieverhang, decimalen_8 ))  # [12]

# Vraag 24 Wat wordt de stijging van de bodem over de lengte van de watergang? (m) (2 decimalen)
stijging_bodem = energieverhang * lengte
print(round(stijging_bodem, decimalen_2 ))  # [13]

# Vraag 25 Je gaat nu de kruinhoogte van de overlaat tov van de bodem van de watergang berekenen. Dit gaat in drie stappen
# Stap 1: Bereken de Energiehoogte H ter plaatse de stuw tov de bodem van de watergang
# Gebruik 2 decimalen en vergeet de eenheid niet
Energiehoogte_watergang = waterdiepte + gemiddelde_stroomsnelheid**2 / (2 * water.g)
print(round(Energiehoogte_watergang, decimalen_2 ))  # [14]

# Stel dat de waterstand benedenstooms van de stuw lager is dan de kruin van de stuw?
# Vraag 26 gaat het om een volkomen of onvolkomen stuw

# Vraag 27 stap 2 Berekeken de energiehoogte boven de kruin van de stuw. (m) (2 decimalen)
energiehoogte_boven_kruin = (debiet / (afvoercoefficient * breedte_stuw))**(2/3)
print(round(energiehoogte_boven_kruin, decimalen_2 ))  # [15]

# Vraag 28 stap 3 Bereken de kruinhoogte van de stuw, gemeten tov de bodem van de watergang. (m) (2 decimalen)
hoogte_stuw = Energiehoogte_watergang - energiehoogte_boven_kruin
print(round(hoogte_stuw, decimalen_2 ))  # [16]

# Vraag 29 We gaan aantonen dat we met met stromend water te maken hebben, daarvoor ga je het getal van froude berekenen.
# Wat is e gemiddelde breedte van de watergang? (m) (2 decimaal)
gemiddelde_breedte = bodembreedte + waterdiepte * talud
print(round(gemiddelde_breedte, decimalen_2 ))  # [17]

# Vraag 30 Bereken de kritische diepte van de watergang. (m) (2 decimalen)
kritische_diepte = (debiet**2 / (water.g * gemiddelde_breedte**2))**(1/3)
print(round(kritische_diepte, decimalen_2 ))  # [18]

# Vraag 31 Bereken het getal van Froude. (2 decimalen)
kritische_stroomsneldheid = (water.g * kritische_diepte)**0.5
getal_froude = gemiddelde_stroomsnelheid / kritische_stroomsneldheid
print(round(getal_froude, decimalen_2 ))  # [19]

# Vraag 32 multiple choice

# Vraag 33 Je gaat nu het kritische bodemverhang berekenen op basis van Manning.
# Hierbij is de evenwichtsdiepte gelijk aan de kritische diepte. De hc en vc heb je al eerder berekend#
# Bereken eerst de hydraulische straal R (m) (2 decimalen)
# Ik ga weer uit vah het trapeziumvormige profiel
kritisch_opp = (bodembreedte + kritische_diepte * talud) * kritische_diepte
kritisch_natte_omtrek = bodembreedte + 2 * kritische_diepte * (1 + talud ** 2) ** 0.5
kritisch_hydraulische_straal = kritisch_opp / kritisch_natte_omtrek
print(round(kritisch_hydraulische_straal, decimalen_2 ))  # [20]

# Vraag 34 Bereken het kritische bodemverhang. (m/m) (7 decimalen)
kritisch_bodemverhang = (gemiddelde_stroomsnelheid * coefficient_Manning / kritisch_hydraulische_straal**(2/3))**(2)
print(round(kritisch_bodemverhang, decimalen_8 ))  # [21]

#")