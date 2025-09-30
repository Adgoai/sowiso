from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap
from DWG.adgo_DWG_lib import water
import math

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso.
#

#sw_Python("
#versie 21-02-2024
#$adgo_lib
#$adgo_DWG_lib

decimalen = 2
print(decimalen) # [0]

Gdroog = kies_integer_getal_stap(15, 23, 1)
print(Gdroog) # [1]

Gnat = Gdroog * 1.05
print(round(Gnat,2)) # [2]

Cohesie = kies_integer_getal_stap(2, 10, 1)
print(Cohesie) # [3]

inwendige_wrijvingshoek = kies_getal_stap(30, 45, 1, 1)
print(inwendige_wrijvingshoek) # [4]


# opgave 2 Bereken de grensa
grensa =abs(45 - 0.5 * inwendige_wrijvingshoek)
print(round(grensa, decimalen))  # [5]

# opgave 3 We gaan uit van één meter dijk.
# Wat wordt de verticale kracht van het gedeelte grond boven het grondwater.
# kN per meter dijk
lamel7bovenGrondwater = 23.9 * Gdroog
print(round(lamel7bovenGrondwater, decimalen)) # [6]

# opgave 4 Wat wordt de verticale kracht van het gedeelte grond onder het grondwater.
# kN per meter dijk
lamel7onderGrondwater = 0.6 * (Gnat - 10)
print(round(lamel7onderGrondwater, decimalen)) # [7]

# opgave 5 Wat wordt de arm voor lamel 7. (m)
lamel7arm = 14.45
print(round(lamel7arm, decimalen)) # [8]

# opgave 6 Wat wordt het aandrijvende moment voor lamel 7 (kNm)
lamel7aandrijvend = (lamel7bovenGrondwater + lamel7onderGrondwater) * lamel7arm
print(round(lamel7aandrijvend, decimalen)) # [9]

# opgave 7 Wat wordt de gemiddelde afstand tussen maaiveld en grondwaterstand? (m)
lamel7afstandTotGrondwaterDroog = 4.88
print(round(lamel7afstandTotGrondwaterDroog, decimalen)) # [10]

# opgave 8 Wat wordt de gemiddelde afstand tussen circke en grondwaterstand? (m)
lamel7afstandTotGrondwaterNat = 0.12
print(round(lamel7afstandTotGrondwaterNat, decimalen)) # [11]

# opgave 9 Wat wordt de grondspanning ter plaatse van de cirkel? (kPa of kN/m2)
lamel7grondspanning = 4.88 * Gdroog + 0.12 * Gnat
print(round(lamel7grondspanning, decimalen)) # [12]

# opgave 10 Wat wordt de waterspanning ter plaatse van de cirkel? (kPa of kN/m2)
lamel7waterspanning = 0.12 * 10
print(round(lamel7waterspanning, decimalen)) # [13]

# opgave 11 Wat wordt de korrelspanning ter plaatse van de cirkel? (kPa of kN/m2)
lamel7korrelspanning = lamel7grondspanning - lamel7waterspanning
print(round(lamel7korrelspanning, decimalen)) # [14]

# opgave 12 Moet voor lamel 7 bij het berekenen van de toelaatbare schuifspanning gerekend worden met de werkelijke α of met de grens α?
#   geen python code

# opgave 13 Wat wordt de toelaatbare schuifspanning ter plaatse van lamel7? (kPa of kN/m2)
lamel7toelaatbareSchuifspanning = (math.sin(math.radians(inwendige_wrijvingshoek)) * math.cos(math.radians(-grensa)) / math.cos(math.radians(inwendige_wrijvingshoek - grensa))) * (lamel7korrelspanning + Cohesie / math.tan(math.radians(inwendige_wrijvingshoek)))
print(round(lamel7toelaatbareSchuifspanning, decimalen)) # [15]

# opgave 14 Wat wordt de toelaatbare schuifkracht ter plaatse van lamel 7? (kN)
lamel7toelaatbareSchuifkracht = lamel7toelaatbareSchuifspanning * 9.6
print(round(lamel7toelaatbareSchuifkracht, decimalen)) # [16]

