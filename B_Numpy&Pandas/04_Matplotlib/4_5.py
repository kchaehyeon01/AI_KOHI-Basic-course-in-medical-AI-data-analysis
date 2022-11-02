import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data_pokemon.csv")

print(df)

fig, ax = plt.subplots()

fire = df[(df["Type 1"] == "Fire") | (df["Type 2"] == "Fire")]
water = df[(df["Type 1"] == "Water") | (df["Type 2"] == "Water")]

ax.scatter(fire["Attack"],fire["Defense"],label="Fire",
           marker="*", color="r",s=50)
ax.scatter(water["Attack"],water["Defense"],label="Water",
           marker="o", color="b", s=10)

ax.set_xlabel("Attack")
ax.set_ylabel("Defense")
ax.legend(loc="upper right")

plt.show()