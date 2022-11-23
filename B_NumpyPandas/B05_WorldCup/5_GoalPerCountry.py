# 국가 별 득점 수 구하기 : 각 국가들이 기록한 득점 수를 내림차순으로 정렬한 결과를 출력해보세요.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

world_cups_matches = pd.read_csv("WorldCupMatches.csv")

# 전처리를 거친 데이터 프레임에서 홈 팀 득점을 나타내는 home 데이터 프레임과, 어웨이 팀 득점을 나타내는 away 데이터 프레임을 각각 만들어보고자 합니다.
# Home Team Name으로 그룹을 묶고, Home Team Goals 칼럼을 추출하여 home에 저장합니다.
# Away Team Name으로 그룹을 묶고, Away Team Goals 칼럼을 추출하여 away에 저장합니다.
home = world_cups_matches.groupby(['Home Team Name'])['Home Team Goals'].sum()
away = world_cups_matches.groupby(['Away Team Name'])['Away Team Goals'].sum()

# concat 메소드를 이용하여 home, away 데이터 프레임을 하나로 합치고, goal_per_country라는 새로운 데이터프레임에 저장하도록 하겠습니다.
# 그리고 결측값을 제거하기 위해 fillna 함수를 적용합니다.
goal_per_country = pd.concat([home, away], axis=1, sort=True).fillna(0)

# goal_per_country 데이터 프레임에 새로운 칼럼 “Goals”를 만들도록 하겠습니다.
# Home Team Goals와 Away Team Goals 를 덧셈 연산한 값을 Goals에 저장합니다.
goal_per_country['Goals'] = goal_per_country['Home Team Goals'] + goal_per_country['Away Team Goals']

# goal_per_country 에서 Goals 칼럼만 추출하고, 내림차순으로 정렬합니다. (이 때, goal_per_country는 시리즈 데이터가 됩니다.)
goal_per_country = goal_per_country['Goals'].sort_values(ascending=False)

# 저장된 값의 dtype를 정수형으로 바꿉니다.
goal_per_country = goal_per_country.astype(int)

print(goal_per_country)

# 상위 10개 국가만 골라 출력합니다.
fig, ax = plt.subplots()
ax.bar(goal_per_country.index[:10], goal_per_country.values[:10], width=0.5)
plt.xticks(goal_per_country.index[:10], rotation=30) # x축 항목 이름 지정, 국가 이름 겹침 : rotation option (30도 회전)
plt.tight_layout() # 글자가 넘쳐서 잘리는 현상 방지
plt.show()

# Series 데이터에서도 직접 plot 함수 호출 가능
goal_per_country[:10].plot(x=goal_per_country.index, y=goal_per_country.values, kind="bar", figsize=(12, 12), fontsize=14)
plt.show()