"""
Написать функцию, которая получает на вход два
списка чисел и возвращает новый список, содержащий
только те числа, которые встречаются в обоих списках.

Пример ввода:

[1, 2, 3, 4], [3, 4, 5, 6]

Пример вывода:

[3, 4]"""

from typing import List


def get_same_numbers(list_1: List[int], list_2: List[int]) -> List[int]:
    # Функция для получения одинаковых чисел в списках
    tmp_list = list()
    for i in list_1:
        if i in list_2:
            tmp_list.append(i)

    return tmp_list


if __name__ == "__main__":
    print(get_same_numbers(list_1=[1, 2, 3, 4], list_2=[3, 4, 5, 6]))
