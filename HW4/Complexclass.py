import numpy as np
class Complex():
    def __init__(self,a=0,b=0):
            self._a=a
            self._b=b
            if np.sqrt(self._a**2+self._b**2)!=0:
             self._r=np.sqrt(a**2+b**2)
             self._phi=np.arccos(self._a/self._r)
            else:
                self._r='Нельзя однозначно задать'
                self._phi='Нельзя однозначно задать'
    def __getattr__(self, item):
        if item=='a':
              return self._a
        if item=='b':
            return self._b

    def __add__(self, other):#Сложение слева
        if type(other)==int or type(other)==float:
            return Complex(self._a+other,self._b)
        if type(other)==Complex:
            return Complex(self._a+other._a,self._b+other._b)
    def __radd__(self, other):#Сложение справ
        if type(other)==int or type(other)==float:
            return Complex(self._a+other,self._b)
        if type(other)==Complex:
            return Complex(self._a+other._a,self._b+other._b)
    def __sub__(self, other):#Вычитание слева
        if type(other)==int or type(other)==float:
            return Complex(self._a-other,self._b)
        if type(other)==Complex:
            return Complex(self._a-other.a,self._b-other._b)
    def __rsub__(self, other):#вычитание справа
        if type(other)==int or type(other)==float:
            return Complex(self._a-other,self._b)
        if type(other)==Complex:
            return Complex(self._a-other._a,self._b-other._b)
    def __str__(self):#Перевод в строку
            return f'({self._a},{self._b})'
    def __mul__(self, other):#умножение слева
        if type(other)==int or type(other)==float:
            return Complex(self._a*other,self._b*other)
        if type(other)==Complex: #умножение справа
            return Complex(self._a*other._a-self._b*other._b,self._a*other._b+self._b*other._a)
    def __rmul__(self, other):
        if type(other)==int or type(other)==float:
            return Complex(self._a*other,self._b*other)
        if type(other)==Complex:
            return Complex(self._a*other._a-self._b*other._b,self._a*other._b+self._b*other._a)
    def __truediv__(self, other):
        if type(other)==int or type(other)==float:
            return Complex(self._a/other,self._b/other)
        if type(other)==Complex:
            return Complex((self._a*other._a+self._b*other._b)/(other._a**2+other._b**2)**(1/2),(-self._a*other._b-self._b*other._a)/(other._a**2+other._b**2)**(1/2))
    def __rtruediv__(self, other):
        if type(other)==int or type(other)==float:
            return Complex(self._a/other,self._b/other)
        if type(other)==Complex:
            return Complex((self._a*other._a+self._b*other._b)/(other._a**2+other._b**2)**(1/2),(-self._a*other._b-self._b*other._a)/(other._a**2+other._b**2)**(1/2))
    def to_exp(self):
        return self._r,self._phi
A=Complex(3,4)
B=Complex(5,6)
C=Complex(4,0)
D=Complex()
print(C.a)
print(C,A,D, D.to_exp())
