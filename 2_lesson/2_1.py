# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

x = input('Введите число: ')
summ = 0
power = len(x) - 2
x = float(x)
x = x * int(10 ** power)
while x:
    summ = summ + int(x) % 10
    x = x // 10

print(int(summ))