import pandas as pd

# loading files
data = pd.read_csv("raw-data/kof_data_export_2025-05-13_14_27_46.csv")
names = pd.read_csv("raw-data/kof_data_export_2025-05-13_14_30_15.csv")

# correspondance dictionnary between data table and variable names table
corr_dict = dict(zip(names["ts_key"], names["Variable"]))

# rename the variables in the data table
data_renamed = data.rename(columns={col: corr_dict[col] for col in data.columns if col in corr_dict})

# diplaying the first lines and print the corrected datafile
# print(f"raw-data/kof_data_export_2025-05-13_14_27_46.csv\n", data.head())
# print(f"raw-data/kof_data_export_2025-05-13_14_30_15.csv\n", names.head())
print(data_renamed.head())
data_renamed.to_csv("corrected_data.csv", index=False)
