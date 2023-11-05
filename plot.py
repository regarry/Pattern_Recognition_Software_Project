import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3)
df = pd.read_csv("iriscorrected.csv")
# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()