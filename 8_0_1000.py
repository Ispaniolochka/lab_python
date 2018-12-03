'''Напишите функцию, которая для целочисленного
списка из 1000 случайных элементов
определяет, сколько отрицательных элементов
располагается между его максимальным и
минимальным элементами включительно.'''

import random

nums = [random.randint(-1000,1000) for _ in range(1000)]
min_num = min(nums)
max_num = max(nums)

min_i = nums.index(min_num)
max_i = nums.index(max_num)

n = 0
if min_i > max_i:
    min_i, max_i = max_i,min_i
    
for i in range(min_i,max_i + 1):
    if nums[i] < 0:
        n +=1

print(n)



