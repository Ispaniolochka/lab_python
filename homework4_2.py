s = "У лукоморья 123 дуб зеленый 456"
print('1. Буква "я" встречается в строке:',s.count('я'))
print('2. Буква "у" встречается в строке:',s.count('у'))
if s.isalpha():
    print("В строке есть цифры.")
else:
    print('3.',s.upper())
x = len(s)
if x > 4:
    print('4.',s.lower())
          
print('5.',s.replace('У','O'))

              
