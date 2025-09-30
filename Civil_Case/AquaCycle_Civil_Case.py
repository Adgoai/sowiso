import numpy as np

from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

from AquaCycle.AquaCycle_lib import kies_integer_getal_stap, kies_getal_stap

# Alleen het de tekst hieronder kopieren naar sowiso variabele $adgo_water_lib
# Onderstaande hekjes verwijderen om de code te activeren in sowiso. Behalve bij versie

# Casus Civil Hydrologie

# sw_Python("
# versie 22-05-2024
# $AquaCycle_lib

# lijst van kengetallen
# stedelijk ca = 5 * 10 km  buitengebied ca 15 * 30 km
# urban housing heeft gemengd rioolstelsel
# urbun industry heeft gescheiden rioolstelsel
rural_total_area_ha = kies_integer_getal_stap(40000,50000,1000)  # ha
rural_surface_level_m = kies_getal_stap(0.4,0.8, 0.1)  # m NAP
rural_groundwater_level_m = rural_surface_level_m - kies_getal_stap(0.4, 0.8, 0.1)  # m NAP
rural_groundwater_level_m = round(rural_groundwater_level_m, 2)
rural_water_area_perc = kies_integer_getal_stap(4,11,1)  # %
rural_storage_surface_mm = 10  # mm
rural_pump_capacity_mmday = kies_integer_getal_stap(8,16,1)  # mm/day

soil_pore_space_perc = kies_integer_getal_stap(20,30,1)  # %
soil_pore_space = soil_pore_space_perc / 100  # -

river_water_level = 0.0  # m NAP

urban_area_ha = kies_integer_getal_stap(4000,5500, 500) # ha
urban_surface_level_m = rural_surface_level_m + 0.9 # m NAP
urban_groundwater_level_m = urban_surface_level_m - kies_getal_stap(1, 1.4, 0.1)  # m NAP
urban_groundwater_level_m = round(urban_groundwater_level_m, 2)
urban_housing_area_perc = kies_getal_stap(60,90,10)  # %
urban_housing_density = kies_integer_getal_stap(30,100,10)  # (house/ha)
urban_housing_population_density = 2.12  # (people/house)
urban_housing_area_ha = urban_area_ha * urban_housing_area_perc / 100  # ha
urban_housing_population= urban_housing_area_ha * urban_housing_density * urban_housing_population_density  # people
urban_housing_drinking_water_demand_year = 50  # m3
urban_housing_paved_area_perc = 50  # %
urban_housing_water_area_perc = kies_integer_getal_stap(4,11,1)  # %
urban_housing_unpaved_area_perc = 100 - urban_housing_paved_area_perc - urban_housing_water_area_perc    # %
urban_housing_paved_area_storage_mm = 1  # mm
urban_housing_discharge_overflow_year_mm = 250  # mm
urban_housing_roofs_perc = 50  # % of total paved area
urban_housing_green_roofs_perc = kies_integer_getal_stap(25,45,5)  # % of total roofs
urban_housing_pavement_perc = 100 - urban_housing_roofs_perc  # % of total paved area
urban_housing_pavement_disconnect_perc = kies_integer_getal_stap(30,55,5)  # % of total pavement


urban_industrial_area_perc = 100 - urban_housing_area_perc  # %
urban_industrial_paved_area_perc = 75  # %
urban_industrial_water_area_perc = kies_integer_getal_stap(4,11,1)  # %
urban_industrial_unpaved_area_perc = 100 - urban_industrial_paved_area_perc  # %
urban_industrial_water_demand = kies_getal_stap(0.5,2.1,0.1,1)  # (l/(ha.s))

urban_sewer_pump_overcapacity_mmhour = kies_getal_stap(0.6,0.9,0.1,1)  # mm/hour
urban_sewer_storage_mm = kies_integer_getal_stap(8,12,1)  # mm

precipitation_short = 20  # mm in 1 hour
precipitation_long = 100  # mm in 24 hours

precipitation_year = kies_integer_getal_stap(800,1200,100)  # mm
rural_evaporation_year = 0.63 * precipitation_year   # mm
round(rural_evaporation_year, 0)
urban_evaporation_year = 0.5 * precipitation_year   # mm
round(urban_evaporation_year, 0)

