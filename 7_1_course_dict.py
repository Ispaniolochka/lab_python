from pprint import pprint
task_list = []

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
        break


'''from pprint import pprint
tasks = [{'name':'поздравить друга с днем рождения', 'category':'ДР', 'time':'12.12.2019'},
         {'name':'купить масло', 'category':'покупки', 'time':'сегодня'}]

pprint(tasks)'''
