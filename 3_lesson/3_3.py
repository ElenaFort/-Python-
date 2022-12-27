# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# # in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def double_system(number):
    num_list = []
    while number != 0:
        num_list.insert(0, number % 2)
        number = number // 2
    return num_list


number = int(input('Введите десятичное число: '))
result = double_system(number)
print(sep="", *result)
