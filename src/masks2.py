"""Функция принимает на вход номер счета и возвращает его маску.
Номер счета замаскирован и отображается в формате
**XXXX
. Т. е. видны только последние 4 цифры."""

card = "2842878893689012"
card_number = card.split()[-1]

get_mask_account = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]

chunks, chunk_size = len(get_mask_account), len(get_mask_account) // 1
print(
    " ".join(
        [get_mask_account[i : i + chunk_size] for i in range(10, chunks, chunk_size)]
    )
)
