# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
num_list = []
n = int(input('Введите число N '))
for i in range(n):
    num_list.append(i)
print("Исходный список:")
print(num_list)
num_list_new = num_list[:]
for k in range(len(num_list_new)):
    j = random.randint(0, len(num_list_new) - 1)
    temp = num_list_new[k]
    num_list_new[k] = num_list_new[j]
    num_list_new[j] = temp
print("Перемешанный список:", end="\n" + str(num_list_new))
