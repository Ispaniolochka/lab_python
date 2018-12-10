from pprint import pprint
import course_reader
import course_writer
'''Пробую открыть фвйл. Если не получается, записываю в него пустой список'''
def CheckForFile(filename):
    try:
        open(filename,'r')
    except Exception:
        course_writer.writer(filename,[])
'''вызываю функцию, проверяющую файл'''        
CheckForFile('task_list.json')
'''читаю файл и передаю содержимое в переменную task_list'''
task_list = course_reader.reader('task_list.json')

while True:
    print('Простой todo: \n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход')
    command = int(input('Укажите число:'))
    
    if command == 1:
        task = {'name': '','category': '','time': ''}
        task['name'] = input('Сформулируйте задачу:')
        task['category'] = input('Добавьте категорию к задаче:')
        task['time'] = input('Добавьте время к задаче:')
        task_list.append(task)
        
    elif command == 2:
        pprint(task_list)
        
    elif command == 3:
        '''в файл task_list.json записываем список словарей task_list'''
        course_writer.writer('task_list.json',task_list)
        '''сохранить словарь в файл'''
        print('Задачи сохранены в файл!')
        break
