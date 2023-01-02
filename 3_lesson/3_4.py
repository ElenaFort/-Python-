# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random


def num_find(len_list):
    num_list = [round(random.uniform(0, 10), 2)
                for num_list in range(len_list)]
    return num_list


def difference(num_list):
    max_num = num_list[0] % 1
    min_num = num_list[0] % 1
    for i in num_list:
        temp = i % 1
        if temp > max_num:
            max_num = temp
        elif temp < min_num:
            min_num = temp
    return round((max_num - min_num), 2)


num_list = num_find(int(input('Введите количество элементов в списке: ')))
result = difference(num_list)
print(num_list)
print('Difference: ', + result)
