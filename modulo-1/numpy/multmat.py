import numpy as np
a = np.array([[5, 1, 3],
              [1, 1, 1],
              [1, 2, 1]])

b = np.array([1, 2, 3])
x = 6
# Mult de matrizes é com arroba @ ou com dot
print(a @ b)
print("Soma: ", a + b)
print("Sub: ", a - b)
matrix = np.array([a.dot(b)])

print (matrix)
print (matrix.T)

# Mult de matrizes  por um escalar: * ou multiply
print(x * a)
print(np.multiply(x, a))



matrix = matrix.T

print(matrix[0][0])
print(matrix[1][0])
print(matrix[2][0])


print (matrix)
print (matrix.T)

newarr = matrix.reshape(4, 3)
