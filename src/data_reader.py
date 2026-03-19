from pathlib import Path

import pandas as pd
import re

from unicodedata import category

from tests.conftest import description


def read_transactions_from_csv(path_file: Path) -> list:
    """Принимает путь к файлу CSV и выдает список словарей с транзакциями."""

    path_file = Path(path_file)

    if not path_file.exists():
        raise FileNotFoundError(f"Файл не найден: {path_file}")

    df = pd.read_csv(path_file)
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


def process_bank_search(transactions:list[dict], search:str)->list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска
    далее возвращает список словарей,
    у которых в описании есть данная строка.
     """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    transaction_filter = [
        transaction for transaction in transactions if pattern.search(transaction.get('description', ''))
    ]
    return transaction_filter


def process_bank_operations(transactions:list[dict], categories:list)->dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """

    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('descriptions', '').lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
    return  category_count