# opgave 15 Wat wordt het stabiliserende moment voor lamel 7? (kNm)
lamel7stabiliserend = lamel7toelaatbareSchuifkracht * 17.5
print(round(lamel7stabiliserend, decimalen)) # [17]

# opgave 16 We gaan uit van één meter dijk. lamel3
# Wat wordt de verticale kracht van het gedeelte grond boven het grondwater.
# kN per meter dijk
lamel3bovenGrondwater = 10.2 * Gdroog
print(round(lamel3bovenGrondwater, decimalen)) # [18]

# opgave 17 Wat wordt de verticale kracht van het gedeelte grond onder het grondwater.
# kN per meter dijk
lamel3onderGrondwater = 23.0 * (Gnat - 10)
print(round(lamel3onderGrondwater, decimalen)) # [19]

# opgave 18 Wat wordt de arm voor lamel 3. (m)
lamel3arm = 2.0
print(round(lamel3arm, decimalen)) # [20]

# opgave 19 Wat wordt het aandrijvende moment voor lamel 3 (kNm)
lamel3aandrijvend = (lamel3bovenGrondwater + lamel3onderGrondwater) * lamel3arm
print(round(lamel3aandrijvend, decimalen)) # [21]

# opgave 20 Wat wordt de gemiddelde afstand tussen maaiveld en grondwaterstand? (m)
lamel3afstandTotGrondwaterDroog = 10.2 / 4
print(round(lamel3afstandTotGrondwaterDroog, decimalen)) # [22]

# opgave 21 Wat wordt de gemiddelde afstand tussen circke en grondwaterstand? (m)
lamel3afstandTotGrondwaterNat = 23.0 / 4
print(round(lamel3afstandTotGrondwaterNat, decimalen)) # [23]

# opgave 22 Wat wordt de grondspanning ter plaatse van de cirkel? (kPa of kN/m2)
lamel3grondspanning = lamel3afstandTotGrondwaterDroog * Gdroog + lamel3afstandTotGrondwaterNat * Gnat
print(round(lamel3grondspanning, decimalen)) # [24]

# opgave 23 Wat wordt de waterspanning ter plaatse van de cirkel? (kPa of kN/m2)
lamel3waterspanning = lamel3afstandTotGrondwaterNat * 10
print(round(lamel3waterspanning, decimalen)) # [25]

# opgave 24 Wat wordt de korrelspanning ter plaatse van de cirkel? (kPa of kN/m2)
lamel3korrelspanning = lamel3grondspanning - lamel3waterspanning
print(round(lamel3korrelspanning, decimalen)) # [26]

# opgave 25 Moet voor lamel 3 bij het berekenen van de toelaatbare schuifspanning gerekend worden met de werkelijke α of met de grens α?
#   geen python code

# opgave 26 Wat wordt de toelaatbare schuifspanning ter plaatse van lamel3? (kPa of kN/m2)
lamel3toelaatbareSchuifspanning = (math.sin(math.radians(inwendige_wrijvingshoek)) * math.cos(math.radians(6.6)) / math.cos(math.radians(inwendige_wrijvingshoek + 6.6))) * (lamel3korrelspanning + Cohesie / math.tan(math.radians(inwendige_wrijvingshoek)))
print(round(lamel3toelaatbareSchuifspanning, decimalen)) # [27]

# opgave 27 Wat wordt de toelaatbare schuifkracht ter plaatse van lamel 3? (kN)
lamel3toelaatbareSchuifkracht = lamel3toelaatbareSchuifspanning * 4
print(round(lamel3toelaatbareSchuifkracht, decimalen)) # [28]

# opgave 28 Wat wordt het stabiliserende moment voor lamel 3? (kNm)
lamel3stabiliserend = lamel3toelaatbareSchuifkracht * 17.5
print(round(lamel3stabiliserend, decimalen)) # [29]

#")
