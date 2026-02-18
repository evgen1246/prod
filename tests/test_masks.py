import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "num_card, expected",
    [
        (1234567899999999, "1234 56** **** 9999"),
        (1111111111111111, "1111 11** **** 1111"),
        ("0001234567890123", "0001 23** **** 0123"),
    ],
)
def test_get_mask_card_number(num_card, expected):
    assert get_mask_card_number(num_card) == expected


@pytest.mark.parametrize("num_card", [111111, 12341234123412345, "abcdefabcdefghijklmno"])
def test_get_mask_card_number_exceptions(num_card):
    with pytest.raises(ValueError):
        get_mask_card_number(num_card)


@pytest.mark.parametrize("num_card, expected", [(1111111111111111, "**1111"), (1111111111110123, "**0123")])
def test_get_mask_account(num_card, expected):
    assert get_mask_account(num_card) == expected


@pytest.mark.parametrize("num_card", [111111, 12341234123412345, "abcdefabcdefghijklmno"])
def test_get_mask_account_exceptions(num_card):
    with pytest.raises(ValueError):
        get_mask_account(num_card)
