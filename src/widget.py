from src import masks


def mask_account_card(srting: str, mask_account=None) -> str:
    """Функия для маскировки счетов и дат"""
    if "Счет" in mask_account:
        account = mask_account[-20:]
        return mask_account[:20] + masks.get_mask_account(account)
    else:
        number_card = "".join(srting[-16:].split())
        return mask_account[:-16] + masks.get_mask_card_number(number_card)


# print(mask_account_card('Maestro:1596837868705199'))


def get_data(info_data: str) -> str:
    """Функия преобразовывания даты и времени"""
    data_day = info_data.split("T")[0]

    return f"{data_day.split('-')[-1]}.{data_day.split('-')[-2]}.{data_day.split('-')[-3]}"


# print(get_data('018-07-11T02:26:18.671407))
