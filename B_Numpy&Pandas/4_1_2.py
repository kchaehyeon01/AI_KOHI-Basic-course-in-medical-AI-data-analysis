# Object Oriented Interface
import matplotlib.pyplot as plt

x = list(range(6))
y = list(range(6))

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_title("First Plot : Object Oriented Interface")
ax.set_xlabel("x")
ax.set_ylabel("y")

fig.set_dpi(300)
fig.savefig("fitst_plot.png")

plt.show()

