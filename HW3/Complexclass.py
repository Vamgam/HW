import numpy as np
class Complex():
    def __init__(self,a=0,b=0):
        self._a=a
        self._b=b
    def get_a(self):
        return self._a
    def get_b(self):
        return self._b
    def a(self,value):
        self._a=value
    def b(self,value):
        self._b=value
    def add(self,B):
        if type(B)==int:
            return Complex(self._a+B,self._b)
        if type(B)==Complex:
            return Complex(self._a+B._a,self._b+B._b)
    def sub(self,B):
        if type(B)==int:
            return Complex(self._a-B,self._b)
        if type(B)==Complex:
            return Complex(self._a-B._a,self._b-B._b)
    def mult(self,B):
        if type(B)==int:
            return Complex(self._a*B,self._b*B)
        if type(B)==Complex:
            return Complex(self._a*B._a-self._b*B._b,self._b*B._a+B._b*self._a)
    def div(self,B):
        if type(B) == int and B!=0:
            return Complex(self._a / B, self._b / B)
        if type(B) == Complex and (B._a**2+B._b**2)!=0:
            return Complex((self._a * B._a + self._b * B._b)/(B._a**2+B._b**2), (self._b * B._a - B._b * self._a)/(B._a**2+B._b**2))
    def __str__(self):#Перевод в строку
            return f'({self._a},{self._b})'
    def transform(self,a,b,key):
     if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
        if key=='exp':
            if (a**2+b**2)!=0:
               print('r=',np.sqrt(abs((a**2+b**2))),' phi=',np.arccos(a/((a**2+b**2))))
            else:
                print('Нельзя перевести в экспоненциальную форму')
        elif key=='norm':
            print('a=',a*np.cos(b),' b=',a*np.sin(b))
            print(a,np.cos(b))
     else:
         print('Неправильный формат данных')

A=Complex(5,4)
B=Complex(3,4)
print(A.add(B),A.sub(B),A.mult(B),A.div(B))
A.transform(a=3,b=4,key='exp')
A.transform(a=5,b=np.pi,key='norm')
A.b(5)
print(A.get_b())