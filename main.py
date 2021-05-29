from mat_lib import Matrice, det

MatA = Matrice([
    [1/3, 0], 
    [1, 20]
])

MatB = Matrice([
    [ 1, 2],
    [ 1, 0]
])

MatC = Matrice([
    [ 3, 8,-1],
    [ 5, 1, 4],
    [ 2, 3,-3]
])

MatD = MatC**(-1)
print(MatD)