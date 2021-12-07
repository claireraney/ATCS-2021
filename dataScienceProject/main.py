from typing import List
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick

# Career statistics for top 50 3pt shooters
df = pd.read_csv("Final Shooting Stats V2 - career totals.csv")

# Statistics by season for top 10 3pt shooters
df2 = pd.read_csv("Full Shooting Stats - top10.csv")

# charts to effective percentages
# 3pt percentage chart
# Steph in blue, everyone else in yellow
df['color'] = ["blue" if df.iloc[i]["Player"] == 'Stephen Curry' else "yellow" for i in range(len(df))]
# sort based on 3P%
df_sorted = df.sort_values('3P%', ascending=False)
plt.bar('Player', '3P%', data=df_sorted, color=df_sorted['color'])
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
df_sorted.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
plt.ylim(0.3, 0.45)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career 3 Point FG Percentage', size=15)
plt.grid(axis='y')
plt.show()

# FT chart
# sort based on FT%
df_sorted = df.sort_values('FT%', ascending=False)
plt.bar('Player', 'FT%', data=df_sorted, color=df_sorted['color'])
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
df_sorted.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
plt.ylim(0.6, 0.95)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career FT Percentage', size=15)
plt.grid(axis='y')
plt.show()

# 2FG chart
# sort based on 2FG%
df_sorted = df.sort_values('2FG%', ascending=False)
# Steph in blue, guards in lightblue, forwards in lightgrey
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
df_sorted.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
plt.ylim(0.4, 0.56)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career 2FG Percentage', size=15)
plt.grid(axis='y')
plt.show()

# FG chart
# sort based on FG%
df_sorted = df.sort_values('FG%', ascending=False)
# Steph in blue, guards in lightblue, forwards in lightgrey
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
df_sorted.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
plt.ylim(0.4, 0.52)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career FG Percentage', size=15)
plt.grid(axis='y')
plt.show()

# EFG chart
# sort based on EFG%
df_sorted = df.sort_values('EFG%', ascending=False)
plt.bar('Player', 'EFG%', data=df_sorted, color=df_sorted['color'])
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
df_sorted.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
plt.ylim(0.45, 0.59)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career EFG Percentage', size=15)
plt.grid(axis='y')
plt.show()

# TS chart
# sort based on TS%
df_sorted = df.sort_values('TS%', ascending=False)
plt.bar('Player', 'TS%', data=df_sorted, color=df_sorted['color'])
df_sorted = plt.gca()
df_sorted.xaxis.set_ticklabels([])
df_sorted.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
plt.ylim(0.5, 0.64)
plt.xlabel('Top 50 3 Point Shooters of All-time', size=15)
plt.ylabel('Career TS Percentage', size=15)
plt.grid(axis='y')
plt.show()

# Histogram of 50/40/90 Club
plt.hist(df['50/40/90 Season'], bins=3, align="mid")
plt.xlabel('Did the Player Have a 50/40/90 Season?', size=15)
plt.ylabel('Count', size=15)
plt.grid(axis='y')
plt.show()

# Boxplot 3PM/GAME
data1 = []
# top 10 3P shooters
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
plt.xticks(rotation=20)
plt.grid(axis='y')
plt.ylabel('Season 3PM/Game', size=15)

# steph in blue, everyone else in yellow
bpcolors = ["yellow", "blue", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow"]
for patch, color in zip(bp['boxes'], bpcolors):
    patch.set_facecolor(color)

plt.show()

#Cumulative 3PM Line Graph (two color)
# steph in blue, everyone else in yellow
palette = {"Stephen Curry": "blue"}
for name in df2["Name"]:
    if name != "Stephen Curry":
        palette[name] = "yellow"

g = sns.relplot(data=df2, x="Year", y="Cumulative 3PM", hue="Name", kind="line", palette = palette, legend=False)
plt.show()

#Cumulative 3PM Line Graph (multi-color)
# steph in blue
palette = ["green", "blue", "yellow", "red", "black", "orange", "cyan", "purple", "grey", "pink"]
g = sns.relplot(data=df2, x="Year", y="Cumulative 3PM", hue="Name", kind="line", palette = palette)
plt.show()