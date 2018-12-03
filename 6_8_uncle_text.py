'''Удалить из стихотворения все слова,
начинающиеся на букву м.
Результат вывести на экран в виде строки.
Строковый метод startswith()'''

s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
words = s.lower().split()
new_words = [word for word in words if not word.startswith('м')]
print(' '.join(new_words))
        





