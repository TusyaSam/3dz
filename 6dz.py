
# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные 
# (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.
# считываем данные




# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# from math import *

# ax = int(input("Введите координату x первой точки: "))
# ay = int(input("Введите координату y первой точки: "))
# bx = int(input("Введите координату x второй точки: "))
# by = int(input("Введите координату y первой точки: "))

# result = round(sqrt((bx - ax)**2 + (by - ay)**2), 2)
# print(result)

# стало
from functools import reduce
dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def dot_range(dot_1, dot_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(rng, 2)
print(dot_range(dot_1, dot_2))






# Вычисление факториала числа

# import os
# from math import factorial
# os.system('cls')

# num = int(input("Введите число: "))
# spisok = []
# result = 1
# for i in range(1, num+1):
#     result *= i
#     spisok.append(result)

# print(spisok)

# стало
n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))