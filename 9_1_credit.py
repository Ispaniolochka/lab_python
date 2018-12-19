'''Определите регион с максимальным
количеством заявок на потребительские
кредиты в 2017 году.'''

import csv
from pprint import pprint

def dict_credit_region(what, when):
    credit_region = {}
    try:
        with open('opendata.csv', encoding='cp1251') as csvfile:
            credit_reader = csv.reader(csvfile, delimiter=',') # delimiter по умолчанию ','
            row_number = 0
            for row in credit_reader:
                if row[0] == what:
                    where = row[1]
                    if where == 'Россия':
                        continue
                    lst = row[2].split('-')                    
                    if lst[0] == when:
                        new_credit_count = int(row[3])
                        if where in credit_region.keys():
                            current_credit_count = int(credit_region[where])
                            credit_region[where] = current_credit_count + new_credit_count
                        else:
                            credit_region[where] = new_credit_count
        return credit_region     
    except Exception as e:
        return e

def search_credit_region(what, when):
    credit_region = dict_credit_region(what, when)
    key_max = max(credit_region, key=credit_region.get)
    return key_max

if __name__ == '__main__':
    print('Регион с максимальным количеством заявок на потребительские кредиты в 2017 году:', search_credit_region('Количество заявок на потребительские кредиты', '2017'))
   
