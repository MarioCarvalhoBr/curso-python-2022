from audioop import lin2adpcm
import numpy as np
"""
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if l == c:
            print(f"posicao: ({l}, {c}) == {matriz[l][c]}")

"""
# str, float, int
# Criação matrix = [[x,y,z], [a,b,c], ...]
matriz = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [12,14,15,16]])

for linha in matriz:
    for dado in linha:
        #print(dado)
        pass

linhas, colunas = matriz.shape
for l in range(linhas):
    for c in range(colunas):
        #print(matriz[l][c])
        pass

#print("linhas: ", linhas)
##print("colunas: ", colunas)
#print("matriz: \n", matriz)
#print("matriz: \n", matriz[0][2])


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)

for dim in d:
    for linha in dim:
        for dado in linha:
            #print(dado)
            pass

x = np.array([[10, 9], [8, 10]])
y = np.array([1,2])

result = np.dot(x, y) 
z = x*y

print(result, "\n") 
print(z) 

m = np.asmatrix(x)

m[0,1] = 100

print(m[0,1])