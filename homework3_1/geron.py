# geron.py
import math

def geron(a, b, c): 
    ''' Вычисляет площадь треугольника по формуле Герона:
    >>> geron(3, 4, 5)
    6.0
    
    >>> geron(7, 8, 9)
    26.83
    '''
    # здесь нужно написать собственный код
    p = (a+b+c)/2
    return math.sqrt(p * (p-a)*(p-b)*(p-c))
      
if __name__ == "__main__":
    import doctest
    doctest.testmod()
