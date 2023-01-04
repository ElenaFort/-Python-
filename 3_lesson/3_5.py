# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fibonacci(n):
    fibo = []
    f0, f1 = 0, 1
    for i in range(n + 1):
        fibo.append(f0)
        f0, f1 = f1, f0 + f1 
    f0, f1 = 0, 1
    for i in range(n):
        f0, f1 = f1, f0 - f1
        fibo.insert(0, f0)
    print(*fibo)


fibonacci(int(input('Введите длину ряда: ')))
