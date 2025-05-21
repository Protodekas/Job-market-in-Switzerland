# importing required packages
import pandas as pd

# === import and cleaning of the data ===
# loading files
data = pd.read_csv("raw-data/kof_data_export_2025-05-13_14_27_46.csv")
names = pd.read_csv("raw-data/kof_data_export_2025-05-13_14_30_15.csv")

# removing the unused columns from the data table
cols_ok = names["ts_key"].tolist()
data = data[["date"] + [col for col in data.columns if col in cols_ok]]

# correspondance dictionnary between data table and variable names table
corr_dict = dict(zip(names["ts_key"], names["Variable"]))

# rename the variables in the data table
data = data.rename(columns={col: corr_dict[col] for col in data.columns if col in corr_dict})

# diplaying the first lines and print the corrected csv data file
# print(data.head())
data.to_csv("corrected_data.csv", index=False)

# dividing data table in dataframes according to the groups
cantons = names[names["Grouped by"] == "Canton"]["Variable"].tolist()
jobs = names[names["Grouped by"] == "Occupation"]["Variable"].tolist()
industries = names[names["Grouped by"] == "Industry"]["Variable"].tolist()

cantons = data[["date"] + [col for col in data.columns if col in cantons]]
jobs = data[["date"] + [col for col in data.columns if col in jobs]]
industries = data[["date"] + [col for col in data.columns if col in industries]]

# === descriptive statistics ===
# stats by group
print("Cantons")
print(cantons.describe().transpose().round(2))

print(f"\nJobs")
print(jobs.describe().transpose().round(2))

print(f"\nIndustries")
print(industries.describe().transpose().round(2))
