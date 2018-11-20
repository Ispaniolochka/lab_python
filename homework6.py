'''Функция для расчета скидки'''
def getdiscount(day,tickets):
    if day == 'завтра':
        return 5
    elif tickets >= 20:
        return 20
    else:
        return 0
    
'''Функция для расчета стоимости от времени сеанса'''    
def get_full_cost(hour):
        if hour == 10:
            return 250
        elif hour == 12:
            return 250
        elif hour == 13:
            return 350
        elif hour == 14:
            return 450
        elif hour == 16:
            return 350
        elif hour == 18:
            return 450
        elif hour == 20:
            return 450
        
'''Функция для расчета стоимости билета с учетом скидки'''
def getcost(full_cost,discount):
    return (full_cost * (100 - discount)) / 100

film = input('Выбрать фильм:')
if len(film)>0:
    day = input('Выбрать день (сегодня, завтра):')
    hour = int(input('Выбрать время:'))
    tickets = input('Выбрать количество билетов:')
    
    
    '''Завела переменную и посчитала ее с помощью вызова функции'''
    discount = getdiscount(day,int(tickets))   
    full_cost = get_full_cost(hour) * int(tickets)
    cost = getcost(full_cost,discount)
    
    print('Выбрали фильм:',film,'День:',day,'Время:',hour,'Количество билетов:',tickets)
    print('Результат:',cost,'рублей.')
else:
    print('Вы не ввели название фильма!')
