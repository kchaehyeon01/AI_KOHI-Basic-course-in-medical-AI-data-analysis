import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x,x+6,color="r")     # rgbcmyk
ax.plot(x,x+4,color="green") # full name
ax.plot(x,x+2,color="0.8")   # 0~1 str : grayscale
ax.plot(x,x,color="#524FA1") # RGB 16진수 코드

plt.show()