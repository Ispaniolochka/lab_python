'''Программа отображает случайное слово на английском
языке (из заранее созданного словаря). Пользователь
пытается угадать слово на русском языке.'''

import tkinter
import random

window = tkinter.Tk()

dictionary = {'Coffe':'Кофе','Tea':'Чай','Wine':'Вино','Whisky':'Виски','Coctail':'Коктейль','Juice':'Сок','Water':'Вода'}
random_key_list = random.sample(dictionary.keys(),1)

def click():
    user_word = entry.get()
    translation = dictionary[random_key_list[0]]
    if user_word == translation:
        label_result.config(text='Угадали!')
    else:
        label_result.config(text='Не угадали!')

label = tkinter.Label(window, text = "Случайное слово:")
label.pack()

label_word = tkinter.Label(window, text= random_key_list[0])
label_word.pack()

label_trs = tkinter.Label(window, text = "Укажите перевод слова")
label_trs.pack()

frame = tkinter.Frame(window)
frame.pack()

entry = tkinter.Entry(frame)
entry.pack()

label_result = tkinter.Label(frame)
label_result.pack()

button_1 = tkinter.Button(frame, text='Готово!',command=click) 
button_1.pack()

button_2 = tkinter.Button(frame, text='Выход', command=window.destroy) 
button_2.pack()


window.mainloop()
