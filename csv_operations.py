import csv
from common_utils import show_com731_header

def read_csv_to_list(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        records = list(reader)
    return headers, records


# ---------- TASK A1 ----------
def fetch_species_by_city(headers, records):
    show_com731_header()
    city = input("Enter City: ")
    h = {k:i for i,k in enumerate(headers)}

    for r in records:
        if r[h["City"]] == city:
            print(r[h["WildlifeSpecies"]],
                  r[h["SpeciesCategory"]],
                  r[h["NumberOfSightings"]],
                  r[h["IsEndangeredSpecies"]])


# ---------- TASK A2 ----------
def fetch_environment_by_time_aqi(headers, records):
    show_com731_header()
    time = input("Time of Day: ")
    aqi = float(input("Max AQI: "))
    h = {k:i for i,k in enumerate(headers)}

    for r in records:
        if r[h["TimeOfDay"]] == time and float(r[h["AirQualityIndex"]]) < aqi:
            print(r[h["Temperature"]],
                  r[h["Humidity"]],
                  r[h["AirQualityIndex"]],
                  r[h["WeatherCondition"]])


# ---------- TASK A3 ----------
def fetch_human_impact_data(headers, records):
    show_com731_header()
    udi = float(input("Urban Development Index > "))
    water = float(input("Proximity To Water > "))
    h = {k:i for i,k in enumerate(headers)}

    for r in records:
        if float(r[h["UrbanDevelopmentIndex"]]) > udi and float(r[h["ProximityToWaterSource"]]) > water:
            print(r[h["HumanActivityLevel"]],
                  r[h["NoiseLevel_dB"]],
                  r[h["LightPollutionLevel"]],
                  r[h["GarbageManagementScore"]])


# ---------- TASK A4 ----------
def fetch_custom_csv_data(headers, records):
    show_com731_header()
    col = input("Numeric column for condition: ")
    c1 = input("Display column 1: ")
    c2 = input("Display column 2: ")
    threshold = float(input("Threshold: "))

    h = {k:i for i,k in enumerate(headers)}

    for r in records:
        try:
            if float(r[h[col]]) > threshold:
                print(r[h[c1]], r[h[c2]])
        except:
            continue
