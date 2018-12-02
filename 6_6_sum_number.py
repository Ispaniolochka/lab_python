'''Дано число, введенное с клавиатуры.
Определить сумму квадратов нечетных
цифр в числе.'''

s = input('Введите число:')
total = 0
for i in s:
    num = int(i)
    if num % 2 == 0:
        continue
    total = total + num**2
print(total)




