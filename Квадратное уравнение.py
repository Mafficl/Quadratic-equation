from math import *
print ('Квадратное уравнение')
a = float (input('Коэффициэнт а = '))
b = float (input('Коэффициэнт b = '))
c = float (input('Коэффициэнт c = '))
D = b**2-4*a*c
if D>0:
    x1 = (-b+sqrt(D))/(2*a)
    x2 = (-b-sqrt(D))/(2*a)
    print('x1 = ', x1, "x2= ", x2)
elif D==0:
    x1 = -b/(2*a)
    print('x =', x1)
else:
    print("Корней нет")