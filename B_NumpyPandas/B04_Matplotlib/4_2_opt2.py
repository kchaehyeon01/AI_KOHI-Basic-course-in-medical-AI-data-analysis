import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
fig, axes = plt.subplots(2,2)

axes[0,0].set_title(".,os")
axes[0,0].plot(x,x+6,marker=".") # 점
axes[0,0].plot(x,x+4,marker=",") # 픽셀
axes[0,0].plot(x,x+2,marker="o") # 원
axes[0,0].plot(x,x+0,marker="s") # 사각형

axes[0,1].set_title("v<^>")
axes[0,1].plot(x,x+6,marker="v") # 삼각형 1
axes[0,1].plot(x,x+4,marker="<") # 삼각형 2
axes[0,1].plot(x,x+2,marker="^") # 삼각형 3
axes[0,1].plot(x,x+0,marker=">") # 삼각형 4

axes[1,0].set_title("1234")
axes[1,0].plot(x,x+6,marker="1") # 삼각선 1
axes[1,0].plot(x,x+4,marker="2") # 삼각선 2
axes[1,0].plot(x,x+2,marker="3") # 삼각선 3
axes[1,0].plot(x,x+0,marker="4") # 삼각선 4

axes[1,1].set_title("pHh")
axes[1,1].plot(x,x+4,marker="p")
axes[1,1].plot(x,x+2,marker="H")
axes[1,1].plot(x,x+0,marker="h")

plt.show()