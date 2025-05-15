import pandas as pd

# loading files
data = pd.read_csv("raw-data/kof_data_export_2025-05-13_14_27_46.csv")
corr_dic = pd.read_csv("raw-data/kof_data_export_2025-05-13_14_30_15.csv")

# diplaying the first lines
print(f"raw-data/kof_data_export_2025-05-13_14_27_46.csv\n", data.head())
print(f"raw-data/kof_data_export_2025-05-13_14_30_15.csv\n", corr_dic.head())
