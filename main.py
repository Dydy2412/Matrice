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
    [ 1, 2, 3, 4, 5],
    [ 6, 7, 8, 9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])

MatD = det(MatC)
print(MatD)