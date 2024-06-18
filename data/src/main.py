import re


def clear_names(file_name: str) -> str:
    """Функция для очистки имен от лишних символов"""
    new_names_list = list()
    with open("data/" + file_name) as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ""
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list


def is_cyrilllic(name_item: str) -> bool:
    """Проверка на вхождение кириллицы в строку"""
    return bool(re.search("а-яА-Я", name_item))


def filter_russian_names(names_list: list) -> list:
    """Фильтрация имен написанных на русском"""
    new_names_list = list()
    for name_item in names_list:
        if is_cyrilllic(name_item):
            new_names_list.append(name_item)
    return new_names_list


if __name__ == "__main__":
    cleared_name = clear_names("names.txt")

    print(filter_russian_names(cleared_name))
