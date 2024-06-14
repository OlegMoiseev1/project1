"""Исправьте код, содержащий ошибки PEP 8 и плохой
нейминг. Добавьте docstring и аннотации типов. Flake8 и
mypy не должны выдавать ошибок."""


def circle_area(r: float) -> float:
    """Подсчет площади окружности"""
    pi = 3.14
    # circle_area = pi * r**2
    return pi * r**2


def format_description(r: float, area: float):
    """Форматированный вывод информации об окружности"""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_circle_info(r: float) -> None:
    """Получение информации об окружности"""
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


if __name__ == "__main__":
    radius = int(input("Enter circle radius (int): "))
    get_circle_info(radius)
