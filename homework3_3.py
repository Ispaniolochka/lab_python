import math
def value(x): 
    if 0.2<= x <= 0.9:
        return math.sin(x)
    else:
        1
element=input('Введите число:')
result=value(float(element))
print('результат:',result)

