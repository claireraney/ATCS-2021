import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/data.csv")
# print(df)
df["champsPerPlayoffs"] = df["Championships"]/df["Playoff Appearence"]

df["Playoff Appearence"].plot(kind="hist", title="Playoff Appearences", edgecolor='black')
df.plot.pie(y="Net Worth", labels=df["Sports Team"], figsize=(10,10))
df.plot.scatter(x="Playoff Appearence", y="Championships", title="Championships vs. Playoff Appearences", grid=True)
plt.show()