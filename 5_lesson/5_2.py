# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# -Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from itertools import groupby
from os import path


def rle_compression(words, code_words):
    if path.exists(words):
        with open(words) as file,\
                open(code_words, "a") as file_2:
            for i in file:
                for j, k in groupby(i):
                    file_2.write("".join(f"{len(list(k))}{j}"))
    else:
        print('Вы пытаетесь открыть файл, которого не существует!')


def rle_recovery(code_words):
    if path.exists(code_words):
        with open(code_words) as file:
            count = ''
            result = ''
            for i in file:
                for j in i:
                    if j.isdigit():
                        count += j
                    else:
                        result += int(count) * j
                        count = ''
    print(result)


rle_compression("text_words.txt", "text_code_words.txt")
rle_recovery("text_code_words.txt")
