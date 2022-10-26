# [실습5] Reshape & 이어붙이고 나누기 (2) 변형...
import numpy as np
print("matrix")
matrix = np.array([[0,1,2,3],
                   [4,5,6,7]])

# 의문 1. 배열 3개도 붙일 수 있나?
triple1 = np.concatenate([matrix,matrix,matrix])
triple2 = np.concatenate([matrix,matrix,matrix],axis=0)
triple3 = np.concatenate([matrix,matrix,matrix],axis=1)
print("\ntriple1-----\n", triple1)
print("\ntriple2-----\n", triple2)
print("\ntriple3-----\n", triple3)

# 의문 2. axis default?
default = np.concatenate([matrix,matrix])
print("\ndefault-----\n", default)
# default=0 (공식 문서에도 써 있음)