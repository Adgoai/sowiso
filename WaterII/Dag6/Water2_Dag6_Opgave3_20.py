from adgo_lib import kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# In de volgende opgaven ga je het volgende gebied bestuderen. Het rekenen aan stuwen en optredende waterstanden
# in watergangen oefenen jullie al voldoende in andere opgaven. Daarom ligt bij deze opgave de nadruk op optimale
# waterstanden, pompcapaciteit en berging (bodem en oppervlaktewater)

#sw_Python("
#versie 15-12-2023
#$adgo_lib
#$adgo_water_lib

decimalen_2 = 2
print(decimalen_2)  # [0]

decimalen_3 = 3
print(decimalen_3)  # [1]

lengteA = kies_integer_getal_stap(350, 460, 10)
print(lengteA)  # [2]

breedteA = kies_integer_getal_stap(150, 260, 10)
print(breedteA)  # [3]

lengteC = lengteA + kies_integer_getal_stap(70, 160, 10)
print(lengteC)  # [4]

breedteC = breedteA
print(breedteC)  # [5]

breedteHoofdWatergang = kies_integer_getal_stap(5, 10, 1)
print(breedteHoofdWatergang)  # [6]

breedteOverigeWatergangen = kies_integer_getal_stap(2, 5, 1)
print(breedteOverigeWatergangen)  # [7]

maaiveldhoogteA = kies_getal_stap(4.0, 4.4, 0.1, 1)
print(maaiveldhoogteA)  # [8]

maaiveldhoogteB = kies_getal_stap(3.0, 4.7, 0.1, 1)
print(maaiveldhoogteB)  # [9]

maaiveldhoogteC = kies_getal_stap(4.3, 4.7, 0.1, 1)
print(maaiveldhoogteC)  # [10]

maaiveldhoogteD = kies_getal_stap(3.3, 3.7, 0.1, 1)
print(maaiveldhoogteD)  # [11]

bergingscoefficient = kies_getal_stap(0.15, 0.30, 0.05, 2)
print(bergingscoefficient)  # [12]

afvoernorm = kies_integer_getal_stap(10, 18, 1)
print(afvoernorm)  # [13]

neerslagintensiteit = kies_integer_getal_stap(15, 25, 1)
print(neerslagintensiteit)  # [14]

lengteGebied = 2 * lengteA + breedteOverigeWatergangen

lengteD = lengteGebied - lengteC - breedteOverigeWatergangen

breedteGebied = breedteA + breedteC + breedteHoofdWatergang + 2 * breedteOverigeWatergangen

brutoOppervlakteGebied = lengteGebied * breedteGebied

OppervlakteWater = 2 * lengteGebied * breedteOverigeWatergangen + lengteGebied * breedteHoofdWatergang + breedteA * breedteOverigeWatergangen + breedteC * breedteOverigeWatergangen

#Vraag 3 Bereken de lengte van Perceel D (m) 0 decimalen
#In tegenstelling tot de moodle opgave is de totale lengte van het gebied gegeven.
#ook zijn de breedte van de watergangen gegeven, dat was bij moodle niet het geval
print(round(lengteD, 0))  # [15]

#Vraag 4 Bereken het totale bruto oppervlak van het gebied (m2) 0 decimalen
print(round(brutoOppervlakteGebied, 0))  # [16]

#Vraag 5 Bereken het totale oppervlak van de watergangen (m2) 0 decimalen
#Omdat nu de afmetingen van de watergangen gegeven zijn, kan je het oppervlak van de watergangen berekenen.
#In moodle ging het andersom, het percentage was wel bekend, de afmetingen van de watergangen niet.
print(round(OppervlakteWater, 0))  # [17]

#Vraag 6 Bereken het percentage water in het gebied tov het totale bruto oppervlak (%) 2 decimalen
percentage_water = (OppervlakteWater / brutoOppervlakteGebied) * 100
print(round(percentage_water, decimalen_2))  # [18]

#Vraag 7 Bereken de afvoercapaciteit van het gemaal (m3/s), 3 decimalen
afvoercapaciteit_gemaal = (afvoernorm / 1000) * brutoOppervlakteGebied / (24 * 3600)
print(round(afvoercapaciteit_gemaal, decimalen_3))  # [19]

#Vraag 8 Wat is het oppervlakte van het gebied waarvan de neerslag over stuw 1 wordt afgevoerd? (m2) 0 decimalen
#Wellicht als extra informatie toevoegen dat de drainage evenwijdig aan de breedte van het gebied loopt.
#We nemen dus aan dat er geen water van het land afstroomt naar de watergangen tussen perceel A en B en tussen perceel C en D.
oppervlakte_stuw1 = lengteGebied * (breedteA / 2 ) + lengteGebied * breedteOverigeWatergangen + (breedteA / 2) * breedteOverigeWatergangen
print(round(oppervlakte_stuw1, 0))  # [20]

#Vraag 9 Wat wordt de afvoer over stuw 1 Bij een continue neerslag van .... mm/dag (m3/s) 3 decimalen
afvoer_stuw1 = (neerslagintensiteit / 1000) * oppervlakte_stuw1 / (24 * 3600)
print(round(afvoer_stuw1, decimalen_3))  # [21]

#Vraag 10 Wat wordt de afvoer over stuw 3 Bij een continue neerslag van .... mm/dag (m3/s) 3 decimalen
oppervlakte_stuw3 = lengteGebied * (breedteC / 2 ) +  lengteGebied  * breedteOverigeWatergangen + (breedteC / 2) * breedteOverigeWatergangen
afvoer_stuw3 = (neerslagintensiteit / 1000) * oppervlakte_stuw3 / (24 * 3600)
print(round(afvoer_stuw3, decimalen_3))  # [22]

#Vraag 11 Wat wordt de afvoer over stuw 2 Bij een continue neerslag van .... mm/dag (m3/s) 3 decimalen
#Wat het ingewikkeld maakt is dat de stuw niet echt aan het einde van perceel C ligt.
#Ik heb nu aangenomen dat de helft van perceel C afstroomt op de hoofdwatergang en over stuw 2 gaat.
#En dat van perceel B er geen water over stuw 2 gaat.
oppervlakte_stuw2 = (breedteC / 2) * lengteC + (breedteA / 2) * lengteA + lengteC * breedteOverigeWatergangen
afvoer_stuw2 = afvoer_stuw1 + (neerslagintensiteit / 1000) * oppervlakte_stuw2 / (24 * 3600)
print(round(afvoer_stuw2, decimalen_3))  # [23]

#Vraag 12 Voor perceel B wordt aangehouden dat de ideale drooglegging 100 cm bedraagt. Wat wordt op basis hiervan de kruinhoogte van stuw 1 tov NAP. (m) 2 decimalen
kruinhoogte_stuw1 = maaiveldhoogteB - 1.0
print(round(kruinhoogte_stuw1, decimalen_2))  # [24]

#Bij een hevige neerslag wordt  91 mm neerslag gemeten gedurende 4 dagen.
#Stel dat 80% van de neerslag na 4 dagen naar het grondwater en oppervlaktewater afstroomt.
#Stel dat tijdens deze neerslag het gemaal 70% van de tijd pompt.
#Stel dat oppervlaktewater en grondwater gelijkmatig stijgen.
#Stel dat de taluds van de watergangen verticaal zijn.
#Stel dat de bergingscoefficient %bergingscoefficient bedraagt.

#Vraag 13 Wat is het totale netto oppervlak (dus geen water) van het gebied (m2) 0 decimalen
netto_oppervlak = brutoOppervlakteGebied - OppervlakteWater
print(round(netto_oppervlak, 0))  # [25]

# Vraag 14 Stap 1 Hoeveel m2 oppervlaktewater geeft dezelfde stijging als het totale landoppervlakte?
equivalent_oppervlak = netto_oppervlak * bergingscoefficient
print(round(equivalent_oppervlak, 0))  # [26]

# Vraag 15 Stap 2 Wat wordt het totale oppervlak aan water (m2) 0 decimalen
totaal_opp_water = equivalent_oppervlak + OppervlakteWater
print(round(totaal_opp_water, 0))  # [27]

# Vraag 16 Stap 3 Wat is de totale hoeveelheid neerslag na de bui van 91 mm in 4 dagen (m3) 0 decimalen
neerslag_volume = brutoOppervlakteGebied * (91 / 1000)
print(round(neerslag_volume, 0))  # [28]

# Vraag 17 Stap 4 Hoeveel m3 stroomt er daadwerkelijk naar het grondwater en opervlaktewater? 0 decimalen
afvoer_volume = neerslag_volume * 0.8
print(round(afvoer_volume, 0))  # [29]

# Vraag 18 Stap 5 Hoeveel m3 water wordt er door het gemaal gedurende de 4 dagen verpompt? 0 decimalen
verpompt_volume = afvoercapaciteit_gemaal * 0.7 * 4 * 24 * 3600
print(round(verpompt_volume, 0))  # [30]

# Vraag 19 Stap 6 Hoeveel m3 water blijft er over om te bergen in het gebied? 0 decimalen
bergings_volume = afvoer_volume - verpompt_volume
print(round(bergings_volume, 0))  # [31]

# Vraag 20 Stap 7 Wat wordt nu de stijging in zowel het grondwater als het oppervlaktewater. (m) 2 decimalen
stijging = bergings_volume / totaal_opp_water
print(round(stijging, decimalen_2))  # [32]

#")