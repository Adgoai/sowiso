from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 7-1-2025
#$adgo_lib
#$adgo_bouwfysica_lib

# We bekijken een simpele gevelconstructie bestaande uit kalkzandsteen + isolatie. We negeren de afwerkingen aan
# binnen- en buitenkant. De gevelconstructie bestaat uit 100mm kalkzandsteen en
# 100mm isolatiemateriaal met een λ-waarde van 0,04 W/mK.

dikte_kalkzandsteen = 100 # mm
dikte_kalkzandsteen_m = dikte_kalkzandsteen / 1000 # m
dikte_isolatie = 100 # mm
dikte_isolatie_m = dikte_isolatie / 1000 # m
lambda_isolatie = 0.04 # W/mK

# a. Wat is de warmtegeleidingscoëfficient van kalkzandsteen? (opzoeken).
lambda_kalkzandsteen = 0.9 # W/mK
afwijkingsfactor = 0.05 # 5%

# b. Bereken de R van beide lagen
R_kalkzandsteen = round(dikte_kalkzandsteen_m / lambda_kalkzandsteen, 2)
R_isolatie = round(dikte_isolatie_m / lambda_isolatie, 2)

# c Bereken de U-waarde van de linker constructie o.b.v. Riso en Rkzs.
R_tot = R_kalkzandsteen + R_isolatie + 0.04 # 0.04 is de overgangsweerstand
U_waarde = round(1 / R_tot, 2)

# d. Wat is de U-waarde van de rechter constructie?

# e. Geef voor beide situaties een schatting van de temperatuur op het scheidingsvlak, aangegeven met een pijl.
t_links = 2 # °C
t_rechts = 18 # °C

# f. Bij welke van de twee onderstaande pijlen (1 of 2) zal de temperatuur in de winter het laagst zijn? Leg uit waarom.
# MC vraag in sowiso

print([lambda_kalkzandsteen, dikte_kalkzandsteen, dikte_isolatie, lambda_isolatie, lambda_kalkzandsteen, afwijkingsfactor,
       R_kalkzandsteen, R_isolatie, U_waarde, t_links, t_rechts])

#")
