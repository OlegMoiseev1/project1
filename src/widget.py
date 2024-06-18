def mask_account_card(cards_number: str) -> str:
    """Функия для маскировки счетов и карт"""
    if "Счет" in cards_number:
        mask_account = f"Счет {get_mask_account_card(card_number[:])}"
        return mask_account
    else:
        card = get_mask_card_numder(cards_number[-16:])
        mask_card = cards_number.replace(cards_number[-16:], card)
        return mask_card


def get_data(data: str) -> str:
    """Функия преобразовывания даты и времени"""
    d = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%fZ"))

    return d.strftime("%d.%m.%Y")


if __name__ == "__main":
    print(mask_account_card("Maestro:1596837868705199"))
    print(get_data("2018-07-11T02:26:18.671407"))
