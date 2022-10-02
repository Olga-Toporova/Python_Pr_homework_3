'''
4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
in
5
out
[5.16, 8.62, 6.57, 7.92, 9.22]
Min: 0.16, Max: 0.92. Difference: 0.76
'''
from random import random
from copy import copy

def max_min_difference(number):
    num_list = []
    for i in range(number):
        num_list.append(round((random()*10), 2))
    print(num_list)
    new_list = copy(num_list)
    i=0
    while i < len(num_list):
        number1 = (new_list[i] * 10 //10) 
        number2 = num_list[i]
        num_list[i] = round((number2 - number1), 2)
        i+=1
    print(num_list)
    minimum = min(num_list)
    print(minimum)
    maximum = max(num_list)
    print(maximum)
    print(maximum - minimum)

    

num = int(input("Введите количество элементов: "))
max_min_difference(num)


