'''Напишите программный код, который будет
создавать новый список, содержащий в
качестве элементов квадратные корни всех
чисел из списка
[2, 4, 9, 16, 25]:
1) на основе цикла for
2) на основе функции map
3) в виде генератора списка'''

from math import sqrt
def fun_1(L):
    S = []
    for x in L:
        S.append(sqrt(x))
    return S

def fun_2(L):
    return list(map(sqrt,L))

def fun_3(L):
    return [sqrt(x) for x in L]

L = [2,4,9,16,25]
print(fun_1(L))
print(fun_2(L))
print(fun_3(L))








    
