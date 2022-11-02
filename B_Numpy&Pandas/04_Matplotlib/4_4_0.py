import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,2,figsize=(8,4))

# bar
x = np.arange(100)
y = np.random.randint(1,100,100)
axes[0].bar(x,y)

# hist
data = np.random.randn(1000)
axes[1].hist(data,bins=100)

plt.show()