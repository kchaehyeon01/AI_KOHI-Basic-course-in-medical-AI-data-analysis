# 범례 & 축 경계 조정
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
fig, ax = plt.subplots()
ax.plot(x,np.sin(x),label="sin(x)") # 범례 이름 지정
ax.plot(x,np.cos(x),label="cos(x)") # 범례 이름 지정

# 축 경계 조정
ax.set_xlim(0,10)      # x축 시작 & 끝 지정
ax.set_ylim(-1.5,1.5)  # y축 시작 & 끝 지정

# 범례
ax.legend(
    loc="upper right", # 위치 지정
    shadow=True,       # 그림자
    fancybox=True,     # 둥근 모서리
    borderpad=3        # 빈칸
)

plt.show()