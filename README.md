

![Screenshot 2024-11-10 135846](https://github.com/user-attachments/assets/66baea72-f700-442b-b0fa-742600d95c47)

# Future EV Demand Impact on Energy and Emissions
Authors: Daniel Huynh, Duy Lam, Yagna Patel, and Kevin Yu

## Problem
This project analyzes how the transition from Gasoline Vehicles to Electric Vehicles (EVs) affects carbon emissions across the United States. By projecting future EV adoption rates and their corresponding energy demands, we identify optimal solutions to implement renewable energy infrastructure to support a carbon neutral world.

## Statement
This information can be used to develop and implement Renewable Energy policies that encourage a carbon neutral world. Governments can use this model to plan their budgets and see where more investments into renewable energy may be needed to meet challenges created from increasing EV demand.

## Project Impact

Policy Development
- Support creation of effective renewable energy policies
- Identify regions requiring immediate infrastructure investment

Resource Allocation
- Help governments optimize budget allocation for renewable and EV infrastructure
- Prioritize high-impact areas for renewable energy development
- Plan strategic grid and EV charging upgrades based on projected EV demand

Environmental Planning
- Track progress toward carbon neutrality goals
- Identify regions where emissions may increase without intervention

## Usage
To use this program, follow these steps:

- In terminal, run the command `pip install -r -requirements.txt`
- 
- run `dashboard.py` and click the local host link outputted in the terminal
- 
- Adjust the slider to change the prediction year for plots and state maps
- 
- Select from a drop down menu to see specific data for an individual state
- 
- For 3d map, you can rotate the map via `command + click` or `ctrl + click`

## Additional Details

## Limits

## Strengths

## Exapansions

## Complexity
**Time Complexity and Space Complexity for Each Function and Operation** //Approximates

Most of the functions are time complexity of O(n) with half coming from data analysis and half coming from plotting functions dynamically

data1Extraction.py:

- `extract_co2_emissions` function: Time: O(n) Space: O(n)

- `extract_annual_generation` function: Time: O(n) Space: O(n)

- `calculate_co2_per_wh` function: Time: O(n²) Space: O(n)

- `process_ev_sales_data` function: Time: O(n) Space: O(n)

data2Regressions.py:
k = prediction year
- `calculate_registration_trend` function: Time: O(n + k) Space: O(n + k)

- `calculate_growth_rate` function: Time: O(n + k) Space: O(n + k)

- `calculate_co2_per_wh` function: Time: O(n + k) Space: O(n + k)

- `calculate_ev_demand` function: Time: O(n + k) Space: O(n + k)

- `calculate_ev_emissions` function: Time: O(n + k) Space: O(n + k)

data3Models.py:

- `plot_registration_trend function` function: Time: O(n), Space: O(n)
  
- `plot_growth_rate` function: Time: O(n), Space: O(n)
  
- `plot_co2_emissions` function: Time O(n), Space: O(n)
  
- `plot_ev_demand` function: Time: O(n), Space: O(n)
  
- `plot_ev_emissions` function: Time: O(n), Space: O(n)
  
- `plot_ev_gas_proportion` function: Time: O(n), Space: O(n)

GeoData1Analysis.py:

- `generate_emissions_projection` function: Time: O(n) Space: O(n)

GeoData2Models.py:

- `create_3d_state_map` function: Time: O(n) Space: O(n)

- `create_3d_county_map` function: Time: O(n) Space: O(n)

GeoData3Generation.py:

- `load_state_data` function: Time: O(n) Space: O(n)

- `calculate_state_emissions_data` function: Time: O(n) Space: O(n)

Dashboard.py:

- `generate_emissions_projection` function: Time: O(n) Space: O(n)

- `generate_ev_emissions_percent_change_projection` function: Time: O(n) Space: O(n)

- `create_3d_state_map` function: Time: O(n) Space: O(n)

- `ev_registration_plot` function: Time: O(n) Space: O(n)

- `co2_plot` function: Time: O(n) Space: O(n)

- `ev_demand_plot` function: Time: O(n) Space: O(n)

- `ev_emissions_plot` function: Time: O(n) Space: O(n)

- `map_view` function: Time: O(n) Space: O(n)

- `percent_map_view` function: Time: O(n) Space: O(n)




## Citations

https://www.eia.gov/environment/emissions/carbon/

https://www.eia.gov/energyexplained/electricity/electricity-in-the-us-generation-capacity-and-sales.php?os=http

https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle

https://afdc.energy.gov/vehicle-registration

