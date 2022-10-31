import numpy as np
# 배열 만들기 ==================================================================

# 1차원 array 객체
print("\n-- np.array([1,2,3,4,5]) -------------------")
arr1d = np.array([1,2,3,4,5])
print(arr1d) # [1 2 3 4 5]

# 2차원 array 객체
print("\n-- np.array([[1,2],[3,4]]) -----------------")
arr2d = np.array([[1,2],[3,4]])
print(arr2d) # [[1 2] [3 4]]

# 배열 dtype =================================================================

# array -> 단일 type으로 구성
print("\n-- 여러 type일 경우 ---------------------------")
arrtypes = np.array([True, 1, 5.2])
print(arrtypes) # [1.  1.  5.2] -> 하나로 맞춰져버림!

# dtype 지정
print("\n-- np.array([1,2,3,4], dtype='float')-------")
arrd = np.array([1,2,3,4], dtype='float')
print(arrd) # [1. 2. 3. 4.]
print("dtype : ", arrd.dtype) # dtype :  float64
print("=> astype(int) : ", arrd.astype(int)) # => astype(int) :  [1 2 3 4]

# int & float -> float (전부 실수형으로 바뀜)
print("\n-- np.array([3, 1.4, 2, 3, 4]) -------------")
print(np.array([3, 1.4, 2, 3, 4])) # [3.  1.4 2.  3.  4. ] -> 모두 실수형으로 맞춰짐!

# 다양한 배열 만들기 ============================================================
print("\n-- 다양한 배열 만들기 --------------------------")
# np.zeros()
arr0s = np.zeros(10, dtype=int)
print(arr0s)

# np.ones()
arr1s = np.ones((3,5), dtype=float)
print(arr1s)

# np.arange()
arrarange = np.arange(0,20,2)
print(arrarange) # [ 0  2  4  6  8 10 12 14 16 18]

# np.linspace()
arrlinsp = np.linspace(0,1,5)
print(arrlinsp) # [0.   0.25 0.5  0.75 1.  ]

# 난수로 채워진 배열 만들기 =======================================================
print("\n-- 난수로 채워진 배열 만들기 --------------------")

# random
arrrandom = np.random.random((2,2))
print(arrrandom)

# 정규분포 : 평균, 표준편차, shape
arrnormal = np.random.normal(0, 1, (2,2))
print(arrnormal)

# randint
arrrandint = np.random.randint(0,10,(2,2))
print(arrrandint)
print(arrrandint.ndim) # 2 : 행렬의 차원
print(arrrandint.size) # 4 : 원소 개수
print(arrrandint.shape) # (2, 2)
print(arrrandint.dtype) # int64