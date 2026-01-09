import matplotlib.pyplot as plt
from common_utils import show_com731_header


# ---------- TASK C1 ----------
def plot_temp_humidity(df):
    show_com731_header()
    season = input("Season: ")

    df[df["Season"] == season] \
      .groupby("City")[["Temperature","Humidity"]] \
      .mean() \
      .plot(kind="bar")

    plt.title("Average Temperature & Humidity by City")
    plt.show()


# ---------- TASK C2 ----------
def plot_yearly_trend(df):
    show_com731_header()
    city = input("City: ")

    # Structure:
    # {year: {species: [values]}}
    yearly_data = {}

    for _, row in df.iterrows():
        if row["City"] != city:
            continue

        date_str = str(row["Date"])

        # ---- SAFE YEAR EXTRACTION (NO pandas) ----
        year = None
        if "/" in date_str:
            parts = date_str.split("/")
            if len(parts[-1]) == 4:
                year = int(parts[-1])
            else:
                year = 2000 + int(parts[-1])  # handles '16'
        elif "-" in date_str:
            parts = date_str.split("-")
            if len(parts[-1]) == 4:
                year = int(parts[-1])
            else:
                year = 2000 + int(parts[-1])

        if year is None:
            continue

        species = row["SpeciesCategory"]
        sightings = float(row["NumberOfSightings"])

        yearly_data.setdefault(year, {})
        yearly_data[year].setdefault(species, [])
        yearly_data[year][species].append(sightings)

    # ---- SORT YEARS PROPERLY ----
    years = sorted(yearly_data.keys())

    # Identify all species categories
    species_categories = set()
    for y in years:
        species_categories.update(yearly_data[y].keys())

    # ---- PLOT CLEAN TRENDS ----
    for species in species_categories:
        averages = []
        for y in years:
            values = yearly_data[y].get(species, [])
            avg = sum(values) / len(values) if values else 0
            averages.append(avg)

        plt.plot(years, averages, marker='o', label=species)

    plt.title("Yearly Trend of Average Wildlife Sightings by Species Category")
    plt.xlabel("Year")
    plt.ylabel("Average Number of Sightings")
    plt.legend(title="Species Category")
    plt.grid(True)
    plt.xticks(years)   # very important
    plt.show()


# ---------- TASK C3 ----------
def plot_public_awareness(df):
    show_com731_header()
    city = input("City: ")

    data = df[df["City"] == city] \
        .groupby("ResidentialAreaType")["PublicAwarenessLevel"] \
        .mean()

    plt.pie(data, labels=data.index, autopct="%1.1f%%")
    plt.title("Public Awareness Distribution")
    plt.show()


# ---------- TASK C4 ----------
def plot_custom_visual(df):
    show_com731_header()
    df.groupby("TimeOfDay")["NoiseLevel_dB"].mean().plot()
    plt.title("Noise Level by Time of Day")
    plt.show()