# Basis Berekeningen
rural_water_area_ha = rural_total_area_ha * rural_water_area_perc / 100  # ha
rural_soil_area_ha = rural_total_area_ha - rural_water_area_ha  # ha
rural_pump_capacity_m3s = (rural_pump_capacity_mmday / (1000 * 86400)) * rural_total_area_ha * 10000 # m3/s
rural_pump_capacity_m3s = round(rural_pump_capacity_m3s, 2)
rural_water_area_ha_trick = rural_water_area_ha + rural_soil_area_ha * soil_pore_space_perc / 100  # ha
rural_max_storage_m3 = rural_water_area_ha_trick * 10000 * (rural_surface_level_m - rural_groundwater_level_m)  # m3
rural_max_storage_m3 = round(rural_max_storage_m3, 0)

urban_housing_paved_area_ha = urban_housing_area_ha * urban_housing_paved_area_perc / 100  # ha
urban_housing_water_area_ha = urban_housing_area_ha * urban_housing_water_area_perc / 100  # ha
urban_housing_unpaved_area_ha = urban_housing_area_ha - urban_housing_paved_area_ha - urban_housing_water_area_ha  # ha
urban_sewer_pump_overcapacity_m3s = urban_sewer_pump_overcapacity_mmhour / (1000 * 3600) * urban_housing_paved_area_ha * 10000  # m3/s
urban_sewer_pump_overcapacity_m3s = round(urban_sewer_pump_overcapacity_m3s, 2)
urban_sewer_storage_m3 = urban_sewer_storage_mm * urban_housing_paved_area_ha * 10000 / 1000  # m3
industrial_area_ha = urban_area_ha * urban_industrial_area_perc / 100  # ha
industrial_paved_area_ha = industrial_area_ha * urban_industrial_paved_area_perc / 100  # ha
industrial_water_area_ha = industrial_area_ha * urban_industrial_water_area_perc / 100  # ha
industrial_unpaved_area_ha = industrial_area_ha * urban_industrial_unpaved_area_perc / 100  # ha
industrial_waster_water_m3s = industrial_area_ha * urban_industrial_water_demand / 1000  # m3/s
industrial_waster_water_m3s = round(industrial_waster_water_m3s, 4)

# vraag 3
rural_precipitation_24hour = round((precipitation_long * rural_total_area_ha * 10000 / 1000),0)  # m3
rural_pump_24hour = round(rural_pump_capacity_m3s * 86400, 0)  # m3
rural_storage_24hour = round(rural_precipitation_24hour - rural_pump_24hour,0)  # m3

# vraag 4
rural_rise_water_24hour = round(rural_storage_24hour / (rural_water_area_ha_trick * 10000), 2)  # m

# vraag 5
rural_water_level_24hour = round(rural_groundwater_level_m + rural_rise_water_24hour, 2)  # m NAP
rural_flooding_24hour = round(rural_water_level_24hour - rural_surface_level_m,2)  # m
if rural_flooding_24hour > 0:
    rural_flood = 1 # ja
else:
    rural_flood = 2 # nee

# vraag 6
rural_precipitation_year_m3 = round(precipitation_year * rural_total_area_ha * 10000 / 1000, 0)  # m3
rural_evaporation_year_m3 = round(rural_evaporation_year * rural_total_area_ha * 10000 / 1000, 0)  # m3
rural_storage_year_m3 = round(rural_precipitation_year_m3 - rural_evaporation_year_m3, 0)  # m3

# vraag 7
rural_pumping_hours_year = round(rural_storage_year_m3 / (rural_pump_capacity_m3s * 3600), 0)  # hours

# vraag 8b
urban_housing_precipitation_short = round(precipitation_short * urban_housing_paved_area_ha * 10000 / 1000, 0)  # m3
urban_housing_storage_paved_short = round(urban_housing_paved_area_ha * urban_housing_paved_area_storage_mm * 10000 / 1000, 0)  # m3
urban_housing_pump_discharge_short = round(urban_sewer_pump_overcapacity_m3s * 3600, 0)  # m3
urban_housing_surplus_rainwater_short = round(urban_housing_precipitation_short - urban_housing_storage_paved_short - urban_sewer_storage_m3 - urban_housing_pump_discharge_short, 0)  # m3

