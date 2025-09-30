from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 12-6-2024
#$adgo_lib
#$adgo_bouwfysica_lib

decimalen = 0
print(decimalen) # [0]

Qtransmissie = kies_getal_stap(4000, 6000, 100) # kWh
Qventilatie = kies_getal_stap(2000, 3000, 100) # kWh
Qzon = kies_getal_stap(3000, 5000, 100) # kWh

print(Qtransmissie) # [1]
print(Qventilatie) # [2]
print(Qzon) # [3]

a = 0.91
b = 0.76

# vraag 1 wat is de warmtebehoefte van de woning
# Qinstallatie = warmtebehoefte woning (WB) = a x (Qtransmissie + Qventilatie) – b x (Qzon + Qiw) =
WB = round(a * (Qtransmissie + Qventilatie) - b * Qzon, 0) # kWh
print(WB) # [4]

# vraag 2 wat is het gasverbruik van de woning
# (warmtebehoefte x 3,6)/(35,17 x rendement)

rendement = 0.85
gasverbruik = round((WB * 3.6) / (35.17 * rendement),0) # m³

print(rendement) # [5]
print(gasverbruik) # [6]

#")
