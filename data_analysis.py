import pandas as pd
from common_utils import show_com731_header


# ---------- TASK B1 ----------
def analyse_top_species(df):
    show_com731_header()
    season = input("Season: ")
    green = float(input("Min Nearby Green Spaces: "))

    print(
        df[(df["Season"] == season) &
           (df["NearbyGreenSpaces"] > green)]
        ["WildlifeSpecies"]
        .value_counts()
        .head(3)
    )


# ---------- TASK B2 ----------
def analyse_weather_time_patterns(df):
    show_com731_header()
    city = input("City: ")

    print(
        df[df["City"] == city]
        .groupby(["WeatherCondition","TimeOfDay"])
        [["NumberOfSightings","SightingDuration_Min"]]
        .mean()
    )


# ---------- TASK B3 ----------
def analyse_interaction_behavior(df):
    show_com731_header()
    interaction = input("Interaction Type: ")

    avg = df[df["InteractionType"] == interaction]["SightingDuration_Min"].mean()

    print(
        df[(df["InteractionType"] == interaction) &
           (df["SightingDuration_Min"] > avg)]
        .groupby("ResidentialAreaType")
        [["NoiseLevel_dB","HumanActivityLevel","LightPollutionLevel"]]
        .mean()
    )


# ---------- TASK B4 ----------
def analyse_custom_insight(df):
    show_com731_header()
    print(
        df.groupby("SpeciesCategory")
        ["PublicAwarenessLevel"]
        .mean()
    )
