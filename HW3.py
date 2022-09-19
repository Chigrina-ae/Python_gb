# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
#
# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.
# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().


#1
# def del_a_b (a, b):
#     try:
#         d = a / b
#         print(f'a/b= {d}')
#     except ZeroDivisionError:
#         print('You can_t del by 0')
#
# a = int(input('enter number a = '))
# b = int(input('enter number b = '))
# del_a_b(a, b)

#2
# def person_info (name, surname, year, city, email, tel):
#     print(f'Name - {name}; Surname - {surname}; Year of birth - {year}; City from - {city}; Email - {email}; Phone - {tel}')
#
# n = input('Enter name ')
# s = input('Enter surname ')
# y = input('Enter year of birth ')
# c = input('Enter city ')
# e = input('Enter email ')
# p = input('Enter phone number ')
#
# person_info(name=n, surname=s, year=y, city=c, email=e, tel=p)

#3
# def my_func(a, b, c):
#     max_ = [a, b, c]
#     max_.sort()
#     sum_ = int(max_[1]) + int(max_[2])
#     return(sum_)
#
# fir = input('Enter first num ')
# sec = input('Enter second num ')
# thi = input('Enter third num ')
#
# print(my_func(fir, sec, thi))

#4.1
# def my_func(a, b):
#     i = 0
#     res = 1
#     while i < (b * -1):
#         res = res / a
#         i = i + 1
#     return(res)
#
# f = 0
# while f == 0:
#     pos = int(input('Enter positive num '))
#     neg = int(input('Enter negative num '))
#     if (pos < 0) or (neg > 0):
#         print('it_s not correct num')
#     else:
#         f = 1
#
# print(my_func(pos, neg))

#4.2
# def my_func(a, b):
#     res = a ** b
#     return(res)
#
# f = 0
# while f == 0:
#     pos = int(input('Enter positive num '))
#     neg = int(input('Enter negative num '))
#     if (neg > 0) or (pos < 0):
#         print('it_s not correct num')
#     else:
#         f = 1
#
# print(my_func(pos, neg))

#5
# def find_sum(end_find):
#     sum_data = 0
#     f = 0
#     while f == 0:
#         data = input('enter num ').split()
#         for num in data:
#             if num == end_find:
#                 f = 1
#                 break
#             else:
#                 sum_data = sum_data + int(num)
#         print(f'Interim amount = ', sum_data)
#     return(sum_data)
#
# end_list = input('enter end symbol ')
# print(f'Total amount = ', find_sum(end_list))

#6
# def int_func(word_upp):
#     word_upp = word_upp.capitalize()
#     return(word_upp)
# word = input('enter text ')
# print(int_func(word))

#7
def int_func(text_upp):
    text_upp = text_upp.title()
    return(text_upp)
text = input('enter text ')
print(int_func(text))
