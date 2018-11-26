import random
words = ['самовар','весна','лето']
word = random.choice(words)
letter_number = random.randint(0,len(word)-1)
lst = list(word)
lst[letter_number] = '?'
lst = ''.join(lst)
print(lst)
user_words = input('Введите букву:')
if user_words == word[letter_number]:
    print('Победа!')
    print('Слово:',word)
else:
    print('Увы! Попробуйте в другой раз.')
    
