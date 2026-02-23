from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


def test_card_number_generator(num_card):
    assert list(card_number_generator(1, 5)) == num_card
    assert len(list(card_number_generator(1, 5))) == 5
