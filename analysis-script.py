# importing required packages
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

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
cantons_cols = names[names["Grouped by"] == "Canton"]["Variable"].tolist()
jobs_cols = names[names["Grouped by"] == "Occupation"]["Variable"].tolist()
industries_cols = names[names["Grouped by"] == "Industry"]["Variable"].tolist()

cantons = data[["date"] + [col for col in data.columns if col in cantons_cols]]
jobs = data[["date"] + [col for col in data.columns if col in jobs_cols]]
industries = data[["date"] + [col for col in data.columns if col in industries_cols]]

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
# index by canton
colors = sns.color_palette("Set1", 9) + sns.color_palette("Set2", 4) + sns.color_palette("Dark2", 8) + sns.color_palette("Paired", 5)
colors[5] = sns.color_palette("tab20b")[1]

cantons["date"] = pd.to_datetime(cantons["date"])
plt.figure(figsize=(16,8))
for i, col in enumerate(cantons_cols):
    plt.plot(cantons["date"], cantons[col], label=col, color=colors[i], linewidth=1)
plt.title("Evolution of job posting index by canton")
plt.ylabel("Index (1st week 2020 = 100)")
plt.xlabel("Time")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05,1), loc="upper left", fontsize="small")
plt.tight_layout()
plt.show()

# index by jobs
colors = sns.color_palette("tab10")

jobs["date"] = pd.to_datetime(jobs["date"])
plt.figure(figsize=(16,8))
for i, col in enumerate(jobs_cols):
    plt.plot(jobs["date"], jobs[col], label=col, color=colors[i], linewidth=1)
plt.title("Evolution of job posting index by job")
plt.ylabel("Index (1st week 2020 = 100)")
plt.xlabel("Time")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05,1), loc="upper left", fontsize="small")
plt.tight_layout()
plt.show()

# index by industry
colors = sns.color_palette("tab20")

industries["date"] = pd.to_datetime(industries["date"])
plt.figure(figsize=(16,8))
for i, col in enumerate(industries_cols):
    plt.plot(industries["date"], industries[col], label=col, color=colors[i], linewidth=1)
plt.title("Evolution of job posting index by industry")
plt.ylabel("Index (1st week 2020 = 100)")
plt.xlabel("Time")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05,1), loc="upper left", fontsize="small")
plt.tight_layout()
plt.show()
