'''Напишите программу,которая по коду города и длительности разговоров вычисляет
их стоимость и выводит результат на экран:
Екатеринбург - код 343, 15 руб/мин
Омск - код 381, 18 руб/мин
Воронеж - код 473, 13 руб/мин
Ярославль - код 485, 11 руб/мин'''

def getcost(code,time):
    if code == 343:
        return 15 * time
    elif code == 381:
        return 18 * time
    elif code == 473:
        return 13 * time
    elif code == 485:
        return 11 * time
    
def getcity(code):
    if code == 343:
        return 'Екатеринбург'
    elif code == 381:
        return 'Омск'
    elif code == 473:
        return 'Воронеж'
    elif code == 485:
        return 'Ярославль'
    
citycode = input('Введите код города:')   '''Переводим строку в число'''
if len(citycode)>0:
    duration = input('Введите количество минут разговора:')
    city = getcity(int(citycode))
    result = getcost(int(citycode),int(duration)) '''int - переводим в целое число'''
    print('Город ',city,'.Стоимость разговора:',result,'рублей')
else:
    print('Вы не ввели код!')
   

