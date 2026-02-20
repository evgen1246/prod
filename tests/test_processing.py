from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(test_data):
    res_executed = filter_by_state(test_data)
    assert len(res_executed) == 2
    assert all(item["state"] == "EXECUTED" for item in res_executed)


def test_sort_by_date(test_data, test_sort_date):
    assert sort_by_date(test_data) == test_sort_date
