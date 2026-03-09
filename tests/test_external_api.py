import json
from unittest.mock import mock_open, patch

from src.external_api import transaction_convert
from src.utils import load_transactions


@patch("requests.get")
def test_transaction_convert(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500}  # Симулируем ответ API
    transaction = {"amount": 100, "currency": "USD"}  # Тестовая транзакция
    assert transaction_convert(transaction) == 7500.0


@patch("os.path.exists", return_value=True)
def test_load_transactions(mock_open_one):
    with patch("builtins.open", mock_open(read_data="[]")):
        assert load_transactions("fake_path.json") == []

    with patch("builtins.open", mock_open(read_data="{}")):
        assert load_transactions("fake_path.json") == []

    with patch("builtins.open", side_effect=json.JSONDecodeError("", "", 0)):
        assert load_transactions("fake_path.json") == []


@patch("os.path.exists", return_value=False)
def test_load_transactions_false(mock_open_one):
    assert load_transactions("fake_path.json") == []
