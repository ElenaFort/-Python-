# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

num_list = []
n = int(input('Введите число N: '))
poz_one = int(input('Введите номер первой позиции: '))
poz_two = int(input('Введите номер второй позиции: '))
for k in range(- n, n + 1):
    num_list.append(k)
print(num_list)
if poz_one <= len(num_list) >= poz_two:
    composition = num_list[poz_one - 1] * num_list[poz_two - 1]
    print(composition)
else:
    print('There are no values for these indexes!')
