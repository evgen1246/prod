import src.masks


def mask_account_card(account_and_num: str | int) -> str:
    account_card_split = account_and_num.split()

    for i, word in enumerate(account_card_split):
        if word.isdigit():

            if len(word) == 20:
                account_card_split[i] = src.masks.get_mask_account(word)
            if len(word) == 16:
                account_card_split[i] = src.masks.get_mask_card_number(word)
        account_card = ' '.join(account_card_split)
    return account_card


