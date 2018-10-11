# 1.
import numpy as np


a = np.array([1, 2, 3])
Randam_a = np.random.randint(0,9, (2,10))
print(Randam_a)

# # 2.
b = np.array([[1, 2, 4],
            [4, 2, 1]])
a = b[1,1]
print(a)
# Aver_a = b.mean()
# print(Aver_a)
#
# # 3.
import math

for i in range(len(b)):
    sigma = math.sqrt((np.sum((b[i] - Aver_a)**2))/len(b))

print(sigma)
sigma1 = np.std(b)
print(sigma1)


# 4.
3 * x0 + x1 = 9
x0 + 2 * x1 = 8

M1 = np.array([[3, 1], [1, 2]])
V1 = np.array([9, 8])

sistema = np.linalg.solve(M1, V1)
print(sistema)