# vraag 10
urban_housing_precipitation_year = round(precipitation_year * urban_housing_paved_area_ha * 10000 / 1000, 0)  # m3
urban_housing_evaporation_year = round(urban_evaporation_year * urban_housing_paved_area_ha * 10000 / 1000, 0)  # m3
urban_housing_discharge_overflow_year = round(urban_housing_discharge_overflow_year_mm * urban_housing_paved_area_ha * 10000 / 1000, 0)  # m3
urban_housing_surplus_rainwater_year = round(urban_housing_precipitation_year - urban_housing_evaporation_year - urban_housing_discharge_overflow_year, 0)  # m3

# vraag 11
urban_housing_wastewater_houses_year = round(urban_housing_population * urban_housing_drinking_water_demand_year, 0)  # m3
urban_housing_total_water_to_plant = round(urban_housing_wastewater_houses_year + urban_housing_surplus_rainwater_year, 0)  # m3

# vraag 12
roofs_area_ha = urban_housing_roofs_perc / 100 * urban_housing_paved_area_ha  # ha
pavement_area_ha = urban_housing_pavement_perc / 100 * urban_housing_paved_area_ha  # ha
pavement_disconnect_area_ha = urban_housing_pavement_disconnect_perc / 100 * pavement_area_ha  # ha
green_roofs_area_ha = urban_housing_green_roofs_perc / 100 * roofs_area_ha  # ha
urban_adjusted_housing_paved_area_ha = round(urban_housing_paved_area_ha - (pavement_disconnect_area_ha + green_roofs_area_ha/2), 0)  # ha

# vraag 13
urban_adjusted_precipitation_short = round(precipitation_short * urban_adjusted_housing_paved_area_ha * 10000 / 1000, 0)  # m3
urban_adjusted_storage_paved_short = round(urban_adjusted_housing_paved_area_ha * urban_housing_paved_area_storage_mm * 10000 / 1000, 0)  # m3
urban_adjusted_surplus_water_short = round(urban_adjusted_precipitation_short - urban_adjusted_storage_paved_short - urban_sewer_storage_m3 - urban_housing_pump_discharge_short, 0)  # m3

# vraag 14
urban_adjusted_extra_infil_short = round((precipitation_short - urban_housing_paved_area_storage_mm) * pavement_disconnect_area_ha * 10000 / 1000, 0)  # m3

# vraag 15
urban_adjusted_precipitation_year = round(precipitation_year * urban_adjusted_housing_paved_area_ha * 10000 / 1000, 0)  # m3
urban_adjusted_evaporation_year = round(urban_evaporation_year * urban_adjusted_housing_paved_area_ha * 10000 / 1000, 0)  # m3
urban_adj_discharge_overflow_year = round(urban_housing_discharge_overflow_year_mm * urban_adjusted_housing_paved_area_ha * 10000 / 1000, 0)  # m3
urban_adj_surplus_rainwater_year = round(urban_adjusted_precipitation_year - urban_adjusted_evaporation_year - urban_adj_discharge_overflow_year, 0)  # m3

# vraag 16
urban_adjusted_extra_infil_year = round((precipitation_year - urban_evaporation_year) * pavement_disconnect_area_ha * 10000 / 1000, 0)  # m3


