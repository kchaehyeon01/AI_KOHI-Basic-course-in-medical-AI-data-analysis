import numpy as np

def get_matrix():
	[n, m] = [int(x) for x in input().strip().split(" ")]
	matrix = []
	for i in range(n):
		row = [int(x) for x in input().strip().split(" ")]
		matrix.append(row)
	return np.array(matrix)

def matrix_tutorial(A):
	B = A.T
	try:
		C = np.linalg.inv(B)
		return np.sum(C>0)
	except:
		return "not invertible"

A = get_matrix()
print(matrix_tutorial(A))