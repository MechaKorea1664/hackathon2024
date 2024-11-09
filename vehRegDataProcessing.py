import pandas as pd
import numpy as np

#print(pd.__version__) Uncomment to verify if pandas is working...

# Math for Numpy?
# Figure Out the Percentage of EV Vehicles for each Year
# Include TOTAL EV/EPHEV Vehicle AND Gas Percentages for each Year
# Somehow Compare EVs with Gas Vehicles (CNG, Gas, Diesel, etc.)
# Turn all of this somehow into a python function

# I am not entirely sure how to convert all of this into a function that would be useful for y'all.
# I DO NOT KNOW WHAT I AM DOING HAHAHAHAHAH -Duy

# Omitting Unknown Fuel Type for Now

# Reads the Excel Document. Make sure it's in the same directory!
df = pd.read_excel("VehicleRegistrationCountByState.xlsx")

# References the column names of the Excel document
EVCol =  "Electric (EV)"
PHEVCol = "Plug-In Hybrid Electric (PHEV)"
HEVCol = "Hybrid Electric (HEV)"
bioCol = "Biodiesel"
ethFlexCol = "Ethanol/Flex (E85)"
CNGCol = "Compressed Natural Gas (CNG)"
propCol = "Propane"
methCol = "Methanol"
gasCol = "Gasoline"
diesCol = "Diesel"

# Year Ranges (Column Positions from Excel document)
year_ranges = {
    2016: (2,52),    #   Associated year:(start_row,end Row)
    2017: (53,103),
    2018: (104,154),
    2019: (155,205),
    2020: (206,256),
    2021: (257,307),
    2022: (308,358),
    2023: (359,409),
}

# Dictionaries to store sums for each year (Call with sumName[year]) Ex. print(EVSums[2022])
# Sums for each type
EVSums = {}
PHEVSums = {}
HEVSums = {}
bioSums = {}
ethFlexSums = {}
CNGSums = {}
propSums = {}
methSums = {}
gasSums = {}
dieselSums = {}

# Total of Combined EV and Combined NON-EV
totalEVSums = {}
totalNonEVSums = {}

# Total of ALL VECHILES COMBINED
totalAll = {}

# Percent of EVs
percsEV = {}

# Percent of NON-EVs
percsNEV = {}

# Differences
percDiffs = {}
totalDiffs = {}

# Sum of Each Vehicle Type for Each Year (seperated)
for year, (startRow, endRow) in year_ranges.items():
    EVColSum = df[EVCol][startRow -1:endRow].sum()
    PHEVcolSum = df[PHEVCol][startRow -1:endRow].sum()
    HEVColSum = df[HEVCol][startRow -1:endRow].sum()
    # Total for ALL EVs
    totalEV = EVColSum + PHEVcolSum + HEVColSum

    bioColSum = df[bioCol][startRow -1:endRow].sum()
    ethFlexColSum = df[ethFlexCol][startRow -1:endRow].sum()
    CNGColSum = df[CNGCol][startRow -1:endRow].sum()
    propColSum = df[propCol][startRow -1:endRow].sum()
    methColSum = df[methCol][startRow -1:endRow].sum()
    gasColSum = df[gasCol][startRow -1:endRow].sum()
    diesColSum = df[diesCol][startRow -1:endRow].sum()
    # Total for ALL NON-EVs
    totalNonEV = bioColSum + ethFlexColSum + propColSum + methColSum + gasColSum + gasColSum

    # Total for ALL VEHICLES
    sumAll = totalEV + totalNonEV

    # Percent EV of ALL
    percEV = round(((totalEV / sumAll) *100),2)
    # Percent NON-EV of ALL
    percNEV = round(((totalNonEV / sumAll)*100),2)

    # Differences
    percDiff = round((abs(percEV-percNEV)),2)
    totalDiff =  round((abs(totalEV-totalNonEV)),2)

    EVSums[year]=EVColSum
    PHEVSums[year]=PHEVcolSum
    HEVSums[year]=HEVColSum
    bioSums[year]=bioColSum
    ethFlexSums[year]=ethFlexColSum
    CNGSums[year]=CNGColSum
    propSums[year]=propColSum
    methSums[year]=methColSum
    gasSums[year]=gasColSum
    dieselSums[year]=diesColSum

    totalEVSums[year] = totalEV
    totalNonEVSums[year] = totalNonEV
    totalAll[year] = sumAll

    percsEV[year] = percEV
    percsNEV[year] = percNEV

    percDiffs[year] = percDiff
    totalDiffs[year] = totalDiff

# Prints in Terminal, Testing functionality,
print(f"Num of EVs in 2016: {EVSums[2017]}") #Sum of EVs for 2016
print(f"Total EV Types in 2016: {totalEVSums[2016]}") #Sum of ALL EVs 2016
print(f"Total Non-Ev Types in 2016: {totalNonEVSums[2016]}") #Sum of ALL NON-EVs 2016
print(f"ALL VEHICLES 2016: {totalAll[2016]}") # Sum of ALL VEHICLES
print(f"Percent of EVs in 2016: {percsEV[2016]}%") # Percent of EVs of all in 2016
print(f"Percent of Non EVs in 2016: {percsNEV[2016]}%") # Percent of NON-EVs of all in 2016
print(f"Percent Diff 2016: {percDiffs[2016]}%") # Percent Diff of EV to non-EV
print(f"Total Diff 2016: {totalDiffs[2016]}%") # Total Diff of EV to non-EV


# Creates and writes into text document
with open("outputFile.txt", "w") as f:
    print("Output File has been created!")
    for year in year_ranges.keys():
        f.write(f"{year}: EV: {percsEV[year]}%      Non-EV: {percsNEV[year]}%     %Diff: {percDiffs[year]}%     rawDiff:{totalDiffs[year]}\n")

f.close()

# RELEASE ME!!!!!!!