import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots()
x = np.arange(15) # 0부터 14까지
y = x**2
ax.plot(
    x, y,
    linestyle = ":", # option 1
    marker = "*",    # option 2
    color="#524FA1"  # option 3
)

plt.show()