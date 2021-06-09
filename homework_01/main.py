"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*list_of_numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in list_of_numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_odd(x):
    return x % 2 != 0


def is_even(x):
    return x % 2 == 0


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x < 2:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True


types = {
    ODD: is_odd,
    EVEN: is_even,
    PRIME: is_prime
}


def filter_numbers(list_of_numbers, type_of_numbers):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    func = types[type_of_numbers]

    return [num for num in list_of_numbers if func(num)]
