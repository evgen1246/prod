import src.masks


def mask_account_card(account_and_num: str | int) -> str:
    """Функция, которая маскирует номера счетов и карт"""
    account_card_split = account_and_num.split()

    for i, word in enumerate(account_card_split):
        if word.isdigit():

            if len(word) == 20:
                account_card_split[i] = src.masks.get_mask_account(word)
            if len(word) == 16:
                account_card_split[i] = src.masks.get_mask_card_number(word)
        account_card = ' '.join(account_card_split)
    return account_card

def get_date(date_full: str)->str:
    """Функция возврщает значение даты по формату "ДД.ММ.ГГГГ" """

    year = date_full[:4]
    month = date_full[5:7]
    day = date_full[8:10]
    date_only = f'{day}.{month}.{year}'

    return date_only

