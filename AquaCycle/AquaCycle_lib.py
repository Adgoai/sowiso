# Gehele tekst kopieren naar sowiso variabele $adgo_lib

#"
# versie 13-12-2023
import random
import numpy as np
import math

def kies_getal_tussen(van, tot, afronden=0):  # afronden geeft het aantal decimalen aan
    return round(random.uniform(van, tot), afronden)

def kies_integer_getal_stap(van, tot, stap=1):  # vaak wil je een vaste stapgrootte tussen de willekeurige getallen
    return random.randrange(van, tot, stap)

def kies_getal_stap(van, tot, stap=0.1, decimalen=1):  # vaak wil je een vaste stapgrootte tussen de willekeurige getallen
    dec = 10 ** decimalen
    start = int(round(van * dec, 0))
    stop = int(round(tot * dec, 0))
    stap_integer = int(round(stap * 10 ** decimalen, 0))
    if stap_integer == 0:
        stap_integer = 1
    getal = random.randrange(start, stop, stap_integer)
    return round((getal / dec), decimalen)

def significante_cijfers(num, digits):
    return '{:.{}g}'.format(num, digits)

#"
