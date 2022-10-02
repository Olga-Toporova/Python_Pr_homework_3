'''
5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Негафибоначчи
in
8
out
-21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

in
5
out
5 -3 2 -1 1 0 1 1 2 3 5
'''

def fibonachi(number):
    fib1, fib2 = 1, 1
    fibonachi1 = [-1, 1, 0, fib1, fib2]
    for i in range(number-2):
        fib1, fib2 = fib2, fib1 + fib2
        fibonachi1.append(fib2)
        if i % 2 != 0:
            fib3 = fib2 * -1
            fibonachi1.insert(0, fib3)
        else:
            fibonachi1.insert(0, fib2)

    print(fibonachi1)


n = int(input("Введите число: "))
fibonachi(n)
