'''Напишите программу-игру.
Компьютер загадывает случайное число, пользователь
пытается его угадать.
Пользователь вводит число до тех пор, пока не угадает
или не введёт слово “Выход”.
Компьютер сравнивает число с введенным и сообщает
пользователю больше оно или меньше загаданного.
Количество попыток ограничено и указывается в
программе.'''

import random
num = random.randint(0,50)
'''функция приглашает пользователя ввести число и проверяет, чтобы это было число или выход'''
def get_user_num(input_str):
    result = input(input_str)
    while True:
        if not result.isdigit() and result != 'Выход':
            result = input('Введите число или слово Выход:')
        else:
            break
    return result

user_num = get_user_num("Компьютер загадал число от 0 до 50. \nУ вас есть 3 попытки или напишите Выход:")
for i in range(0,2):
    if user_num == 'Выход':
        break
    elif int(user_num) > num:
        user_num = get_user_num('Введите число меньше:')
    elif int(user_num) < num:
        user_num = get_user_num('Введите число больше:')
    else:
        break
    
if user_num == 'Выход':
    print('Вы вышли из игры!')
elif int(user_num) != num:
    print('Game over')
    print('Число:', num)
else:
    print('Вы угадали! Поздравляю!')
    

            



    

