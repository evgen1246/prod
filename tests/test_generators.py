import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.conftest import num_card


def test_filter_by_currency(test_filter):
    usd_transactions = list(filter_by_currency(test_filter, "USD"))
    rub_transactions = list(filter_by_currency(test_filter, "RUB"))
    assert len(usd_transactions) == 1
    assert len(rub_transactions) == 2

    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0

    no_currency = list(filter_by_currency(test_filter, "EUR"))
    assert len(no_currency) == 0


def test_transaction_descriptions(test_filter, description):
    descriptions = list(transaction_descriptions(test_filter))
    assert len(descriptions) == 3

    assert descriptions == description


# @pytest.mark.parametrize("start","stop" num_card)
def test_card_number_generator(num_card):
    assert list(card_number_generator(1, 5)) == num_card
    assert len(list(card_number_generator(1, 5))) == 5


@pytest.mark.parametrize("start, stop, expected", [(1, 5,
                                                  ["0000 0000 0000 0001",
                                                   "0000 0000 0000 0002",
                                                   "0000 0000 0000 0003",
                                                   "0000 0000 0000 0004",
                                                   "0000 0000 0000 0005"])])
def test_card_generator(start, stop, expected):
    gen_num = list(card_number_generator(start, stop))
    assert  gen_num == expected
