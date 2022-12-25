# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num_list = []
summ = 0
n = int(input('Введите число N '))
for k in range(1, n + 1):
    num_list.append(round(((1 + 1/k) ** k), 3))
    summ = summ + num_list[k - 1]
print(num_list)
print(summ)