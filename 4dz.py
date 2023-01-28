# print("Python", , "is the best")

# 1.Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# print(f' Введите число n=' )
# n=float(input())
# print(f' Введите число d=')
# d=int(input())
# count=round(n,d)
# print(f'Округляем: {count}')

# 2 Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N=int(input())
# spisok=[]
# for i in range(1,sqrt(N)+1):
#     if N%i==0:
#         print(i)


# def sieve_of_eratosthenes(number: int) -> list: #таблица эратосфена
#     row = {i: '_' for i in range(2, number + 1) if i == 2 or i > 2 and i % 2 != 0}
# # use a dict cause a list too expensive operation for deletion items
#     i = 2
#     while True:
#         if i ** 2 > number:
#             break
#         elif i != 2 and i % 2 == 0:
#             i += 1
#             continue

#         for j in range(i, number + 1, 2):
#             if j * i > number:
#                 break
#             elif (j * i) in row:
#                 del row[j * i]
#         i += 1
#     return list(row)


# def prime_factorization(number: int) -> list:
#     prime_numbers = sieve_of_eratosthenes(number)
#     if number in prime_numbers: return [number]
#     prime_factors = [i for i in prime_numbers if number % i == 0]
#     return prime_factors


# if __name__ == '__main__':
#     print(prime_factorization(2200))
#     print(prime_factorization(239))
#     print(prime_factorization(100))


# 3 Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной 
#  последовательности.
# from math import * 
# my_dict = [2, 4, 5, 21, 2, 4, 67]
# spisok=[]
# for i in range(0,len(my_dict)):
#     for j in range(i,len(my_dict)): #сравниваю каждый элемент списка с каждым элементом
#         if my_dict[i] != my_dict[j] and my_dict[j] not in spisok: #проверяю, чтобы элемент был отличен от других эл-ов и не был в новом списке
#             spisok.append(my_dict[j])
# print(spisok)




#2 вариант
# метод count

# 3
# def main():
#     user_array = []
#     result_array = []
#     user_array = list(map(int, input('Enter sequence of integer numbers. Use space bar to split. ').split()))

#     for element in user_array:
#         if user_array.count(element) == 1:
#             result_array.append(element)
#     print(f'Unique elements in array {user_array} are - ', end='')
#     print(result_array)


# if __name__ == "__main__":
# main()

# 4 Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# from os import system
# system('cls')

# k = int(input('k= '))

# polynominal = ''
# for i in range(k, 0, -1):
#     polynominal += str(random.randrange(0, 101)) + '*x^' + str(i) + ' + '
# polynominal += str(random.randrange(0, 101)) + ' =0'
# print(polynominal)

# with open('polynominal.txt', 'w') as file1:
#     print(polynominal, file=file1, end='')

# или

# def general_koef(n):

#     mnogochlen = ""

#     for i in range(n, -1, -1):
#         rnd = randint(0,10)
#         if rnd != 0:
#             if len(mnogochlen) > 1:
#                 mnogochlen += " + "
#         if i == 0:
#             mnogochlen += str(rnd)
#         else:
#             mnogochlen += str(rnd) + "*x^" + str(i)
#     mnogochlen += " = 0"
#     return mnogochlen

# 5 Даны два файла, в каждом из которых находится 
# запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Открываем 2 наших записанных файла txt, выводим на печать
with open('D:\обучение\Урок 3. Языки программирования\Python\\5dz_5.txt', 'r') as filek:
first1 = filek.read()
with open('D:\обучение\Урок 3. Языки программирования\Python\\5dz_5.txt', 'r') as filek:
second2 = filek.read()

print(f"{first1} Первый многочлен ")
print(f"{second2} Второй многочлен")

# переводим наши многочлены обратно в словарь: ключ значение
def backdictinary(polinomilal: str) -> dict:
    polinomilal = polinomilal.replace('+', '').replace(' x',' 1*x').replace('*x ', '*x**1')
    polinomilal = polinomilal.split()[:-2] # берем срез, чтобы 0 и = отвалились
    dict_equation = {}
    # for i in range(len(polinomilal)):
        # polinomilal[i] = polinomilal[i].split('*x**')
    for item in polinomilal:
        i = item.split('*x**')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        else:
            dict_equation[0] = int(i[0])
    return dict_equation

# выводим на печать первый и второй словарь, который получился из многочленов
dict_equation = backdictinary(first1)
print(dict_equation)

dict_equation = backdictinary(second2)
print(dict_equation)


# суммируем наши многочлены по ключам(если ключа нет,то берется ноль)
def addition(first_eq: dict, second_eq: dict):
    final_eq = {}
    final_eq.update(first_eq)
    final_eq.update(second_eq)
    for key in final_eq:
        final_eq[key] = first_eq.get(key, 0) + second_eq.get(key, 0)
    return final_eq


final_eq = addition(backdictinary(first1), backdictinary(second2))
print(final_eq)

with open("'D:\обучение\Урок 3. Языки программирования\Python\\5dz_5.txt'", "w", encoding='UTF-8') as filek:
filek.write(str(final_eq))






