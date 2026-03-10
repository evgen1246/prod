import json
import os
from typing import Dict, List


def load_transactions(file_path: str) -> List[Dict]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    """
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []

    except json.JSONDecodeError:
        return []
