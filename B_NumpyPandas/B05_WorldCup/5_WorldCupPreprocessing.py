# 월드컵 매치 데이터 전처리
import pandas as pd
import matplotlib.pyplot as plt

world_cups_matches = pd.read_csv("WorldCupMatches_un.csv")

# 데이터 전처리를 위해 데이터 프레임의 일부 값을 replace 함수를 사용해 교체해줍니다.
world_cups_matches = world_cups_matches.replace('Germany FR', 'Germany')
world_cups_matches = world_cups_matches.replace("C�te d'Ivoire","Côte d'Ivoire")
world_cups_matches = world_cups_matches.replace("rn”>Bosnia and Herzegovina","Bosnia and Herzegovina")
world_cups_matches = world_cups_matches.replace("rn”>Serbia and Montenegro","Serbia and Montenegro")
world_cups_matches = world_cups_matches.replace("rn”>Trinidad and Tobago","Trinidad and Tobago")
world_cups_matches = world_cups_matches.replace("rn”>United Arab Emirates","United Arab Emirates")
world_cups_matches = world_cups_matches.replace("Soviet Union","Russia")

# 데이터 프레임에 중복된 데이터가 얼마나 있는지 확인할 수 있습니다.
dupli = world_cups_matches.duplicated()
print(len(dupli[dupli==True]))

# 중복값 제거
world_cups_matches = world_cups_matches.drop_duplicates()