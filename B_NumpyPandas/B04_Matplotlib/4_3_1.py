import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x,x**2,
    marker="o",
    markersize=15,
    markerfacecolor="black", # 원 안쪽 색
    markeredgecolor="blue"   # 원 테두리 색
)
plt.show()