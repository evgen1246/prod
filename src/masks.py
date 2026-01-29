from typing import Union


def get_mask_card_number(num_card: Union[int, str], count_mask: int = 6) -> str:
    """
    Принимает на вход номер карты и возвращает её маску.
    Видны первые 6 цифр и последние 4 цифры.

    """
    num_card = str(num_card)
    mask = num_card[:6] + "*" * count_mask + num_card[-4:]
    blocks = [mask[i: i + 4] for i in range(0, len(mask), 4)]
    # Объединяем блоки с пробелами
    result = " ".join(blocks)

    return result


def get_mask_account(num_card: Union[int, str]) -> str:
    """
    Принимает на вход номер карты и возвращает её маску.
    Видны только последние 4 цифры номера,
    а перед ними — две звездочки.
    """

    num_card = str(num_card)
    mask = "**" + num_card[-4:]
    # Объединяем блоки с пробелами

    return mask


