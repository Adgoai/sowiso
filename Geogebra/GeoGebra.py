import random

from adgo_lib import kies_getal_tussen, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# tekenen van een watergang in geogebra

# A------B                      E------F
#         -                  -
#            -            -
#               C------D


#sw_Python("
#versie 22-05-2024
#$adgo_lib

print(10) # [0]

talud_x = 2
talud_y = 3
diepte = 4
bodembreedte = 3
zijkant = 3

xA = 0
xB = zijkant
xC = xB + talud_x * diepte
xD = xC + bodembreedte
xE = xD + talud_y * diepte
xF = xE + zijkant

breed = 2 * zijkant + bodembreedte + diepte * (talud_x + talud_y) + 2
hoog = breed / 4


gggCommands = '\\n'.join([
    f'ZoomIn[0,-{hoog},{breed},{hoog}]',
    'A = (0,0)',
    f'B = ({xB},0)',
    f'C = ({xC},{-diepte})',
    f'D = ({xD},{-diepte})',
    f'E = ({xE},0)',
    f'F = ({xF},0)',
    'ShowLabel(A,false)',
    # 'ShowLabel(B,false)',
    'ShowLabel(C,false)',
    'ShowLabel(D,false)',
    'ShowLabel(E,false)',
    'ShowLabel(F,false)',
    'PA = Polygon(B,C,D,E)',
    'SetColor(PA, Blue)',
    'AB = Segment(A,B)',
    'BC = Segment(B,C)',
    'CD = Segment(C,D)',
    'DE = Segment(D,E)',
    'EF = Segment(E,F)',

])
print(gggCommands) # [1]

#")
