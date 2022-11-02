# option 1 : linestyle
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
fig, ax = plt.subplots()

ax.plot(x,x+6,linestyle="-")  # solid
ax.plot(x,x+4,linestyle="--") # dashed
ax.plot(x,x+2,linestyle="-.") # dashdot
ax.plot(x,x,linestyle=":")    # dotted

plt.show()