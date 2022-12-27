# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample


def num_find(len_list):
    num_list = sample(range(1, len_list * 3), k=len_list)
    return num_list


def result_function(num_list):
    result = []
    new_list_len = len(num_list)//2
    if len(num_list) % 2 != 0:
        new_list_len = new_list_len + 1
    for i in range(new_list_len):
        result.append(num_list[i] * num_list[len(num_list) - i - 1])
    if len(num_list) % 2 != 0:
        result[new_list_len - 1] = num_list[new_list_len - 1]
    return result


num_list = num_find(int(input('Введите количество элементов в списке: ')))
result_list = result_function(num_list)
print(num_list)
print(result_list)
