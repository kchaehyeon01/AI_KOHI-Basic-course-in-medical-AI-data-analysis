# [실습6] Reshape & 이어붙이고 나누기 (3)
import numpy as np
print("matrix")
matrix = np.array([[0,1,2,3],
                   [4,5,6,7],
                   [8,9,10,11],
                   [12,13,14,15]])
print(matrix,"\n")

# Q1. 주어진 matrix를 axis=0을 활용하여 3번째 행을 기준으로 나누고, 
    # 그 결과를 a, b 변수에 각각 저장, 출력
a, b = np.split(matrix,[3],axis=0)
print("\na-----\n",a)
print("\nb-----\n",b)
# Q2. 주어진 matrix를 axis=1을 활용하여 1번째 열을 기준으로 나누고,
    # 그 결과를 c, d 변수에 각가 저장, 출력
c, d = np.split(matrix,[1],axis=1)
print("\nc-----\n",c)
print("\nd-----\n",d)