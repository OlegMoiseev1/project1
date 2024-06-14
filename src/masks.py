"""Функция принимает на вход номер карты и возвращает ее маску.
Номер карты замаскирован и отображается в формате
XXXX XX** **** XXXX
. Т. е. видны первые 6 цифр и последние 4, номер разбит по
блокам по 4 цифры, разделенным пробелами."""

card = "2842878893689012"
card_number = card.split()[-1]

get_mask_card_number = (
    card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
)

chunks, chunk_size = len(get_mask_card_number), len(get_mask_card_number) // 4
print(
    " ".join(
        [get_mask_card_number[i : i + chunk_size] for i in range(0, chunks, chunk_size)]
    )
)
