# 토끼와 거북이의 시간별 위치를 그래프로 시각화
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_the_hare_and_the_tortoise.csv")

fig, ax = plt.subplots()

ax.plot(df["시간"],df["토끼"],label="Rabbit",color="pink")
ax.plot(df["시간"],df["거북이"],label="Turtle",color="green")
ax.legend(loc="upper left",shadow=True,fancybox=True,borderpad=2)

plt.show()