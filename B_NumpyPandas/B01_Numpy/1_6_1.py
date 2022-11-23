# [실습6] Reshape & 이어붙이고 나누기 (3) 변형...
import numpy as np
print("matrix")
matrix = np.array([[0,1,2,3],
                   [4,5,6,7],
                   [8,9,10,11],
                   [12,13,14,15]])
print(matrix,"\n")

# 의문 1. 3개 split 가능?
a, b, c = np.split(matrix,[1,3],axis=0)
print("\na-----\n",a)
print("\nb-----\n",b)
print("\nc-----\n",c)