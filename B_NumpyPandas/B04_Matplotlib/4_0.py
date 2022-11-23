# 그래프 여러개 겹쳐서 그리기
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x**2)
y4 = np.cos(x**2)

fig, axes = plt.subplots(2,1)

axes[0].plot(x,y1)
axes[0].plot(x,y2)
axes[0].set_title("axes[0]")

axes[1].plot(x,y3)
axes[1].plot(x,y4)
axes[1].set_title("axes[1]")

plt.show()