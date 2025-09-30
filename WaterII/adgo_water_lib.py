import adgo_lib

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
#"
# versie 8-6-2023
class water:

    sgzoet = 1000
    sgzout = 1025
    g = 10
    kin_visco = 1.3 * 10 ** -6

def oppervlakte_cirkel(diameter_m):
    oppervlak = 0.25 * 3.14159 * diameter_m ** 2
    return oppervlak
def snelheidshoogte_m(v):
    snelheidshoogte = v ** 2 / (2 * water.g)
    return snelheidshoogte
def drukhoogte_m(p, sg):
    drukhoogte = p / (sg * water.g)
    return drukhoogte
def druk_pascal(h, sg):
    druk = h * sg * water.g
    return druk
def Bernoulli_dH_energie(z1, h1, v1, z2, h2, v2):
    dH = z1 - z2 + h1 - h2 + v1 ** 2 / (2 * water.g) - v2 ** 2 / (2 * water.g)
    return dH
def Bernoulli_dh_druk (v1, v2, dH):
    dh = (v1 ** 2 - v2 ** 2) / (2 * water.g) - dH
    return dh

#"
