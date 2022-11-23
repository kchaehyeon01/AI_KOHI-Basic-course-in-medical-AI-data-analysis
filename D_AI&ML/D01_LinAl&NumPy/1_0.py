import numpy as np

print("\n[행렬 만들기]")
A = np.array([[1,2],[3,4]])

print("\n# A :\n",A)
print("\n# A * 3 :\n",A*3)
print("\n# A + A :\n",A+A)
print("\n# A - A :\n",A-A)

print("\n\n\n[element-wise operation : 행렬 내 원소에 대한 산술연산]")
print("\n# A ** 2 :\n",A**2)
print("\n# 3 ** A :\n",3**A)
print("\n# A - A :\n",A-A)

print("\n\n\n[행렬 곱셈]")
x = np.array([[1,2],[3,4]])
y = np.array([[3,4],[3,2]])
print("\n# np.dot(x,y) :\n",np.dot(x,y))

print("\n\n\n[비교연산 : array 내의 값을 빠르게 비교]")
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print("\n# a == b :\n",a==b)
print("\n# a > b :\n",a>b)

print("\n\n\n[논리 연산 : logical_and, logical_or 함수 -> array 내 element-wise 연산 수행]")
a = np.array([1,1,0,0],dtype=bool)
b = np.array([1,0,1,0],dtype=bool)
print("\n# np.logical_or(a,b) :\n",np.logical_or(a,b))
print("\n# np.logical_and(a,b) :\n",np.logical_and(a,b))

print("\n\n\n[Reductions : array를 하나의 스칼라 값으로 만들어주는 연산]")
a = np.array([1,2,3,4,5])
print("\n# np.sum(a) :\n",np.sum(a))
print("\n# a.sum() :\n",a.sum())
print("\n# a.min() :\m",a.min())
print("\n# a.max() :\n",a.max())
print("\n# a.argmin() (최소값의 인덱스 반환):\n",a.argmin())
print("\n# a.argmax() (최대값의 인덱스 반환):\n",a.argmax())

print("\n\n\n[Logical Reductions : array가 bool-type일 때 하나로 출력하는 것]")
a = np.array([1,1,1],dtype=bool)
b = np.array([1,1,0],dtype=bool)
c = np.array([0,0,0],dtype=bool)
print("\n# np.all(a/b/c) :\n",np.all(a),np.all(b),np.all(c))
print("\n# np.any(a/b/c) :\n",np.any(a),np.any(b),np.any(c))

print("\n\n\n[Statistical Recuctions]")
x = np.array([1,2,3,1])
print("\n# np.mean(x) :\n",np.mean(x))
print("\n# np.median(x) :\n",np.median(x))
print("\n# np.std(x) :\n",np.std(x))