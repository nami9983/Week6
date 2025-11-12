import pandas as pd
import requests

japan_eq = df[df["place"].str.contains("Japan", case=False, na=False)]
print(f"日本で発生した地震の数：{len(japan_eq)}件")
