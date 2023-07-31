import pandas as pd

# Load the CSV file
input_file = "/Users/femisokoya/Documents/GitHub/road-collisions/road-collision-result.csv"
df = pd.read_csv(input_file)

# Melt the dataframe
melted_df = pd.melt(
    df,
    id_vars=["Year", "Country Code", "Region or country"],
    value_vars=[
        "Fatal collisions",
        "Serious collisions (unadjusted) ",
        "Serious collisions (adjusted)",
        "Slight collisions (unadjusted)",
        "Slight collisions (adjusted)",
        "Total collisions",
        "Killed",
        "Seriously injured (unadjusted) ",
        "Seriously injured (adjusted)",
        "Killed or seriously injured (KSI) unadjusted",
        "Killed or seriously injured (KSI) adjusted",
        "Slightly injured (unadjusted)",
        "Slightly injured (adjusted)",
        "Total casualties",
    ],
    var_name="Occurence",
    value_name="Observation",
)

# Save the melted dataframe to CSV
output_file = "road-collision-melt.csv"
melted_df.to_csv(output_file, index=False)
