'''
2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
in
4
out
[2, 5, 8, 10]
[20, 40]

in
5
out
[2, 2, 4, 8, 8]
[16, 16, 4]
'''
from random import randrange


def new_list(number):
    num_list = []
    for i in range(number):
        num_list.append(randrange(11))
    return num_list


def result_sum(origin_list):
    result = []
    length = len(origin_list)
    for i in range(length // 2):
        result.append(origin_list[i] * origin_list[length - 1 - i])
    if length % 2 != 0:
        result.append(origin_list[length // 2 ])
    print(result)


n = int(input("Введите количество элементов: "))
result_list = new_list(n)
print(result_list)
result_sum(result_list)
