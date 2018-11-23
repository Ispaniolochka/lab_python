s = "У лукоморья 123 дуб зеленый 456"
if s.find('я'):
    print('1. Буква "я" встречается в строке:',s.count('я'))
print('2. Буква "у" встречается в строке:',s.count('у'))
if s.isalpha():
    print(s.upper())
else:
    print('3.',s.upper())
x = len(s)
if x > 4:
    print('4.',s.lower())
s.replace(str(0),'O')       
print('5.',s.replace(str(0),'O'))

              
