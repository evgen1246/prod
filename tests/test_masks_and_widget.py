import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "num_card, expected",
    [
        (1234567899999999, "123456******9999"),
        (1111111111111111, "111111******1111"),
        (1787897897878978, "178789******8978"),
        (1100111001100111, "110011******0111"),
    ],
)
def test_get_mask_card_number(num_card, expected):
    assert get_mask_card_number(num_card) == expected


@pytest.mark.parametrize("num_card", [111111, 12341234123412345, "abcdefabcdefghijklmno"])
def test_get_mask_card_number_exceptions(num_card):
    with pytest.raises(ValueError):
        get_mask_card_number(num_card)


@pytest.mark.parametrize("account_number", [111111, 12341234123412345, "abcdefabcdefghijklmno"])
def test_get_mask_account_exceptions(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)

@pytest.mark.parametrize("num_card, expected", [(11111111111111111111, "**1111"), (11111111111111110123, "**0123")])
def test_get_mask_account(num_card, expected):
    assert get_mask_account(num_card) == expected

def test_get_date():
    assert get_date("2026-10-10T02:26:18.000000") == "10.10.2026"
    assert get_date("2025-02-25T15:45:30.000000") == "25.02.2025"




def test_widget():
    assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 700079******6361'
    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'

