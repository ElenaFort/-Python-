# 1. Напишите программу, удаляющую из текста все слова,
# содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

from random import sample


def checking_correctness():

    while True:
        n = input('Введите количество слов: ')
        if not n.isnumeric() or int(n) == 0:
            print('Нужно ввести положительное число! Попробуйте ещё раз!')
        else:
            return (n)


def spisok(count, word='абв'):
    my_list = []
    for i in range(count):
        temp = sample(word, k=3)
        my_list.append("".join(temp))
    return my_list


def get_new_spisok(my_list):
    count = 0
    new_list = []
    for i in my_list:
        if i != 'абв':
            new_list.append(i)

    return new_list


a = spisok(int(checking_correctness()))
print(*a)
print(*get_new_spisok(a))
