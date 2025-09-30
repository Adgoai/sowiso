from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 04-09-2024
#$adgo_lib
#$adgo_bouwfysica_lib

# In een woning is het ventilatiedebiet 270 m3/h. (variatie van 180 tot 320 met stappen van 20).

delta_t = 13 # K
stookseizoen = 4000 # h

Q_ventilatie = kies_integer_getal_stap(180, 320, 20)

dichtheid_lucht = 1.25 # kg/m3
c_lucht = 1000 # J/kgK

volume_woning = round(0.75 * Q_ventilatie / 5) * 5 # m3 afgerond op 5 m3

ventilatievoud = round(volume_woning / Q_ventilatie,2) # 1/h

Q_ventilatie_dm3_s = round(Q_ventilatie / 3.6, 0) # dm3/s

#warmteverlies door ventilatie
Q_ventilatie_W = round(dichtheid_lucht *c_lucht * Q_ventilatie_dm3_s * delta_t * (stookseizoen / 1000000), 0)

print(Q_ventilatie) # [0]
print(delta_t) # [1]
print(stookseizoen) # [2]
print(dichtheid_lucht) # [3]
print(c_lucht) # [4]
print(volume_woning) # [5]
print(ventilatievoud) # [6]
print(Q_ventilatie_dm3_s) # [7]
print(Q_ventilatie_W) # [8]

#")
