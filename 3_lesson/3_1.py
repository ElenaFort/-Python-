# 1. Задайте список, состоящий из произвольных чисел, количество
# задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8
from random import sample


def num_find(len_list):
    num_list = sample(range(1, len_list * 3), k=len_list)
    return num_list


def honesty_position(num_list):
    summ = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            summ = summ + num_list[i]
    print(summ)


num_list = num_find(int(input('Введите количество элементов в списке: ')))
print(num_list)
honesty_position(num_list)
