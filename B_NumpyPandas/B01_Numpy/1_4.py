# [실습4] Reshape & 이어붙이고 나누기 (1)
import numpy as np

print("array")
array = np.arange(8)
print(array)
print("shape : ", array.shape, "\n")

# Q1. array를 (2,4) 크기로 reshape하여 matrix에 저장한 뒤 matrix와 그의 shape을 출력
print("# reshape (2,4)")
matrix = array.reshape(2,4)
print(matrix)
print("shape : ", matrix.shape)