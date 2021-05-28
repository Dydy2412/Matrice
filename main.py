from mat_lib import Matrice, det

MatA = Matrice([
    [-133, 2], 
    [   3, 2]
])

MatB = Matrice([
    [ 1, 2, 3],
    [ 2,-1, 0],
    [ 6, 1, 0]
])

MatC = Matrice([
    [ 3,-2,-1],
    [-5, 1, 2],
    [ 2, 0,-3]
])

MatD = det(MatB)
print(MatD)