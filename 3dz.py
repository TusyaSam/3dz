
# 1 Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random
# def summa_nechet_elem_spiska(def_list):
#     sum=0
#     for i in range(len(def_list)):
#         if i %2!=0:
#             sum+= def_list[i]
#     return sum

# lenght_list=10
# my_list=[random.randint(0,10) for i in range(lenght_list)]
# my_odd_list=[my_list[i] for i in range(lenght_list) if i%2!=0]
# print(f'{my_list} элементы нечетных позиций {my_odd_list}, ответ {summa_nechet_elem_spiska(my_list)}')


# 2 Напишите программу, которая найдёт произведение пар
#  чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def proz_par_elem_spiska(array: list[int])->list[int]:
#     spisok=[]
#     for i in range(int(len(array)//2+len(array)%2)):  #for i in range(ceil(len(array)/2)):
#         spisok.append(array[i]*array[-(i+1)])
#     return spisok

# print(proz_par_elem_spiska([2,3,4,5,6]))
# print(proz_par_elem_spiska([2,3,5,6]))

# метод ceil округляет вверх

# 3 Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# import math

# lenght_list=5
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# my_tail_list=[round(my_list[i]-int(my_list[i]),2) for i in range(lenght_list)]
# my_shorttail_list=[]
# for i in range(lenght_list):
#     if my_tail_list[i]:
#         my_shorttail_list.append(my_tail_list[i])

# print(f"{my_list}-> {my_shorttail_list}-> {max(my_shorttail_list)-min(my_shorttail_list)}")

# 4 Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n= int(input("число N: "))
## print (f"число N  в двоичной: {bin(n)}")

b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)


# 5 Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


# Семинар


# 1. Задайте строку из набора чисел. Напишите программу, которая покажет 
# большее и меньшее число. В качестве символа-разделителя используйте пробел.


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python


# 3. Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.