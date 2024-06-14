"""Написать функцию, которая получает на вход
список чисел и возвращает новый список,
содержащий только числа, которые являются палиндропами

Пример ввода: [121, 123, 131, 34543]
Пример вывода: [121, 131, 34543]"""

from typing import List


def get_palindromes(number_list: List) -> List[int]:
    # Возвращает список чисел, который является палиндромами

 #       tmp_list = []
 #       for i in number_list:
 #          if str(i) == str(i)[::-1]:
 #             tmp_list.append(i)
 #       return tmp_list
 return [i for i in number_list if str(i) == str(i)[::-1]]


if __name__ == "__main__":
    print(get_palindromes([121, 123, 131, 34543]))
