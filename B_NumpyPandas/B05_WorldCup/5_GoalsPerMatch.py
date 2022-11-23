# 역대 월드컵의 경기 당 득점 수
import pandas as pd
import matplotlib.pyplot as plt

# WorldCups.csv파일을 pandas의 DataFrame으로 만들어보세요
world_cups = pd.read_csv("WorldCups.csv")

# 만든 데이터 프레임의 칼럼 중 Year 와 GoalsScored, MatchesPlayed 칼럼만 추출해보세요.
world_cups = world_cups[['Year','GoalsScored','MatchesPlayed']]
print(world_cups)

# 데이터 프레임에 경기당 득점 수를 의미하는 새로운 칼럼 GoalsPerMatch를 추가합니다. GoalsPerMatch 의 값은 GoalsScored / MatchesPlayed입니다.
world_cups['GoalsPerMatch'] = world_cups['GoalsScored']/world_cups['MatchesPlayed']
print(world_cups)

fig, axes = plt.subplots(2,1, figsize=(4,8))

axes[0].plot(world_cups['Year'],world_cups['MatchesPlayed'],label="matches",color="blue",marker="o")
axes[0].bar(world_cups['Year'],world_cups['GoalsScored'],label="goals",color="gray")
axes[0].legend(loc="upper left",fancybox=True,)

axes[1].grid(True)
axes[1].plot(world_cups['Year'],world_cups['GoalsPerMatch'],label="goals_per_matches",color="r",marker="o")
axes[1].legend(loc="lower left",fancybox=True)

plt.show()