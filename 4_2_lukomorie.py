'''s = "У лукоморья 123 дуб зеленый 456"
1. Определить, встречается ли в строке буква 'я'. Вывести на экран ее
позицию (индекс) в строке.
2. Определить, сколько раз в строке встречается буква 'у'.
3. Определить, состоит ли строка из букв, ЕСЛИ нет, ТО вывести строку в
верхнем регистре.
4. Определить длину строки. ЕСЛИ длина строки превышает 4 символа, ТО
вывести строку в нижнем регистре.
5. Заменить в строке первый символ на 'О'. Результат вывести на экран'''


s = "У лукоморья 123 дуб зеленый 456"
if s.find('я'):
    print('1. Буква "я" встречается в строке:',s.count('я'))
print('2. Буква "у" встречается в строке:',s.count('у'))
if not s.isalpha():
    print('3.',s.upper())
x = len(s)
if x > 4:
    print('4.',s.lower())
print('5.','O' + s[1:])             
