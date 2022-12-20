# 5. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099


x1 = int(input('Введите координату х для первой точки: '))
y1 = int(input('Введите координату у для первой точки: '))
x2 = int(input('Введите координату х для второй точки: '))
y2 = int(input('Введите координату у для второй точки: '))
tempX = (x2 - x1) * (x2 - x1)
tempY = (y2 - y1) * (y2 - y1)
result = (tempX + tempY)**0.5
print(round(result, 3))
