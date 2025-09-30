from adgo_lib import kies_getal_tussen, kies_getal_stap
from DWG.adgo_DWG_lib import water
import math


# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie



#sw_Python("
#versie 7-12-2023
#$adgo_lib
#$adgo_DWG_lib


decimalen = 2
print(decimalen) # [0]

golflengte = kies_getal_tussen(39, 60, 0)
print(round(golflengte,0))  # [1]

golfperiode = kies_getal_stap(5, 7, 0.1, 1)
print(round(golfperiode,1))  # [2]

waterdiepte = kies_getal_tussen(5, 10, decimalen)
print(round(waterdiepte, decimalen))  # [3]

#  vraag 7 Bereken de voortplantingssnelheid in m/s
voortplantingssnelheid = golflengte / golfperiode
print(round(voortplantingssnelheid, decimalen))  # [4]

# vraag 8 Bereken de grensdiepte diepwatergolf in m
grensdiepte = 0.5 * golflengte
print(round(grensdiepte, decimalen))  # [5]

# vraag 9 Geef een schatting van de golfhoogte H (m)  Als faktor mag je 3.8 aanhouden
golfhoogte = (golfperiode / 3.8) ** 2
print(round(golfhoogte, decimalen))  # [6]

# vraag 10 Wat zal de orbitale snelheid van een waterdeeltje aan het oppervlakte bij deze golf zijn, bij een waterdiepte van .. m.
# Als golflengte L mag je de golflengte van de diepwatergolf van .. m aanhouden. Dit is eigenlijk niet helemaal correct. In ondiepwater zal de golflengte korter worden.
# Gebruik 2 decimalen en m/s.
snelheidOppervlakte = (math.pi * golfhoogte / golfperiode) * (1 / math.tanh((2 * math.pi * waterdiepte) / golflengte))
print(round(snelheidOppervlakte, decimalen))  # [7]

# vraag 11 Wat zal de orbitale snelheid van een waterdeeltje aan de bodem bij deze golf zijn, bij een waterdiepte van .. m.
#  Gebruik 2 decimalen en m/s.
snelheidbodem = (math.pi * golfhoogte / golfperiode) * (1 / math.sinh((2 * math.pi * waterdiepte) / golflengte))
print(round(snelheidbodem, decimalen))  # [8]

# vraag 12 Hoeveel energie (Nm) bevat de golf?
# Gaat uit van zoutwater en een breedte van de golf van 100 m.
energieGolf = (1/8) * water.sgzout * water.g * 100 * golflengte * (golfhoogte ** 2)
print(round(energieGolf, decimalen))  # [9]

#")
