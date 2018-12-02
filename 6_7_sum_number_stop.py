'''Найти сумму чисел, вводимых с клавиатуры.
Количество вводимых чисел заранее
неизвестно.
Окончание ввода - слово “Стоп”
При ошибке ввода попросить повторить ввод
числа.'''

def get_user_num(input_str):
    result = input(input_str)
    while True:
        if not result.isdigit() and result != 'Стоп':
            result = input('Ошибка. Введите число:')
        else:
            break
    return result

total = 0
while True:
    s = get_user_num("Введите число или Стоп для выхода:")
    if s == 'Стоп':
        break
    total = total + int(s)
print(total)
