from adgo_lib import kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# De rechthoekige goot heeft een breedte (b) van 2,3 m. De waterdiepte is 0,5 m.
# De gemiddelde stroomsnelheid (u)  bedraagt 3,3 m/s.
# bereken debiet

#Stel nu dat het debiet gelijk blijft en ook de waterdiepte.
#Hoe breed moet het kanaal worden om de stroomsnelheid te verlagen tot 2,85 m/s.


#sw_Python("
#versie 6-9-2023
#$adgo_lib
#$adgo_water_lib

decimalen = 2
print(decimalen)  # [0]

breedte = kies_getal_stap(1, 3, 0.1, 1)
print(breedte)  # [1]

diepte = 0.5
print(diepte)  # [2]

stroomsnelheid = kies_getal_stap(0.5, 2, 0.1, 1)
print(stroomsnelheid)  # [3]

faktor = kies_getal_stap(0.2, 0.7, 0.1, 1)
nieuwe_stroomsnelheid = stroomsnelheid * faktor
print(round(nieuwe_stroomsnelheid,1))  # [4]

# Vraag 10 Bereken het debiet. Gebruik 2 decimalen, eenheid = m3/s
debiet = breedte * diepte * stroomsnelheid
print(round(debiet, decimalen))  # [5]

# Vraag 11 Bereken de nieuwe breedte. Gebruik 2 decimalen, eenheid = m
nieuwe_breedte = debiet / (diepte * nieuwe_stroomsnelheid)
print(round(nieuwe_breedte, decimalen))  # [6]

#")