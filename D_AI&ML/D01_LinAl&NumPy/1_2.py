import numpy as np
A = np.array([[1,4,5,8],[2,1,7,3],[5,4,5,9]])
A = A/np.sum(A)

mean = np.mean(A)
median = np.median(A)
std = np.std(A)
var = np.var(A)
print(mean,median,std,var)