import tkinter
from tkinter import *
from pprint import pprint
import course_reader
import course_writer

def CheckForFile(filename):
    try:
        open(filename,'r')
    except Exception:
        course_writer.writer(filename,[])
       
CheckForFile('task_list.json')

task_list = course_reader.reader('task_list.json')
window = tkinter.Tk()
canvas = Canvas(window, width=500,height=250)
canvas.pack()

def click_1():
    task = {'задача': '','категория': '','время': ''}
    task['задача'] = entry_1.get()
    task['категория'] = entry_2.get()
    task['время'] = entry_3.get()
    task_list.append(task)
    course_writer.writer('task_list.json',task_list)
    print('Задачи сохранены в файл!')
        
def click_2():
    pprint(task_list)

    
def click_3():
    course_writer.writer('task_list.json',task_list)
    print('Задачи сохранены в файл!')
    
var = tkinter.StringVar()

label_1 = tkinter.Label(window, text='Задача')
label_1.place(x=100,y=20)

label_2 = tkinter.Label(window, text='Категория')
label_2.place(x=100,y=50)

label_3 = tkinter.Label(window, text='Время')
label_3.place(x=100,y=80)

entry_1 = tkinter.Entry(window)
entry_1.place(x=180,y=20)

entry_2 = tkinter.Entry(window)
entry_2.place(x=180,y=50)

entry_3 = tkinter.Entry(window)
entry_3.place(x=180,y=80)

button_1 = tkinter.Button(window, text='Добавить задачу',command=click_1) 
button_1.place(x=180,y=120)

button_2 = tkinter.Button(window, text='Вывести список задач',command=click_2) 
button_2.place(x=180,y=150)

button_3 = tkinter.Button(window, text='Выход',command=window.destroy) 
button_3.place(x=180,y=180)



window.mainloop()
