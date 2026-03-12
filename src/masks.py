import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(num_card: int | str) -> str:
    """
    Принимает на вход номер карты и возвращает её маску.
    Видны первые 6 цифр и последние 4 цифры.

    """

    num_card = str(num_card)
    logger.info(f"Получен номер карты: {num_card}")
    if len(num_card) != 16 or not num_card.isdigit():
        logger.error("Ошибка: Не содержит 16 цифр")
        raise ValueError("Номер карты должен содержать 16 цифр!")

    mask_card = f"{num_card[:6]}******{num_card[-4:]}"
    logger.info(f"Маскиовка карты успешна: {mask_card}")

    return mask_card


def get_mask_account(account_number: int | str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    """
    account_number = str(account_number)
    logger.info(f"Получен номер счета: {account_number}")
    if len(account_number) != 20 or not account_number.isdigit():
        logger.error("Ошибка: Не содержит 20 цифр")
        raise ValueError("Номер счета должен содержать 20 цифр.")

    mask = f"**{account_number[-4:]}"
    logger.info(f"Маскиовка счёта успешна: {mask}")

    return mask
