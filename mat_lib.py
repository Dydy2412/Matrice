## Dydy2412 ##
Matrice_ = object

class Matrice():
    '''Matrice class for matrice operation'''

    def __init__(self, li : list):

        if sum([len(i) for i in li])/len(li) != len(li[0]):
            raise ValueError('This list not have the same lenth for each row.')

        self.mat = li
        self.n = len(li)
        self.p = len(li[0])

    def __str__(self):
        temp_li = [[str(j) for j in i] for i in self.mat]
        max_lenth = max([len(j) for i in temp_li for j in i])+1
        output = [['' for j in range(self.p+2)] for j in range(self.n)]

        for i in range(len(output)):
            for j in range(len(output[i])):
                if j == 0 : 
                    output[i][j] = '['
                elif j == len(output[i])-1 : 
                    output[i][j] = ' ]\n'
                else:
                    output[i][j] = ' '*(max_lenth-len(temp_li[i][j-1]))+ temp_li[i][j-1]
        str_out = [''.join(i) for i in output]

        return ''.join(str_out)

    def __call__(self):
        return self.mat

    def __neg__(self):
        return self*(-1)

    def __add__(self, smat : Matrice_) -> Matrice_:
        '''Add two matrices (same order)'''

        if not isinstance(smat, Matrice):
            raise ValueError('This method need a Matrice instance as parameter')

        if self.n == smat.n and self.p == smat.p:
            return Matrice([[self.mat[i][j]+smat()[i][j] for j in range(smat.p)] for i in range(self.n)])
        else:
            raise ValueError('This two matrices does not have the same order')

    def __sub__(self, smat : Matrice_) -> Matrice_:
        '''Substract two matrices (same order)'''

        return self + (-smat)

    def __mul__(self, val : float or Matrice_) -> Matrice_:
        '''Muliply matrices with coefficient or other matrices'''
        if isinstance(val,Matrice):
            return self.mul(val)
        elif type(val) == int:
            return self.coef(val)
        else:
            raise ValueError('Wrong Parameter')

    def __pow__(self, val):
        '''Matrices power and inverse (squared)'''
        if val == -1:
            pass
        elif val >= 0:
            
            out = Matrice([[1 if i==j else 0 for j in range(self.p)] for i in range(self.n)])
            for i in range(val):
                out *= self

            return out
        else:
            raise ValueError('Negative power > -1 not allowed')

    def coef(self, coef : int) -> Matrice_:
        '''Apply coefficient to a matrice'''

        return Matrice([[j*coef for j in i] for i in self.mat])

    def mul(self, smat : Matrice_) -> Matrice_:
        '''Muliply tow matrices (same row/column)'''

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

    def get_row(self, index : int) -> list:
        '''Return a row of the matrice'''

        return self.mat[index]

    def get_column(self, index : int) -> list:
        '''Return a column of the matrice'''

        return [i[index] for i in self.mat]

    def is_squared(self):
        return self.n == self.p
