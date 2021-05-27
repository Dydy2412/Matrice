## Dydy2412 ##
Matrice_inst = object

class Matrice():
    '''Matrice class for matrice operation'''

    def __init__(self, li : list):

        if sum([len(i) for i in li])/len(li) != len(li[0]):
            raise ValueError('This list not have the same lenth for each row.')

        self.mat = li
        self.n = len(li)
        self.p = len(li[0])

    def coef(self, coef : int) -> Matrice_inst:
        '''Apply coefficient to a matrice'''

        return Matrice([[j*coef for j in i] for i in self.mat])

    def add(self, smat : Matrice_inst) -> Matrice_inst:
        '''Add two matrices (same order)'''

        if not isinstance(smat, Matrice):
            raise ValueError('This method need a Matrice instance as parameter')

        if self.n == smat.n and self.p == smat.p:
            return Matrice([[self.mat[i][j]+smat.get_list()[i][j] for j in range(smat.p)] for i in range(self.n)])
        else:
            raise ValueError('This two matrices does not have the same order')

    def sub(self, smat : Matrice_inst) -> Matrice_inst:
        '''Substract two matrices (same order)'''

        smat.coef(-1)
        self.add(smat)

    def mul(self, smat : Matrice_inst) -> Matrice_inst:
        '''Muliply tow matrices (same row/column)'''

        if not isinstance(smat, Matrice):
            raise ValueError('This method need a Matrice instance as parameter')

        if self.p == smat.n:
            return Matrice([[self.single_mul(self.get_row(i), smat.get_column(j)) for j in range(smat.p)] for i in range(self.n)])
        else:
            raise ValueError("This Matrices can't be multiplied")

    def single_mul(self, mata : list, matb : list) -> list:
        '''Add product of each index of the two list'''

        return sum([mata[i]*matb[i] for i in range(len(mata))])

    def get_width(self) -> int:
        '''Return the width of the matrice'''
        return self.n

    def get_lenth(self) -> int:
        '''Return the lenght of the matrice'''
        return self.p

    def get_order(self) -> tuple:
        '''Return the order of the matrice'''
        return (self.n, self.p)

    def get_list(self) -> list:
        '''Return the list format of the matrice'''
        return self.mat

    def get_row(self, index : int) -> list:
        '''Return a row of the matrice'''
        return self.mat[index]

    def get_column(self, index : int) -> list:
        '''Return a column of the matrice'''
        return [i[index] for i in self.mat]

    def print_mat(self) -> None:
        '''Diplay the Matrice'''
        for i in self.mat:
            print(i)

MatA = Matrice([
    [-1, 2, 1], 
    [ 3, 0, 2]
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

MatD = MatA.mul(MatB)
MatD.print_mat()