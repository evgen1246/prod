import re
from collections import Counter
from pathlib import Path

import pandas as pd


def read_transactions_from_csv(path_file: Path) -> list:
    """Принимает путь к файлу CSV и выдает список словарей с транзакциями."""
    path_file = Path(path_file)

    if not path_file.exists():
        raise FileNotFoundError(f"Файл не найден: {path_file}")

    try:
        df = pd.read_csv(path_file, sep=';')
    except Exception as e:
        print(f"Ошибка при чтении CSV файла {path_file}: {e}")
        return []

    # Проверка, что df не пустой после чтения
    if df.empty:
        print(f"Предупреждение: CSV файл {path_file} пуст или не содержит данных.")
        return []

    operation = df.to_dict(orient="records")
    return operation


def read_transactions_from_excel(path_file: Path) -> list:
    """Принимает путь к файлу Excel и выдает список словарей с транзакциями."""
    path_file = Path(path_file)

    if not path_file.exists():
        raise FileNotFoundError(f"Файл не найден: {path_file}")
    df = pd.read_excel(path_file)
    operation = df.to_dict(orient="records")
    return operation


def process_bank_search(transactions: list[dict], search: str) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска
    далее возвращает список словарей,
    у которых в описании есть данная строка.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    transaction_filter = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]

    return transaction_filter


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict:
    """Функция подсчёта операций по категориям"""
    category_list = [
        transaction.get("description") for transaction in transactions if transaction.get("description") in categories
    ]

    category_count = Counter(category_list)
    return dict(category_count)


def process_bank_operations(transactions: list[dict], categories: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """

    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
    return category_count