# variabelen naar sowiso
print(rural_total_area_ha)  # [0]
print(rural_surface_level_m)  # [1]
print(rural_groundwater_level_m)  # [2]
print(rural_water_area_perc)  # [3]
print(rural_storage_surface_mm)  # [4]
print(rural_pump_capacity_mmday)  # [5]
print(soil_pore_space)  # [6]
print(soil_pore_space_perc)  # [7]
print(river_water_level)  # [8]
print(urban_area_ha)  # [9]
print(urban_surface_level_m)  # [10]
print(urban_groundwater_level_m)  # [11]
print(urban_housing_area_perc)  # [12]
print(urban_housing_density)  # [13]
print(urban_housing_population_density)  # [14]
print(urban_housing_area_ha)  # [15]
print(urban_housing_population)  # [16]
print(urban_housing_drinking_water_demand_year)  # [17] vraag 11
print(urban_housing_paved_area_perc)  # [18]
print(urban_housing_water_area_perc)  # [19]
print(urban_housing_unpaved_area_perc)  # [20]
print(urban_industrial_area_perc)  # [21]
print(urban_industrial_paved_area_perc)  # [22]
print(urban_industrial_water_area_perc)  # [23]
print(urban_industrial_unpaved_area_perc)  # [24]
print(urban_industrial_water_demand)  # [25]
print(urban_sewer_pump_overcapacity_mmhour)  # [26]
print(urban_sewer_storage_mm)  # [27]
print(precipitation_short)  # [28] Vraag 8b
print(precipitation_long)  # [29] Vraag 3
print(precipitation_year)  # [30]
print(rural_evaporation_year)  # [31]
print(urban_evaporation_year)  # [32]

# vraag 1
print(rural_water_area_ha)  # [33]
print(rural_soil_area_ha)  # [34]
print(rural_pump_capacity_m3s)  # [35]

# vraag 2
print(rural_water_area_ha_trick)  # [36]
print(rural_max_storage_m3)  # [37]

# vraag 3
print(rural_precipitation_24hour)  # [38]
print(rural_pump_24hour)  # [39]
print(rural_storage_24hour)  # [40]

# vraag 4
print(rural_rise_water_24hour)  # [41]

# vraag 5
print(rural_water_level_24hour)  # [42]
print(rural_flooding_24hour)  # [43]
print(rural_flood)  # [44]

# vraag 6
print(rural_precipitation_year_m3)  # [45]
print(rural_evaporation_year_m3)  # [46]
print(rural_storage_year_m3)  # [47]

# vraag 7
print(rural_pumping_hours_year)  # [48]

# vraag 8a
print(urban_housing_paved_area_ha)  # [49]
print(urban_housing_water_area_ha)  # [50]
print(urban_housing_unpaved_area_ha)  # [51]

# vraag 8b
print(urban_housing_precipitation_short)  # [52]
print(urban_housing_storage_paved_short)  # [53]
print(urban_sewer_storage_m3)  # [54]
print(urban_housing_pump_discharge_short)  # [55]
print(urban_housing_surplus_rainwater_short)  # [56]

# vraag 10
print(urban_housing_precipitation_year)  # [57]
print(urban_housing_evaporation_year)  # [58]
print(urban_housing_discharge_overflow_year)  # [59]
print(urban_housing_surplus_rainwater_year)  # [60]

# vraag 11
print(urban_housing_wastewater_houses_year)  # [61]
print(urban_housing_total_water_to_plant)  # [62]

# vraag 12
print(urban_housing_roofs_perc)  # [63]
print(urban_housing_green_roofs_perc)  # [64]
print(urban_housing_pavement_perc)  # [65]
print(urban_housing_pavement_disconnect_perc) # [66]
print(urban_adjusted_housing_paved_area_ha)  # [67]

# vraag 13
print(urban_adjusted_precipitation_short)  # [68]
print(urban_adjusted_storage_paved_short)  # [69]
print(urban_adjusted_surplus_water_short)  # [70]

# vraag 14
print(urban_adjusted_extra_infil_short)  # [71]

# vraag 15
print(urban_adjusted_precipitation_year)  # [72]
print(urban_adjusted_evaporation_year)  # [73]
print(urban_adj_discharge_overflow_year)  # [74]
print(urban_adj_surplus_rainwater_year)  # [75]

# vraag 16
print(urban_adjusted_extra_infil_year)  # [76]

#Deze was ik vergeten :-(
print(urban_housing_paved_area_storage_mm)  # [77]
print(urban_housing_discharge_overflow_year_mm)  # [78]
print(urban_sewer_pump_overcapacity_m3s)  # [79]

#")