# [실습5] Reshape & 이어붙이고 나누기 (2)
import numpy as np
print("matrix")
matrix = np.array([[0,1,2,3],
                   [4,5,6,7]])
print(matrix)
print("shape :", matrix.shape, "\n")

# Q1. 주어진 matrix 두 개를 세로로 이어붙이고 m이라는 변수에 저장하여 출력
m = np.concatenate([matrix,matrix], axis=0)
print(m)

# Q2. 주어진 matrix 변수 두 개를 가로로 이어붙이고 n이란 변수에 저장하여 출력
n = np.concatenate([matrix,matrix], axis=1)
print(n)