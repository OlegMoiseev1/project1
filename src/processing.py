def filter_by_stste(old_list: list, state: str = "EXECUTED") -> list[str]:
    """Фунцкия которая получает список словарей и возвращает новый спиоок,
    содержащий только те словари, у которых ключ state содержит переданное
    в функцию значение"""

    new_list = []
    for i in old_list:
        if i.get("state") == state:
            new_list.append(i)

    return new_list


def sort_by_date(old_list: list, date: bool = True) -> list[str]:
    """Функция которая возвращает список по убыванию"""
    sortted_old_list = sorted(old_list, key=lambda x: x["date"], reverse=date)
    return sortted_old_list


if __name__ == "__main__":
    print(
        filter_by_stste(
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
