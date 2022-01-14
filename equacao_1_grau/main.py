# Ax + B = 0
# x = -B/A
def entrada():
    A = float(input("A: \n"))
    B = float(input("B: \n"))
    return A, B, [1,24,25,265], "Mario"

def calc(A, B):
    x = -B/A
    print("X: ", x)
    return x

A, B, _, _ = entrada()
calc(A, B)
