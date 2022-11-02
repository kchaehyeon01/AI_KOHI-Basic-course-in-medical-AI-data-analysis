# [실습2] 배열의 기초 (1)
import numpy as np

print("\n1차원 array")
array = np.arange(10)
print(array)

# Q1. array의 자료형 출력
print("\narray의 자료형 출력")
print(type(array))

# Q2. array의 차원 출력
print("\narray의 차원 출력")
print(array.ndim)

# Q3. array의 모양 출력
print("\narray의 모양 출력")
print(array.shape)

# Q4. array의 크기 출력
print("\narray의 크기 출력")
print(array.size)

# Q5. array의 dtype 출력
print("\narray의 dtype 출력")
print(array.dtype)

# Q6. array의 인덱스 5의 요소 출력
print("\narray의 인덱스 5의 요소 출력")
print(array[5])

# Q7. array의 인덱스 3의 요소부터 인덱스 5 요소까지 출력
print("\narray의 인덱스 3의 요소부터 인덱스 5 요소까지 출력")
print(array[3:6])