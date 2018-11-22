import random
num = random.randint(1,4)
user_num = int(input('Введите число от 1 до 4:'))
if user_num == num:
    print('Победа')
elif user_num > num:
    print('Не угадали. Ваше число больше!')
elif user_num < num:
    print('Не угадали. Ваше число меньше!')
else:
    print('Повторите еще раз!')
