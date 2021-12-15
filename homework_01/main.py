"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(numbers):
    return [number**2 for number in numbers]

numbers = [1,2,5,7]
power_numbers(numbers)


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
    if argument == "even":
        return [number for number in numbers if number % 2 == 0]
    if argument == "odd":
        return [number for number in numbers if number % 2 != 0]
    if argument == "prime":
        return [number for number in numbers if is_prime(number) == True]


numbers = [1,2,3,4,5,6]
filter_numbers(numbers, PRIME)

