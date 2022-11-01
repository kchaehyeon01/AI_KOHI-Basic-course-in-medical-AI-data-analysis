# 그래프 여러 개 그리기
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi*4, 100) # 0부터 4pi까지 100개의 균등한 구간
fig, axes = plt.subplots(2,1) # 한 fig(도화지)에 몇 개 그릴지 옵션 지정 -> 1개 fig에 2개 이상 그래프 그릴 수 있음
axes[0].plot(x,np.sin(x))
axes[1].plot(x,np.cos(x))

plt.show()