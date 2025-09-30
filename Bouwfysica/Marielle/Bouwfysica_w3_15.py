import random
from adgo_lib import kies_getal_tussen, kies_getal_stap, kies_integer_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

#sw_Python("
#versie 15-01-2025
#$adgo_lib
#$adgo_bouwfysica_lib

# We beschouwen een stuk dak van een wat oudere woning, bestaande uit:
# 14 m2 gesloten dakconstructie met U = 0,5 W/m2K en
# 1m2 een dakraam met U = 2,5 W/m2K
# Verder weet je dat het temperatuurverschil tussen binnen en buiten 13K bedraagt en dat de lengte van het stookseizoen 3500 uur bedraagt.

# Bereken hoeveel warmte er gedurende het stookseizoen door het gesloten deel van het dak verloren gaat

Q_transmissie_gesloten = round(14 * 0.5 * 13 * 3500 / 1000, 0)

# Bereken hoeveel warmte er gedurende het stookseizoen door het dakraam verloren gaat.

Q_transmissie_dakraam = round(1 * 2.5 * 13 * 3500 / 1000, 0)

# Door extra isolatie aan te brengen tegen het dak, kan de U worden teruggebracht naar 0,2 /m2K.
#
# Door het dakraam te vervangen kan de U worden teruggebracht naar 1,3 W/m2K.
 # Bereken hoeveel warmte er gedurende het stookseizoen door het gesloten deel van het dak verloren gaat als de verbetering is doorgevoerd.

Q_transmissie_gesloten_verbeterd = round(14 * 0.2 * 13 * 3500 / 1000, 0)

# Hoeveel minder is dat (in kWh)? Antwoord 319-127 = 192 kWh

Q_transmiss_minder = Q_transmissie_gesloten - Q_transmissie_gesloten_verbeterd

# Bereken hoeveel warmte er gedurende het stookseizoen door het nieuwe dakraam verloren gaat.

Q_transmissie_dakraam_verbeterd = round(1 * 1.3 * 13 * 3500 / 1000, 0)

# Hoeveel minder is dat (in kWh)?

Q_transmissie_minder_dakraam = Q_transmissie_dakraam - Q_transmissie_dakraam_verbeterd


print([Q_transmissie_gesloten, Q_transmissie_dakraam, Q_transmissie_gesloten_verbeterd, Q_transmiss_minder, Q_transmissie_dakraam_verbeterd, Q_transmissie_minder_dakraam])


#")
