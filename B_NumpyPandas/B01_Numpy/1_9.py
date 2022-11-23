# [실습9] 집계함수 & 마스킹연산
import numpy as np
matrix = np.arange(8).reshape((2,4))

# Q1. sum 함수로 matrix의 총 합계를 구해 출력
print("sum :", np.sum(matrix))

# Q2. max 함수로 matrix 중 최댓값을 구해 출력
print("max :", np.max(matrix))

# Q3. min 함수로 matrix 중 최솟값을 구해 출력
print("min :", np.min(matrix))

# Q4. mean 함수로 matrix의 평균값을 구해 출력
print("mean :", np.mean(matrix))

# Q5. sum 함수의 axis 매개변수로 각 열의 합을 구해 출력
print("각 열의 합 :", np.sum(matrix, axis=0))

# Q6. sum 함수의 axis 매개변수로 각 행의 합을 구해 출력
print("각 행의 합 :", np.sum(matrix, axis=1))

# Q7. std 함수로 matrix의 표준편차를 구해 출력
print("std :", np.std(matrix))

# Q8. 마스킹 연산을 이용하여 matrix 중 5보다 작은 수들만 추출하여 출력
print("matrix 중 5보다 작은 수만 출력 :\n", matrix[matrix<5])