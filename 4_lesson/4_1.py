# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

from decimal import Decimal


def calculate_number(a, d):
    number = Decimal(a)
    number = number.quantize(Decimal(d))
    print(number)


calculate_number(input("Введите действительное число: "),
                 input("Введите требуемую точность: "))
