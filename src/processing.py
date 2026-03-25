def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state.
    """
    filtered_data = [
        item
        for item in data
        if isinstance(item, dict)
        and isinstance(item.get("state"), str)
        and item.get("state").lower() == state.lower() == state.lower()
    ]

    return filtered_data


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Сортирует список словарей по дате в порядке убывания (по умолчанию)
    """
    if not isinstance(data, list):
        return []
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
