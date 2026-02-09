from datetime import datetime


def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state."""

    filtered_data = [item for item in data if item.get('state', '').lower() == state.lower()]
    return filtered_data


def sort_by_date(data: list[], reverse_order: bool = True) -> list:
    """Сортирует список словарей по дате в указанном порядке(убывание)"""
    return sorted(data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse_order)
