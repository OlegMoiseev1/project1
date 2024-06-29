def filter_by_state(operations: list, state: str = "EXECUTED") -> list[dict]:
    """Фунцкия которая получает список словарей и возвращает новый спиоок,
    содержащий только те словари, у которых ключ state содержит переданное
    в функцию значение"""

    filtered_operations = []
    for item in operations:
        if item.get("state") == state:
            filtered_operations.append(item)

    return filtered_operations


def sort_by_date(operations: list, reverse: bool = True) -> list[dict]:
    """Функция которая возвращает список по убыванию"""
    sortted_operations = sorted(
        operations, key=lambda x: x["reverse"], reverse=reverse
    )
    return sortted_operations


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )
