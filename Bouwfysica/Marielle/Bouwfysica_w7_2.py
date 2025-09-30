from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 26-09-2024
#$adgo_lib
#$adgo_bouwfysica_lib


#Van de uitwendige scheidingsconstructies van een woning zijn de volgende gegevens bekend:
# Vloer: Rc = 4,3 m2K/W , oppervlakte = 85 m2  (variatie mogelijkheden: Rc vanaf 3,7 met stappen van 0,1 omhoog tot 5, oppervlakte van 70 tot 100 m2 met stappen van 5 m2, koppelen aan dak)
# Gevels (gesloten delen): Rc = 5,7  m2K/W , oppervlakte = 115 m2 (variatie mogelijkheden: Rc vanaf 4,7 met stappen van 0,1 omhoog tot 6, oppervlakte van 100 tot 130 m2 met stappen van 5 m2, koppelen aan dak)
# Dak: Rc = 7,0  m2K/W , oppervlakte = 85 m2 (variatie mogelijkheden: Rc vanaf 6,3 met stappen van 0,1 omhoog tot 8, oppervlakte van 70 tot 100 m2 met stappen van 5 m2, koppelen aan vloer)
#De vloer bevindt zich boven een kruipruimte.
#Bereken het totale transmissieverlies gedurende het stookseizoen (4000uur) door de gesloten delen (dus exclusief ramen, deuren etc). De gemiddelde binnen- en buitentemperatuur gedurende het stookseizoen is respectievelijk 18°C en 5°C.
# De weegfactor “a” is 1 behalve voor de begane grondvloer, dan is deze 0,7.

Rc_vloer = kies_getal_stap(3.7, 5, 0.1, 1)
oppervlakte_vloer = kies_getal_stap(70, 100, 5, 0)

Rc_gevels = kies_getal_stap(4.7, 6, 0.1, 1)
oppervlakte_gevels = kies_getal_stap(100, 130, 5, 0)

Rc_dak = kies_getal_stap(6.3, 8, 0.1, 1)
oppervlakte_dak = oppervlakte_vloer

stookseizoen = 4000
t_binnen = 18
t_buiten = 5
a_weeg = 1
a_vloer = 0.7

Rsi_vloer = 0.17 # m²K/W
Rse_vloer = 0.17 # m²K/W

Rsi_gevels = 0.13 # m²K/W
Rse_gevels = 0.04 # m²K/W

Rsi_dak = 0.10 # m²K/W
Rse_dak = 0.04 # m²K/W

#berekeningen
U_vloer = round(1 / (Rsi_vloer + Rse_vloer + Rc_vloer), 3)
U_gevels = round(1 / (Rsi_gevels + Rse_gevels + Rc_gevels),3)
U_dak = round(1 / (Rsi_dak + Rse_dak + Rc_dak), 3)

Q_vloer = round(a_vloer * oppervlakte_vloer * U_vloer * (stookseizoen / 1000) * (t_binnen - t_buiten),0)

Q_gevels = round(a_weeg * oppervlakte_gevels * U_gevels * (stookseizoen / 1000) * (t_binnen - t_buiten),0)

Q_dak = round(a_weeg * oppervlakte_dak * U_dak * (stookseizoen / 1000) * (t_binnen - t_buiten),0)

Q_totaal = round(Q_vloer + Q_gevels + Q_dak, 0)

print(Rc_vloer) # [0]
print(oppervlakte_vloer) # [1]
print(Rc_gevels) # [2]
print(oppervlakte_gevels) # [3]
print(Rc_dak) # [4]
print(oppervlakte_dak) # [5]
print(stookseizoen) # [6]
print(t_binnen) # [7]
print(t_buiten) # [8]
print(a_weeg) # [9]
print(a_vloer) # [10]
print(Rsi_vloer) # [11]
print(Rse_vloer) # [12]
print(Rsi_gevels) # [13]
print(Rse_gevels) # [14]
print(Rsi_dak) # [15]
print(Rse_dak) # [16]
print(U_vloer) # [17]
print(U_gevels) # [18]
print(U_dak) # [19]
print(Q_vloer) # [20]
print(Q_gevels) # [21]
print(Q_dak) # [22]
print(Q_totaal) # [23]


# Opgave b

#MC in sowioso

#")
