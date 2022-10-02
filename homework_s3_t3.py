'''
3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Без использования встроенной функции преобразования, без строк.
in
88
out
1011000

in
11
out
1011
'''


def turn_into_number(num):
    result = []

    while num > 0:
        to_binary = num % 2
        result.append(to_binary)
        num //= 2
        reverse_result = result[::-1]
    return reverse_result


number = int(input("Введите число: "))
print(turn_into_number(number))
