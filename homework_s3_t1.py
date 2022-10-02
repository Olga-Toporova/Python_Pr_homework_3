'''
1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
in
5
out
[10, 2, 3, 8, 9]
22

in
4
out
[4, 2, 4, 9]
8
'''
from random import randrange

def new_list (number):
    num_list = []
    for i in range(number):
        num_list.append(randrange(number+1))
    return num_list

def sum_odd_position(num_list):
    length = len(num_list) 
    return sum(num_list[i] for i in range(0, length, 2))

N = int(input("Введите количество элементов: "))
result_list = new_list(N)
print(result_list)
print(sum_odd_position(result_list))
