# 역대 월드컵의 관중 수 출력하기
import pandas as pd
import matplotlib.pyplot as plt

# WorldCups.csv파일을 pandas의 DataFrame으로 만들어보세요 : 변수 world_cups에 WorldCups.csv를 데이터 프레임으로 저장
world_cups = pd.read_csv("WorldCups.csv")

# 만든 데이터 프레임의 칼럼 중 Year와 Attendance 칼럼만 추출하여 출력해보세요.
world_cups = world_cups[['Year','Attendance']]
print(world_cups)

# world_cups를 이용하여 역대 월드컵의 평균 관중 수를 그래프로 출력해보도록 하겠습니다.
fig, ax = plt.subplots()
ax.plot(world_cups['Year'],world_cups['Attendance'],marker="o", color="black")
ax.set_xlabel("Year")
ax.set_ylabel("Attendance")
plt.show()

# 또는
plt.plot(world_cups['Year'], world_cups['Attendance'], marker='o', color='black')
plt.show()