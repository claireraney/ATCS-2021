import pandas as pd

import matplotlib.pyplot as plt

netWorth = pd.Series([5140000000,
3200000000,
4700000000,
4180000000,
5000000000,
5250000000,
2250000000,
6500000000,
1340000000,
4050000000,
2750000000,
1400000000])

plt.boxplot(netWorth)
plt.show()