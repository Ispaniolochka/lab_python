element=input("Введите номер элемента:")
if len(element)>0:
    number=int(element)
    if number==3:
        print(number,'Li')
    elif number==17:
        print(number,'Cl')
    elif number==25:
        print(number,'Mn')
    elif number==80:
        print(number,'Hg')
else:
    print('Вы не ввели число!')
