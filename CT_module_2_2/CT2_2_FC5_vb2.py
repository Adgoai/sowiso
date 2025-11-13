from adgo_lib import kies_integer_getal_stap, kies_getal_tussen, kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#Water stroomt met een constante snelheid van 0,5m/s van een smalle watergang naar een brede zandvang een schematisch bovenaanzicht van de situatie en 2 schematische dwarsprofielen zijn hierboven gegeven
# a. Bepaal het getal van Reynolds ‘Rew’ ter plaatse van de instromende watergang
# b. Bepaal het debiet in de zandvang
# c. Bepaal het getal van Reynolds ‘Rew’ ter plaatse van de zandvang
# d. Geef aan waar spraken is van turbulente stroming en waar van laminaire stroming
# e. Verklaar de term ‘zandvang’ op basis van de bovenstaande antwoorden

#sw_Python("
#versie 26-6-2025
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen) # [0]

snelheid = kies_getal_stap(0.4, 0.8, 0.1, decimalen)
print(snelheid) # [1]

bodem_1 = kies_getal_stap(0.4, 0.8, 0.1, decimalen)
print(bodem_1) # [2]

bodem_2 = kies_getal_stap(900, 1500, 100, decimalen)
print(bodem_2) # [3]

diepte = kies_getal_stap(0.8, 1.2, 0.1, decimalen)
print(diepte) # [4]

talud = 1
print(talud) # [5]

kine_visco = water.kin_visco
print(kine_visco) # [6]

# vraag a
A_1 = (bodem_1 + diepte) * diepte
O_1 = (2 * diepte)**2 + bodem_1
R_1 = A_1/O_1
print(round(R_1, decimalen)) # [7]

Re_1 = (snelheid * R_1) / kine_visco
print(round(Re_1, 0)) # [8]

# vraag b
debiet = snelheid * A_1
print(round(debiet, decimalen)) # [9]

# vraag c
A_2 = (bodem_2 + diepte) * diepte
O_2 = (2 * diepte)**2 + bodem_2
R_2 = A_2 / O_2
print(round(R_2, decimalen)) # [10]

significant = 3
snelheid_2 = debiet / A_2
v2_afgerond = float(f'{snelheid_2:.{significant}g}')
print(v2_afgerond) # [11]

Re_2 = (snelheid_2 * R_2) / kine_visco
print(round(Re_2, 0)) # [12]

if Re_2 < 400:
    print(1) # [13]
elif Re_2 > 900:
    print(2) # [13]
else:
    print(3) # [13]

#")