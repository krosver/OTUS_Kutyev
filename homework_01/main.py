"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*numbers):
    return [number**2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    i=1
    k=0
    while i < number:
        if number % i == 0:
            k+=1
        i+=1
    if k==1:
        return True

def filter_numbers(numbers, argument):
    if argument == EVEN:
        return [number for number in numbers if number % 2 == 0]
        # return filter(lambda number: number % 2 == 0)
    if argument == ODD:
        return [number for number in numbers if number % 2 != 0]
        # return filter(lambda number: number % 2 == 1)
    if argument == PRIME:
        return list(filter(is_prime,numbers))

