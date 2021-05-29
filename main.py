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
    [ 3,-2,-1],
    [-5, 1, 2],
    [ 2, 0,-3]
])

MatD = MatA/3
print(MatD)