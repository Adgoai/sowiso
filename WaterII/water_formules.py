#uitwerking van formules die in de opgaven gebruikt worden
import math

from adgo_lib import kies_getal_stap, kies_integer_getal_stap
from WaterII.adgo_water_lib import water
import numpy as np

from scipy.optimize import root, fsolve

g = water.g

print ("De meest gebruikte formules uit de opgaven bij vloeistofmechanica")

print("Oppervlakte cirkel")
diameter = kies_getal_stap(0.1, 2.0, 0.1, 1)
oppervlak = 0.25 * 3.14159 * diameter**2
print(round(oppervlak, 7))

print("Diameter cirkel")
oppervlak = kies_getal_stap(0.1, 2.0, 0.1, 1)
diameter = (oppervlak / (0.25 * 3.14159))**0.5
print(round(diameter, 2))

print("Natte omtrek cirkel")
natteOmtrek = math.pi * diameter
print(round(natteOmtrek, 4))



print("Debiet over een korte volkomen overlaat")
afvoercoeff = kies_getal_stap(1.1, 1.9, 0.1, 1)
breedte = kies_getal_stap(1.5, 5.0, 0.5, 1)
H_specifiek = kies_getal_stap(0.3, 1.0, 0.1, 1)
debiet = afvoercoeff * breedte * H_specifiek**1.5
print(round(debiet, 3)) # [4]


print("Formule van Darcy Weisbach")
lambdaCT = kies_getal_stap(0.02, 0.08, 0.01, 2)
lengte = kies_getal_stap(100, 1000, 100, 0)
hydraulischeStraal = kies_getal_stap(0.5, 2.5, 0.5, 1)
stroomsnelheid = kies_getal_stap(0.5, 2.0, 0.5, 1)
wrijvingsverlies = lambdaCT * (lengte / (4 * hydraulischeStraal)) * (stroomsnelheid**2 / (2 * g))
print(round(wrijvingsverlies, 3))




#Debiet H over een korte volkomen overlaat
afvoercoefficint = 1.1
breedte = 1.5
H_specifiek = 0.4
debiet = 0.584

debiet = afvoercoefficint * breedte * H_specifiek**1.5

H_specifiek = (debiet / (afvoercoefficint * breedte))**(1/1.5)

#formule van darcy weisbach
Lambda = 0.02
L = 100
R = 1.5
V = 1.5

Wrijvingsverlies = Lambda * (L / (4 * R)) * (V**2 / (2 * g))

V = ((2 * g * Wrijvingsverlies * 4 * R) / (Lambda * L))**0.5

#formule van manning
n = 0.015
R = 1.5
S = 0.0005

#C = R**(1/6) / n
V = (1 / n) * R**(2/3) * S**(1/2)
#print(V)
S = (V * n / R**(2/3))**2
#print(S)

#formule van chezy
C = 50
R = 1.5
S = 0.0005

V = C * (R * S)**(1/2)
#print(V)

S = (V / C)**2 / R
#print(S)

#Coefficient van Chezy
kinematische_viscositeit = 1.3 * 10**-6
R = 1.5
S = 0.0005
k = 2
#laminaire_grenslaag = 12 * kinematische_viscositeit / (g * R * S)**0.5

#C bij hydraulisch ruwe buis
C = 18 * np.log10(12 * R / (k / 1000))
#print(C)

# Getal van Reynolds
decimalen = 0
v = kies_getal_stap(0.2,4.0, 0.1, 1)
kinv = 10**-6
#print(kinv)

Re = v * R / kinv
#print(round(Re,decimalen))


print ("Stromend en schietend water bij gegeven H, Q, B")
energiehoogte = 2.4
debiet = 10
breedte = 11
kritischeDiepte = (2/3) * energiehoogte
def equation(y, H, Q, B):
    return y + (Q**2 / (20 * B**2)) * (1 / y**2) - H

# Finding the roots of the function using a range of initial guesses
y_schietend = root(equation, [0.01, kritischeDiepte], args=(energiehoogte, debiet, breedte)).x

# Filtering only the positive roots
diepteSchietend = [y for y in y_schietend if 0 < y < kritischeDiepte]
print(round(diepteSchietend[0], 2))

#vraag 20 Bij welke waterstand hebben we te maken met stromend water?
diepteStromend = root(equation, (energiehoogte - 0.01), args=(energiehoogte, debiet, breedte)).x
print(round(diepteStromend[0], 2))

print ("Bereken de evenwichtsdiepte van een trapeziumvormige watergang")
bodemverhang = kies_integer_getal_stap(1000, 5500, 500)
bodembreedte = kies_getal_stap(2, 8, 0.5, 1)
taludhelling = kies_integer_getal_stap(1, 5, 1)
debiet = kies_getal_stap(1, 3, 0.1, 1)
coeff_manning = kies_getal_stap(0.01, 0.03, 0.005, 3)
# Vraag 35 Bepaal de evenwichtsdiepte (m) bovenstrooms van de stuw (afgerond op 2 decimalen)
# oppervlak = ((bodembreedte + hevenwicht * taludhelling) * hevenwicht)
# natt_omtrek = (bodembreedte + 2 * hevenwicht * (1 + taludhelling ** 2) ** 0.5)
# hydraulische_straal = oppervlak / natt_omtrek
# gemiddelde_stroomsnelheid = (debiet / ((bodembreedte + hevenwicht * taludhelling) * hevenwicht))
# energieverhang = (gemiddelde_stroomsnelheid * coeff_manning / hydraulische_straal**(2/3))**(2)
# hydraulische_straal = (((bodembreedte + hevenwicht * taludhelling) * hevenwicht) / (bodembreedte + 2 * hevenwicht * (1 + taludhelling ** 2) ** 0.5))
# energieverhang = ((debiet / ((bodembreedte + hevenwicht * taludhelling) * hevenwicht)) * coeff_manning / (((bodembreedte + hevenwicht * taludhelling) * hevenwicht) / (bodembreedte + 2 * hevenwicht * (1 + taludhelling ** 2) ** 0.5))**(2/3))**(2)

