import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,3)

# Bar plot
x1 = np.arange(10)
axes[0].set_title("Bar plot")
axes[0].bar(x1,x1*2)

# Bar plot 누적
x = np.random.rand(3)
y = np.random.rand(3)
z = np.random.rand(3)
data = [x,y,z]
x_ax = np.arange(3)
axes[1].set_title("Bar plot accumulate")
for i in x_ax:
    axes[1].bar(x_ax, data[i],
    bottom=np.sum(data[:i], axis=0))
axes[1].set_xticks([-1,0,1,2,3]) # x축 값 지정
axes[1].set_xticklabels(["-1","0","1","2","3"]) # x축 값의 label 지정

# Histogram
data = np.random.randn(1000)
axes[2].set_title("Histogram (bins=50)")
axes[2].hist(data,bins=10) # bins : 막대기 수

plt.show()