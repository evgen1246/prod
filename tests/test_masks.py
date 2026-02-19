import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("num_card, expected", [
        (1234567899999999, "123456******9999"),
        (1111111111111111, "111111******1111"),

    ])
def test_get_mask_card_number(num_card, expected):
    assert get_mask_card_number(num_card) == expected


@pytest.mark.parametrize("num_card", [111111, 12341234123412345, "abcdefabcdefghijklmno"])
def test_get_mask_card_number_exceptions(num_card):
    with pytest.raises(ValueError):
        get_mask_card_number(num_card)


# @pytest.mark.parametrize("account_number, expected", [(1111111111111111, "**1111"), (1111111111110123, "**0123")])
# def test_get_mask_account(account_number, expected):
#     assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [111111, 12341234123412345, "abcdefabcdefghijklmno"])
def test_get_mask_account_exceptions(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)
