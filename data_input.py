import csv


# Summarized Electric_Vehicle_Population_Data. (2024 ONLY)
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
                
                

#car_registration_per_state_per_year()
summarize_EVPSHBS()