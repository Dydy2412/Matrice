## Dydy2412 ##
from fractions import Fraction
from math import prod

Matrice_ = object

def det(mat : Matrice_) -> int:
    '''Return the determinant of the matrice'''
    order = mat.get_width()

    if not mat.is_squared():
        raise ValueError('Matrice not squared')

    if mat.get_width() == 1:
        return mat()[0]

    elif mat.get_width() == 2:
        return mat()[0][0]*mat()[1][1] - mat()[0][1]*mat()[1][0]

    elif mat.get_width() >= 3:
        row = mat.get_row(0)
        det_coef = [-row[i] if (i+1)%2==0 else row[i] for i in range(len(row))]
        det_mat = [Matrice([[mat()[k][l] for l in range(mat.p) if l!=j] for k in range(1,mat.n)]) for j in range(mat.p)]

        return sum([det_coef[j]*det(det_mat[j]) for j in range(len(det_coef))])

class Matrice():
    '''Matrice class for matrice operation'''

    def __init__(self, li : list) -> None:

        if sum([len(i) for i in li])/len(li) != len(li[0]):
            raise ValueError('This list not have the same lenth for each row.')

        self.mat = li
        self.n = len(li)
        self.p = len(li[0])

    def __str__(self) -> str:
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

    def __call__(self) -> list:
        return self.mat

    def __neg__(self) -> Matrice_:
        return self*(-1)

    def __add__(self, smat : Matrice_) -> Matrice_:
        '''Add two matrices (same order)'''

        if not isinstance(smat, Matrice):
            raise TypeError('This method need a Matrice instance as parameter')

        if self.n == smat.n and self.p == smat.p:
            return Matrice([[Fraction(self.mat[i][j]+smat()[i][j]).limit_denominator() for j in range(smat.p)] for i in range(self.n)])
        else:
            raise ValueError('This two matrices does not have the same order')

    def __sub__(self, smat : Matrice_) -> Matrice_:
        '''Substract two matrices (same order)'''

        return self + (-smat)

    def __mul__(self, val : float or Matrice_) -> Matrice_:
        '''Muliply matrices with coefficient or other matrices'''
        if isinstance(val,Matrice):
            return self.__mul(val)
        elif type(val) == float or int:
            return self.__coef(val)
        else:
            raise TypeError('Wrong Parameter')

    def __pow__(self, val : int) -> Matrice_:
        '''Matrices power and inverse (squared)'''
        if val == -1:
            d = det(self)
            if d != 0 and self.is_squared():
                if self.n == 1: #1x1
                    return Matrice([1/self()[0]])

                elif self.n == 2: #2x2 
                    return Matrice([[self()[1-i][1-j] if i==j else -self()[i][j] for j in range(2)] for i in range(2)])*(1/d)

                elif self.n == 3: #3x3
                    output = Matrice([[0 for j in range(3)] for i in range(3)])
                    
                    for i in range(3):
                        for j in range(3):
                            temp = [[self()[k][l] for l in range(3) if k!=i and l!=j] for k in range(3)]
                            temp.remove([])
                            mat_det = det(Matrice(temp))
                            if (i+j+2)%2 == 0:                               
                                if i==j: 
                                    output()[i][j] = mat_det
                                else: 
                                    output()[j][i] = mat_det
                            else:
                                output()[j][i] = -mat_det
                    
                    return output*(1/d)

                else:
                    raise ValueError('Matrice too big')
            else:
                raise ValueError('Matrice non-inversible')
        elif val >= 0:
            
            out = Matrice([[1 if i==j else 0 for j in range(self.p)] for i in range(self.n)])
            for i in range(val):
                out *= self

            return out
        else:
            raise ValueError('Negative power > -1 not allowed')

    def __truediv__(self, val : int or Matrice_) -> Matrice_:
        if isinstance(val, Matrice):
            return self*val**(-1)
        elif type(val) == int or float:
            return self*(1/val)
        else:
            raise TypeError('Wrong Parameter')

    def __coef(self, coef : int) -> Matrice_:
        '''Apply coefficient to a matrice'''

        return Matrice([[Fraction(j*coef).limit_denominator() for j in i] for i in self.mat])

    def __mul(self, smat : Matrice_) -> Matrice_:
        '''Muliply tow matrices (same row/column)'''

        if self.p == smat.n:
            return Matrice([[self.__single_mul(self.get_row(i), smat.get_column(j)) for j in range(smat.p)] for i in range(self.n)])
        else:
            raise ValueError("This Matrices can't be multiplied")

    def __single_mul(self, mata : list, matb : list) -> list:
        '''Add product of each index of the two list'''

        return sum([Fraction(mata[i]*matb[i]).limit_denominator() for i in range(len(mata))])

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

    def is_squared(self) -> bool:
        return self.n == self.p
