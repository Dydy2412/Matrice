## Dydy2412 ##

class Matrice():

    def __init__(self, li : list):

        if sum([len(i) for i in li])/len(li) != len(li[0]):
            raise ValueError('This list not have the same lenth for each row.')

        self.mat = li
        self.n = len(li)
        self.p = len(li[0])

    def coef(self, coef : int):
        self.mat = [[j*coef for j in i] for i in self.mat]

    def add(self, smat):
        if not isinstance(smat, Matrice):
            raise ValueError('This method need a Matrice instance as parameter')

        if self.n == smat.n and self.p == smat.p:
            self.mat = [[self.mat[i][j]+smat.get_list()[i][j] for j in range(self.p)] for i in range(self.n)]
        else:
            raise ValueError('This two matrices does not have the same order')

    def sub(self, smat):
        smat.coef(-1)
        self.add(smat)

    def mul(self, smat):
        if not isinstance(smat, Matrice):
            raise ValueError('This method need a Matrice instance as parameter')

        if self.p == smat.n:
          for i in range(self.n):
            for j in range(smat.p):
              

    def get_width(self):
        return self.n

    def get_lenth(self):
        return self.p

    def get_order(self):
        return (self.n, self.p)

    def get_list(self):
        return self.mat

    def print_mat(self):
        for i in self.mat:
            print(i)

MatA = Matrice([
    [2,2,1], 
    [3,1,0]
])

MatB = Matrice([
    [1,1,2], 
    [0,2,3]
])

MatA.sub(MatB)
MatA.print_mat()