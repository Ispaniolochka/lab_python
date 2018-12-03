'''Дан список из 20 элементов. Найти пять
соседних элементов, сумма значений которых
максимальна.'''

L =[2,3,9,50,47,38,97,45,21,8,17,92,36,52,84,27,33,74,13,23]


def fun(L):
    max_sum = 0 #максимальная сумма 5-ки
    index_start = 0 #индекс первого числа в 5-ке(из max_sum)
    
    for i in range(len(L)-5):
        sum_now = L[i]+L[i+1]+L[i+2]+L[i+3]+L[i+4] #сумма текущей 5-ки
        if sum_now > max_sum:
            max_sum = sum_now
            index_start = i
    return index_start

index_start = fun(L)
print(L[index_start])
print(L[index_start+1])
print(L[index_start+2])
print(L[index_start+3])
print(L[index_start+4])
             
            
    





    
