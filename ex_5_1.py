import random
words = ['самовар','весна','лето']
word = random.choice(words)
print(word)
random.choice(word)
lst = list(word)
lst[2] = '?'
lst = ''.join(lst)
print(lst)
user_words = input('Введите букву:')
if user_words == word[2]:
    input('Победа!')
else:
    input('Увы! Попробуйте в другой раз.')
    
