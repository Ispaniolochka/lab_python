'''Найдите сумму всех значений функции
         y(x)=x**2 +3
на интервале от 10 до 30 с шагом 2'''

def y(x):
    return x*x + 3
total = 0
for i in range(10,31,2):
    total = total + y(i)
    print(total)
    
