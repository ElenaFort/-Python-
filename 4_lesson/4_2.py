# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

def prime_factorization(n):
    i = 2
    multipliers = []
    while i * i <= n:
        while n % i == 0:
            multipliers.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        multipliers.append(round(n))
    return multipliers


print(prime_factorization(int(input("Введите натуральное число N: "))))
