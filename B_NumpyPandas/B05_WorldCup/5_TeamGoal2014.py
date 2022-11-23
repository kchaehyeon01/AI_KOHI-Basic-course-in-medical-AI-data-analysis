# 2014 월드컵 다득점 국가 순위
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WorldCupMatches_2014.csv")

# 데이터 프레임에서 마스킹 연산을 이용하여 Year가 2014인 것들을 추출하세요.
world_cup_matches = df[df['Year']==2014]

# 2014년 월드컵 경기 데이터 중에서 홈 팀의 골 수와 원정 팀의 골 수를 각각 계산하려고 합니다.
# 데이터가 저장된 형태로 인해 홈 팀 데이터와 원정 팀 데이터를 각각 구한 뒤 합쳐주어야 합니다.
# Home Team Name을 그룹으로 묶어 Home Team Goals의 합계를 구하고 home_team_goal 변수에 저장합니다.
# Away Team Name을 그룹으로 묶어 Away Team Goals의 합계를 구하고 away_team_goal 변수에 저장합니다.
home_team_goal = world_cup_matches.groupby(['Home Team Name'])['Home Team Goals'].sum()
away_team_goal = world_cup_matches.groupby(["Away Team Name"])['Away Team Goals'].sum()

# 홈 득점 수와 원정 득점 수를 하나의 데이터로 합치겠습니다.
# 이 때, 결측값을 없애기 위해 fillna 함수를 적용합니다. 결측값이 존재한다는 것은, 골을 넣지 못했다는 의미이므로 0으로 대체합니다.
team_goal_2014 = pd.concat([home_team_goal,away_team_goal],axis=1).fillna(0)

# 홈 팀 골과 원정 팀 골 수를 합한 새로운 칼럼 goals를 만들고, 기존 칼럼은 drop 함수를 이용해 삭제합니다.
team_goal_2014['goals'] = team_goal_2014['Home Team Goals'] + team_goal_2014['Away Team Goals']
team_goal_2014 = team_goal_2014.drop(['Home Team Goals', 'Away Team Goals'], axis=1)

# 저장된 값을 정수로 변환합니다.
team_goal_2014.astype(int)

# 데이터 프레임을 내림차순으로 정렬하고, 올바른 값이 출력되는지 확인합니다.
team_goal_2014 = team_goal_2014['goals'].sort_values(ascending=False)

print(team_goal_2014)

# 1
fig, ax = plt.subplots()
ax.bar(team_goal_2014.index,team_goal_2014.values)
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()

# 2
team_goal_2014.plot(x=team_goal_2014.index, y=team_goal_2014.values, kind="bar", figsize=(12, 12), fontsize=14)
plt.show()