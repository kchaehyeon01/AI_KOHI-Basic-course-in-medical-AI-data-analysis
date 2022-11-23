# size와 color를 각각 지정한 Scatter
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = np.random.randn(50) # 정규분포 50개
y = np.random.randn(50)
colors = np.random.randint(0,100,50)
sizes = 500*np.pi*np.random.rand(50)**2

ax.scatter(
    x,y,      # 점의 중앙 지점
    c=colors, # 숫자로 지정 (0~100)
    s=sizes,
    alpha=0.3 # 투명도
)

plt.show()