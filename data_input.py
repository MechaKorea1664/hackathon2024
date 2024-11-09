import csv
import pandas as pd
import decimal as d

# Summarized Electric_Vehicle_Population_Data. (2024 ONLY)
# Outdated
def car_registration_per_state_per_year():
    #VIN (1-10),County,City,State,Postal Code,Model Year,Make,Model,Electric Vehicle Type,Clean Alternative Fuel Vehicle (CAFV) Eligibility,Electric Range,Base MSRP,Legislative District,DOL Vehicle ID,Vehicle Location,Electric Utility,2020 Census Tract
    dict_washington_2024 = {}
    with open("hackathon2024\Data\Electric_Vehicle_Population_Data.csv",newline="") as csv_open:
        line_content = csv.reader(csv_open,delimiter=',')
        for row in line_content:
            if row[1] not in dict_washington_2024:
                if row[8] == "Battery Electric Vehicle (BEV)":
                    dict_washington_2024[row[1]] = 1
            else:
                if row[8] == "Battery Electric Vehicle (BEV)":
                    dict_washington_2024[row[1]] += 1

    with open('hackathon2024\Data_Summary\Washington_2024.csv', 'w', newline='') as csvfile:
        fieldnames = ['County', 'EV Count']
        writer = csv.writer(csvfile)
        writer.writerow(["County","EV Count"])
        for county,ev_count in dict_washington_2024.items():
            writer.writerow([county,ev_count])

# Summarized Electric_Vehicle_Population_Size_History_By_County.
# Outdated / incomplete
def summarize_EVPSHBS():
    dict_nationwide = {}
    with open("hackathon2024\Data\Electric_Vehicle_Population_Size_History_By_County.csv",newline="") as csv_open:
        line_content = csv.reader(csv_open,delimiter=',')
        totalread = 0
        for row in line_content:
            totalread += 1
            if row[0] == "Date":
                continue
            year = row[0].split()[2]
            dict_nationwide[year] = {row[2]}
            dict_nationwide[year][row[2]][row[1]] = {"EV Count":row[4],"Non-EV Count": int(row[4]) + int(row[7])}

    totalcount = 0
    for year,state in dict_nationwide.items():
        for state,county in state.items():
            print(year,state,county)      
            totalcount += 1
    print(totalcount) 
    print(totalread)         

# Reading annual_CO2_per_state_power_generation_summary.xlsx and
# reading annual_generation_state.xls
# It's me Kevin
def CO2_to_kWh_per_state_annual():
    # Measured in million metric tons of carbon dioxide.
    annual_state_CO2 = pd.read_excel("hackathon2024/emission/annual_CO2_per_state_power_generation.xlsx",header=4,skiprows=[56,57],)
    # Measured in megawatt hours.
    annual_state_electricity = pd.read_excel("hackathon2024/emission/annual_generation_state.xls",header=1)
    state_name_abbreviation = {"Alabama":"AL", "Alaska":"AK","Arizona":"AZ","Arkansas" :"AR","California":"CA",
                               "Colorado":"CO","Connecticut":"CT","Delaware":"DE","District of Columbia":"DC",
                               "Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL",
                               "Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA",
                               "Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN",
                               "Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV",
                               "New Hampshire":"NH","New Jersey":"NJ","New Mexico":"NM","New York":"NY",
                               "North Carolina":"NC","North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR",
                               "Pennsylvania":"PA","Puerto Rico":"PR","Rhode Island":"RI","South Carolina":"SC",
                               "South Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT",
                               "Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY"}
    
    annual_state_CO2_to_Wh = {"State":[], "Year":[], "CO2/Wh":[]}

    for year in range(2016,2023):
        for index, row in annual_state_CO2.iterrows():
                current_state_abbreviated = state_name_abbreviation[row["State"]]
                annual_state_CO2_to_Wh["State"].append(current_state_abbreviated)
                annual_state_CO2_to_Wh["Year"].append(year)

                state_carbon_production = row[year]
                row_of_interest = annual_state_electricity.loc[
                    (annual_state_electricity["YEAR"] == year) &
                    (annual_state_electricity["STATE"] == current_state_abbreviated) &
                    (annual_state_electricity["TYPE OF PRODUCER"] == "Total Electric Power Industry") &
                    (annual_state_electricity["ENERGY SOURCE"] == "Total")]
                state_electricity_production = row_of_interest["GENERATION (Megawatthours)"].iloc[0]

                # Convert values to needed units.
                state_carbon_production_kg = d.Decimal(state_carbon_production) * d.Decimal(1000000000)
                state_electricity_production_Wh = d.Decimal(state_electricity_production) * d.Decimal(1000000)

                # Choose the least amount of sig-fig digits and remove non-sigfig digits
                precision_digits = min(len(str(state_carbon_production).split(".")[0])+1,len(str(state_electricity_production).split(".")[0]))
                d.getcontext().prec = precision_digits
                print(precision_digits)

                # Calculate kg CO2 / Wh
                state_kg_CO2_per_Wh = state_carbon_production_kg / state_electricity_production_Wh


                # Append kg CO2 / Wh to yearly dictionary.
                annual_state_CO2_to_Wh["CO2/Wh"].append(float(state_kg_CO2_per_Wh))

                # Reset precision
                d.getcontext().prec = 64
    
    output = pd.DataFrame(annual_state_CO2_to_Wh)
    output.to_csv("hackathon2024/Data_Summary/emission_16-22.csv",index=False)
    
CO2_to_kWh_per_state_annual()