from adgo_lib import kies_getal_stap
from WaterII.adgo_water_lib import water

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Een kanaal met een rechthoekige doorsnede heeft een breedte van 11 m. Het debiet bedraagt 10 m3/s.
# Bereken de kritische diepte hc
# Gebruik 2 decimalen en vergeet de eenheid niet

#sw_Python("
#versie 20-9-2023
#$adgo_lib
#$adgo_water_lib
from scipy.optimize import root

decimalen_2 = 2
print(decimalen_2)  # [0]

bodembreedte = kies_getal_stap(8.0, 12.5, 0.5, 1)
print(bodembreedte)  # [1]

debiet = kies_getal_stap(8,15,0.5,1)
print(debiet)  # [2]

# Vraag 15 Bereken de kritische diepte hc (m)
hc = (debiet ** 2 /(water.g * bodembreedte ** 2)) ** (1 /3)
print(round(hc, decimalen_2))  # [3]

# Vraag 16 Bereken de kritische snelheid vc (m/s)
vc = (water.g * hc) ** (1 /2)
print(round(vc, decimalen_2))  # [4]

# Vraag 17 Stel waterdiepte is ..... bereken de stroomsnelheid
waterdiepte = 1.4 * hc
print(round(waterdiepte, decimalen_2))  # [5]
stroomsnelheid = debiet / (bodembreedte * waterdiepte)
print(round(stroomsnelheid, decimalen_2))  # [6]

# Vraag 18 Bereken het getal van froude
froude = stroomsnelheid / vc
print(round(froude, decimalen_2))  # [7]

# vraag 19 Stel dat de Energiehoogte is
# In deze situatie kunnen 2 waterstanden optreden.
# Bij welke waterstand hebben we te maken met schietend water?
# Defining the function
H = 2 + hc
print(round(H, decimalen_2)) # [8]

def equation(y, H, Q, B):
    return y + (Q**2 / (20 * B**2)) * (1 / y**2) - H

# Finding the roots of the function using a range of initial guesses
y_schietend = root(equation, [0.01 , hc], args=(H, debiet, bodembreedte)).x

# Filtering only the positive roots
schietend = [y for y in y_schietend if 0 < y < hc]
print(round(schietend[0], decimalen_2))  # [9]

#vraag 20 Bij welke waterstand hebben we te maken met stromend water?
y_stromend = root(equation, (H - 0.01), args=(H, debiet, bodembreedte)).x
print(round(y_stromend[0], decimalen_2))  # [10]

#")