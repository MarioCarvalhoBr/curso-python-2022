import numpy as np
a = np.array([[5, 1, 3],
              [1, 1, 1],
              [1, 2, 1]])

b = np.array([1, 2, 3])

z = np.dot(a, b)
newarr = z.reshape(1, 3)

print(newarr)
print(newarr.shape)