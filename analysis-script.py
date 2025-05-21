# importing required packages
import pandas as pd
import json
import matplotlib.pyplot as plt

# === import and cleaning of the data ===
# loading files
data = pd.read_csv("original_data/kof_data_export_2025-05-13_14_27_46.csv")
names = pd.read_csv("original_data/kof_data_export_2025-05-13_14_30_15.csv")

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
# print("Cantons")
# print(cantons.describe().transpose().round(2))

# print(f"\nJobs")
# print(jobs.describe().transpose().round(2))

# print(f"\nIndustries")
# print(industries.describe().transpose().round(2))

# # saving stats in a json file
# desc_dict = {
#     "Cantons" : cantons.describe().transpose().round(2).to_dict(orient="index"),
#     "Jobs" : jobs.describe().transpose().round(2).to_dict(orient="index"),
#     "Industries" : industries.describe().transpose().round(2).to_dict(orient="index")
# }

# with open("json_files/desc_stats.json", "w") as f:
#     json.dump(desc_dict, f, indent=4)


# === plotting the data ===
cantons["date"] = pd.to_datetime(cantons["date"])
cantons.set_index("date").plot(figsize=(14,6))
plt.title("Evolution of job posting index by canton (2020 = 100)")
plt.ylabel("Index")
plt.grid(True)
plt.legend(bbox_to_anchor = (1.05, 1), loc = "upper left")
plt.tight_layout()
plt.show()
