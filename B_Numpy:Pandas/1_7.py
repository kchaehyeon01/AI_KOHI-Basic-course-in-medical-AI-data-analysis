# [실습7] Numpy 연산
import numpy as np

array = np.array([1,2,3,4,5])
# array = np.arange(1,6) # 동일

array2 = np.array([5,4,3,2,1])
# array2 = np.arange(5,0,-1) # 동일

print(array)
print(array2)

# Q1. array + 5
print(array+5)

# Q2. array -5
print(array-5)

# Q3. array * 5
print(array*5)

# Q4. array / 5
print(array/5)

# Q5. array + array2
print(array+array2)

# Q6. array - array2
print(array-array2)