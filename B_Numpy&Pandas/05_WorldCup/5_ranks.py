# 월드컵 4강 이상 성적 집계하기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# WorldCups.csv 을 데이터 프레임으로 만든 변수 world_cups가 주어졌습니다.
# 데이터 프레임에서 역대 대회 1위 국가, 2위 국가, 3위 국가, 4위 국가를 추출하여 각각 변수 winner, runners_up, third, fourth에 저장하도록 하겠습니다.
world_cups = pd.read_csv("WorldCups.csv")
winner = world_cups['Winner']
runners_up = world_cups['Runners-Up']
third = world_cups['Third']
fourth = world_cups['Fourth']

# value_counts 함수를 이용해 각 시리즈 데이터에 저장된 값을 세어주고 저장합니다.
winner_count = pd.Series(winner.value_counts())
runners_up_count = pd.Series(runners_up.value_counts())
third_count = pd.Series(third.value_counts())
fourth_count = pd.Series(fourth.value_counts())

# 위 데이터들을 하나의 데이터 프레임으로 합치도록 하겠습니다.
ranks = pd.DataFrame({
  "Winner" : winner_count,
  "Runners_Up" : runners_up_count,
  "Third" : third_count,
  "Fourth" : fourth_count
})

# ranks에 들어있는 값이 NaN이라면, 해당 순위를 기록한 적이 없다는 의미입니다.
# 따라서 데이터의 결측값을 0으로 채우고, dtype을 int64로 다시 설정합니다.
ranks = ranks.fillna(0).astype("int64")

# 각 국가들을 우승 횟수, 준우승 횟수, 3위 횟수, 4위 횟수 순서대로 내림차순 정렬하세요.
ranks = ranks.sort_values(["Winner","Runners_Up","Third","Fourth"],ascending=False)
print(ranks)


# 그래프 그리기
# x축에 그려질 막대그래프들의 위치입니다.
x = np.array(list(range(0, len(ranks))))

# 그래프를 그립니다.
fig, ax = plt.subplots()

# x 위치에, 항목 이름으로 ranks.index(국가명)을 붙입니다.
plt.xticks(x, ranks.index, rotation=90)
plt.tight_layout()

# 4개의 막대를 차례대로 그립니다.
ax.bar(x - 0.3, ranks['Winner'],     color = 'gold',   width = 0.2, label = 'Winner')
ax.bar(x - 0.1, ranks['Runners_Up'], color = 'silver', width = 0.2, label = 'Runners_Up')
ax.bar(x + 0.1, ranks['Third'],      color = 'brown',  width = 0.2, label = 'Third')
ax.bar(x + 0.3, ranks['Fourth'],     color = 'black',  width = 0.2, label = 'Fourth')

plt.show()

# ranks 데이터에서 직접 plot 함수 호출
ranks.plot(y=["Winner", "Runners_Up", "Third", "Fourth"],
    kind="bar", 
    color=['gold', 'silver', 'brown', 'black'], 
    figsize=(15,12),
    fontsize=10, 
    width=0.8,
    align='center')
plt.show()