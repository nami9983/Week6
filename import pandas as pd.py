import pandas as pd
import requests

japan_eq = df[df["place"].str.contains("Japan", case=False, na=False)]
print(f"日本で発生した地震の数：{len(japan_eq)}件")

max_eq = df.loc[df["mag"].idxmax()]
print(f"最大マグニチュード：{max_eq['mag']}（場所：{max_eq['place']}／日時：{max_eq['time']}）")
