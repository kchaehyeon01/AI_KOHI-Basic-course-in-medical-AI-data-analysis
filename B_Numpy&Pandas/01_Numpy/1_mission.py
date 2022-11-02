# [미션] 양치기 소년의 거짓말 횟수 구하기
daily_liar_data = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
# 주어진 daily_liar_data 배열 : 양치기 소년이 100일동안 한 말을 정리한 배열
# 진실을 이야기했으면 1, 거짓말을 했으면 0으로 기록되어 있음
# 100일 간 얼마나 거짓말을 했는지 횟수를 세어 출력

import numpy as np
array = np.array(daily_liar_data)

# 방법 1
totday = array.size
trueday = np.sum(array)
liarday1 = totday-trueday
print(liarday1)

# 방법 2
lie = array-1
liarday2 = -np.sum(lie)
print(liarday2)