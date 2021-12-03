import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/oldFaithful.csv")

x = df["wait_time"]
y = df["eruption_time"]

correlation = y.corr(x)
print(correlation)

plt.title("Old Faithful Eruptions")
plt.xlabel("Wait Time")
plt.ylabel("Eruption Time")
plt.scatter(x, y)

model = np.polyfit(x, y, 1)

x_lin_reg = range(x.min(), x.max())

predict = np.poly1d(model)

y_lin_reg = predict(x_lin_reg)

plt.plot(x_lin_reg, y_lin_reg, color="red")
print(model)


