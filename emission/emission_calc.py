# Reminder that distance is measured in MILES.

# Calculates carbon emission by gas vehicles' average mpg.
def calculate_emission_gas_kilogram(distance, avg_mpg):
    return (distance/avg_mpg)*8.887

def calculate_emission_diesel_kilogram(distance, avg_mpg):
    return (distance/avg_mpg)*10.190

# Calculate's carbon emission by EV.
def calculate_emission_electric_kilogram(distance, avg_mileage, year):
    # Calculations, sources in Emission Data Summary.txt.
    efficiency = {2016:0.0004464,
                  2017:0.0004319,
                  2018:0.0004219,
                  2019:0.0003917,
                  2020:0.0003616,
                  2021:0.0003776,
                  2022:0.0003644,
                  2023:0.0003416}
    return (distance/avg_mileage)*efficiency[year]