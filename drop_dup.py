import pandas as pd

df = pd.read_csv("test.csv")
df = df.drop_duplicates()
df["nearest_station"] = df["nearest_station"].map(lambda x: x.split(" ")[0])
df.to_csv("wine_tabelog.csv", index=False)