#from scipy.optimize import fsolve
energieverhang = 1 / bodemverhang
# Definiëren van de vergelijking
def equation(hevenwicht):
    left_side = (debiet / ((bodembreedte + hevenwicht * taludhelling) * hevenwicht))
    right_side = coeff_manning / (((bodembreedte + hevenwicht * taludhelling) * hevenwicht) / (bodembreedte + 2 * hevenwicht * (1 + taludhelling ** 2) ** 0.5))**(2/3)
    return (left_side * right_side)**2 - energieverhang

# Proberen met meerdere startwaarden
start_values = [0.1, 0.5]
solutions = []

for guess in start_values:
    try:
        solution, = fsolve(equation, guess)
        if solution > 0:  # Omdat hevenwicht positief moet zijn
            solutions.append(solution)
    except:
        continue

# Verwijderen van dubbele oplossingen (als die er zijn) en sorteren
unique_solutions = sorted(set(solutions))

# De oplossing afdrukken
hevenwicht = unique_solutions[0]
print(round(unique_solutions[0], 2))


print ("kritische diepte trapeziumvormige watergang")
# Vraag 36 Bepaal vervolgens de kritische diepte (m) bovenstrooms van de stuw (afgerond op 2 decimalen)
# H = (3/2) * hkritisch
# H = hkritisch + v**2 / (2 * water.g)
# oppervlak = ((bodembreedte + hkritisch * taludhelling) * hkritisch)
# v = (debiet / ((bodembreedte + hkritisch * taludhelling) * hkritisch))
# (3/2) * hkritisch = hkritisch + (debiet / ((bodembreedte + hkritisch * taludhelling) * hkritisch))**2 / 20

# from scipy.optimize import fsolve
# Definiëren van de vergelijking voor hkritisch
def hkritisch_equation(hkritisch):
    return (3/2) * hkritisch - hkritisch - (debiet / ((bodembreedte + hkritisch * taludhelling) * hkritisch))**2 / 20

# Proberen met meerdere startwaarden
start_values = [0.1, 0.5]
hkritisch_solutions = []

for guess in start_values:
    try:
        solution, = fsolve(hkritisch_equation, guess)
        if solution > 0:  # Omdat hkritisch positief moet zijn
            hkritisch_solutions.append(solution)
    except:
        continue

# Verwijderen van dubbele oplossingen (als die er zijn) en sorteren
unique_hkritisch_solutions = sorted(set(hkritisch_solutions))

# De oplossing afdrukken
hkritisch = unique_hkritisch_solutions[0]
print(round(unique_hkritisch_solutions[0],2))

print ("Bereken de waterstand in een trapeziumvormige watergang, op basis van bekende Q, width, sideSlopeLeft, sideSlopeRight en H ;  gezocht: diepte")
# velocity = Q / A
# area = ((width + 0.5 *depth * sideSlopeLeft + 0.5 *depth * sideSlopeRight) * depth)
# H = depth + velocity**2 / (20)

# velocity = (Q / ((width + 0.5 *depth * sideSlopeLeft + 0.5 * depth * sideSlopeRight) * depth))
# H = depth + (Q / ((width + 0.5 * depth * SlopeLeft + 0.5 * depth * SlopeRight) * depth))**2 / 20
# depth <= H
# depth >= 0


from sympy import symbols, diff

# Definieer de variabelen
depth, H, Q, SlopeLeft, SlopeRight, width = symbols('depth H Q SlopeLeft SlopeRight width')

# Definieer de vergelijking
equation = H - (depth + (Q / ((width + 0.5 * depth * SlopeLeft + 0.5 * depth * SlopeRight) * depth)) ** 2 / 20)

# Bereken de afgeleide van de vergelijking ten opzichte van depth
derivative = diff(equation, depth)


# Definieer de Newton-Raphson methode
def newton_raphson(H_val, Q_val, SlopeLeft_val, SlopeRight_val, width_val, initial_guess, max_iterations=1000,
                   tolerance=1e-6):
    current_guess = initial_guess
    for i in range(max_iterations):
        # Evalueer de functie en haar afgeleide
        f_val = equation.subs(
            {H: H_val, Q: Q_val, SlopeLeft: SlopeLeft_val, SlopeRight: SlopeRight_val, width: width_val,
             depth: current_guess})
        f_prime_val = derivative.subs(
            {H: H_val, Q: Q_val, SlopeLeft: SlopeLeft_val, SlopeRight: SlopeRight_val, width: width_val,
             depth: current_guess})

        # Update de schatting met de Newton-Raphson formule
        next_guess = current_guess - f_val / f_prime_val

        # Controleer op convergentie
        if abs(next_guess - current_guess) < tolerance:
            return next_guess

        current_guess = next_guess

    return current_guess


# Voorbeeld van het gebruik van de functie:
H_val = 6
Q_val = 90
SlopeLeft_val = 1
SlopeRight_val = 1
width_val = 3
initial_guess = 0.9 * H_val
print ("H : ", H_val)
print("Q : ", Q_val)

result = newton_raphson(H_val, Q_val, SlopeLeft_val, SlopeRight_val, width_val, initial_guess)
print(result)

area = ((width_val + 0.5 * result * SlopeLeft_val + 0.5 * result * SlopeRight_val) * result)
velocity = Q_val / area
print("area : ", area)
print("velocity : ", velocity)
vhead = (velocity**2) / 20
print("vhead : ", vhead)
