# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной
# последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random


def num_find(len_list):
    if len_list <= 0:
        print("Введено неверное значение!")
        return []
    num_list = [random.randint(0, 10) for num_list in range(len_list)]
    print(num_list)
    return num_list


def get_unique_numbers(numbers):
    unique = []
    for i in numbers:
        if numbers.count(i) == 1:
            unique.append(i)
    return unique


numbers = num_find(
    int(input("Введите количество элементов начального списка: ")))
print(get_unique_numbers(numbers))
