import pandas as pd

# Read the spreadsheet
file_path = '/Users/femisokoya/Documents/GitHub/road-collisions/road-collisions.xlsx'
worksheet_name = 'Collisions_and_cas_by_region'
df = pd.read_excel(file_path, sheet_name=worksheet_name)

# Delete rows 0 to 3 and make row 4 the column header
df.columns = df.iloc[2]
df = df[3:]

# Convert values in column 1 to the specified mapping
region_mapping = {
    "North East": "E12000001",
    "North West": "E12000002",
    "Yorkshire and Humberside": "E12000003",
    "East Midlands": "E12000004",
    "West Midlands": "E12000005",
    "Eastern": "E12000006",
    "South East": "E12000007",
    "London": "E12000008",
    "South West": "E12000009",
    "England": "E92000001",
    "Wales": "W92000004",
    "Scotland": "S92000003",
    "Great Britain": "K02000001",
}

# Assuming the region column name is 'RAS2013: Estimated number of reported drink drive collisions and casualties in Great Britain by country and English region',
# change it if different
region_column_name = 'Region or  country'

df[region_column_name] = df[region_column_name].map(region_mapping)


# Drop all blank columns
df.dropna(axis=1, how='all', inplace=True)

# Drop duplicate columns (keep the first occurrence)
df = df.loc[:, ~df.columns.duplicated()]

# Update the column headers
new_headers = {
    "Collision year": "Collision year",
    "Region or  country": "Region or country",
    "Fatal collisions": "Fatal collisions",
    "Serious collisions (unadjusted)": "Serious collisions (unadjusted)",
    "Serious collisions (adjusted) [note 3]": "Serious collisions (adjusted)",
    "Slight collisions (unadjusted)": "Slight collisions (unadjusted)",
    "Slight collisions (adjusted) [note 3]": "Slight collisions (adjusted)",
    "Total collisions [note 4]": "Total collisions",
    "Collision year": "Year",
    "Region or  country": "Country Code",
    "Killed": "Killed",
    "Seriously injured (unadjusted)": "Seriously injured (unadjusted)",
    "Seriously injured (adjusted) [note 3]": "Seriously injured (adjusted)",
    "Killed or seriously injured (KSI) unadjusted": "Killed or seriously injured (KSI) unadjusted",
    "Killed or seriously injured (KSI) adjusted [Note 3]": "Killed or seriously injured (KSI) adjusted",
    "Slightly injured (unadjusted)": "Slightly injured (unadjusted)",
    "Slightly injured (adjusted) [note 3]": "Slightly injured (adjusted)",
    "Total casualties [note 4]": "Total casualties"
}

df.rename(columns=new_headers, inplace=True)

# Save the result to road-collision-result.csv
output_file_path = 'road-collision-result.csv'
df.to_csv(output_file_path, index=False)
