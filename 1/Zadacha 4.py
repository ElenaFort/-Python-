# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти
# (x и y).

# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

quarterNumber = int(input('Введите номер четверти: '))
if quarterNumber == 1:
    print('x > 0, y > 0')
elif quarterNumber == 2:
    print('x < 0, y > 0')
elif quarterNumber == 3:
    print('x < 0, y < 0')
elif quarterNumber == 4:
    print('x > 0, y < 0')
else:
    print('Нет такой четверти')
