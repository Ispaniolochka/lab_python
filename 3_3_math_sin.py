'''Написать программу, вычисляющую значение
функции (на вход подается вещественное число):'''

import math
def value(x): 
    if 0.2<= x <= 0.9:
        print('результат:', math.sin(x))
    else:
        print('результат:',1)
element=input('Введите число:')
result=value(float(element))


