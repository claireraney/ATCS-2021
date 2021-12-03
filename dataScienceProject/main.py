from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("Final Shooting Stats V2 - career totals.csv")
df2 = pd.read_csv("Full Shooting Stats - top10.csv")

# charts to effective percentages
# 3pt percentage chart
df['color'] = ["blue" if df.iloc[i]["Player"] == 'Stephen Curry' else "yellow" for i in range(len(df))]
df_sorted = df.sort_values('3P%', ascending=False)
plt.bar('Player', '3P%', data=df_sorted, color=df_sorted['color'])
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
plt.ylim(0.3, 0.45)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career 3 Point FG Percentage', size=15)
plt.grid(axis='y')
plt.show()

# FT chart
df_sorted = df.sort_values('FT%', ascending=False)
plt.bar('Player', 'FT%', data=df_sorted, color=df_sorted['color'])
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
plt.ylim(0.6, 0.95)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career FT Percentage', size=15)
plt.grid(axis='y')
plt.show()

# 2FG chart
df_sorted = df.sort_values('2FG%', ascending=False)
col: List[str] = []
for index, row in df_sorted.iterrows():
    if row['Player'] == 'Stephen Curry':
        col.append('blue')
    elif row["Position"] == 'G':
        col.append('lightblue')
    else:
        col.append('lightgrey')

plt.bar('Player', '2FG%', data=df_sorted, color=col)
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
#df_sorted.yaxis_set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))
plt.ylim(0.4, 0.56)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career 2FG Percentage', size=15)
plt.grid(axis='y')
plt.show()

# FG chart
df_sorted = df.sort_values('FG%', ascending=False)
col: List[str] = []
for index, row in df_sorted.iterrows():
    if row['Player'] == 'Stephen Curry':
        col.append('blue')
    elif row["Position"] == 'G':
        col.append('lightblue')
    else:
        col.append('lightgrey')

plt.bar('Player', 'FG%', data=df_sorted, color=col)
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
#df_sorted.yaxis_set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))
plt.ylim(0.4, 0.52)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career FG Percentage', size=15)
plt.grid(axis='y')
plt.show()

# EFG chart
df_sorted = df.sort_values('EFG%', ascending=False)
plt.bar('Player', 'EFG%', data=df_sorted, color=df_sorted['color'])
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
#df_sorted.yaxis_set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))
plt.ylim(0.45, 0.6)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career EFG Percentage', size=15)
plt.grid(axis='y')
plt.show()

# TS chart
df_sorted = df.sort_values('TS%', ascending=False)
plt.bar('Player', 'TS%', data=df_sorted, color=df_sorted['color'])
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
#df_sorted.yaxis_set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))
plt.ylim(0.5, 0.65)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career TS Percentage', size=15)
plt.grid(axis='y')
plt.show()

# Boxplot 3PM/GAME
data1 = []
bplabels = ["Ray Allen", "Stephen Curry", "Reggie Miller", "James Harden", "Kyle Korver", "Vince Carter", "Jason Terry", "Jamal Crawford", "Paul Pierece", "Damian Lillard"]
for name in bplabels:
    data1.append((df2.loc[df2["Name"] == name, ["3PM/GAME"]]))
df1st = df2.loc[df2["Name"] == "Ray Allen"]
df2nd = df2.loc[df2["Name"] == "Stephen Curry"]
df3rd = df2.loc[df2["Name"] == "Reggie Miller"]
df4th = df2.loc[df2["Name"] == "James Harden"]
df5th = df2.loc[df2["Name"] == "Kyle Korver"]
df6th = df2.loc[df2["Name"] == "Vince Carter"]
df7th = df2.loc[df2["Name"] == "Jason Terry"]
df8th = df2.loc[df2["Name"] == "Jamal Crawford"]
df9th = df2.loc[df2["Name"] == "Paul Pierce"]
df10th = df2.loc[df2["Name"] == "Damian Lillard"]

data = [df1st["3PM/GAME"], df2nd["3PM/GAME"], df3rd["3PM/GAME"], df4th["3PM/GAME"], df5th["3PM/GAME"], df6th["3PM/GAME"], df7th["3PM/GAME"], df8th["3PM/GAME"], df9th["3PM/GAME"], df10th["3PM/GAME"]]
ax = plt.subplot()
bp = ax.boxplot(data, notch=True, patch_artist=True )
plt.xticks([1,2, 3, 4, 5, 6, 7, 8, 9, 10], bplabels)
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.ylabel('Season 3PM/Game', size=15)

bpcolors = ["yellow", "blue", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow"]
for patch, color in zip(bp['boxes'], bpcolors):
    patch.set_facecolor(color)

plt.show()

#Cummmulative 3PM Line Graph
palette = {"Stephen Curry": "blue"}
for name in df2["Name"]:
    if name != "Stephen Curry":
        palette[name] = "yellow"

g = sns.relplot(data=df2, x="Year", y="Cumulative 3PM", hue="Name", kind="line", palette = palette)
plt.show()