"""Написать функцию, которая получает на вход два списка
чисел и возвращает новый список,
только те числа, которые есть только в одном из списков.
Пример ввода: [1, 2, 3, 4], [3, 4, 5, 6]
Пример вывода: [1, 2, 5, 6]"""

from typing import List


def get_unique_numbers(list_1: List[int], list_2: List[int]) -> List[int]:
    """Возвращает список тех чисел, которые не повторяются в списках"""
    return list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))


if __name__ == "__main__":
    print(get_unique_numbers(list_1=[1, 2, 3, 4], list_2=[3, 4, 5, 6]))
