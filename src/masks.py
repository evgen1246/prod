from typing import Union


def get_mask_card_number(num_card: Union[int, str], count_mask: int = 6) -> str:
    """
    Принимает на вход номер карты и возвращает её маску.
    Видны первые 6 цифр и последние 4 цифры.

    """

    num_card = str(num_card)
    if len(num_card) != 16 or not num_card.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр!")

    mask_card = f"{num_card[:6]}******{num_card[-4:]}"

    return mask_card


def get_mask_account(account_number: Union[int, str]) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    """

    account_number = str(account_number)
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать 20 цифр.")

    mask = f"**{account_number[-4:]}"


    return mask
