from unittest.mock import patch


from src.data_reader import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
@patch("os.path.exists", return_value=True)
def test_read_transactions_from_csv(mock_exists, mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [{"amount": 10, "currency": "USD"}]
    result = read_transactions_from_csv("file_path.csv")
    assert result == [{"amount": 10, "currency": "USD"}]


@patch("pandas.read_excel")
@patch("os.path.exists", return_value=True)
def test_read_transactions_from_excel(mock_exists, mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [{"amount": 111, "currency": "USD"}]
    result = read_transactions_from_excel("file_path.excel")
    assert result == [{"amount": 111, "currency": "USD"}]
