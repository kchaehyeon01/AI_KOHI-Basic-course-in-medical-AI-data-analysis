# [실습3] 배열의 기초 (2)
import numpy as np

print("2차원 array")
matrix = np.arange(1,16).reshape(3,5) # 1부터 15까지 들어있는 (3,5)짜리 배열을 만듦
# matrix = np.arange(1,16).reshape(3,-1) # 해도 됨 -> -1 : 알아서 해라
print(matrix)

# Q1. matrix의 자료형을 출력해보세요.
print("자료형 :", type(matrix))

# Q2. matrix의 차원을 출력해보세요.
print("차원 :", matrix.ndim)

# Q3. matrix의 모양을 출력해보세요.
print("모양 :", matrix.shape)

# Q4. matrix의 크기를 출력해보세요.
print("크기 :", matrix.size)

# Q5. matrix의 dtype(data type)을 출력해보세요.
print("dtype :", matrix.dtype)

# Q6. matrix의 (2,3) 인덱스의 요소를 출력해보세요.
print("(2,3) 인덱스의 요소 ([2,3]):", matrix[2,3])
print("(2,3) 인덱스의 요소 ([2][3]):", matrix[2][3])

# Q7. matrix의 행은 인덱스 0부터 인덱스 1까지, 열은 인덱스 1부터 인덱스 3까지 출력해보세요.
print(matrix[0:2,1:4])


print("이렇게 하면 다름... 주의")
print(matrix[0:2])
print(matrix[0:2][1:4]) # 틀림 : 1차원 배열을 요소로 인식한 것

# 1차원 배열을 요소로 인식했다는 것이 확실
print("\nTEST----------")
testmatrix = np.arange(1,26).reshape(-1,5)
print(testmatrix)
print(testmatrix[:,1:4])
print(testmatrix[:][1:4])